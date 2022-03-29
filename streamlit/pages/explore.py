import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def app():
    def file_selector(folder_path='.'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a file', filenames)
        return os.path.join(folder_path, selected_filename)
    filename = file_selector()
    st.write('You selected `%s`' % filename)
    st.markdown("<h3 style = 'color : #ff4b4b'> Model</h3>",unsafe_allow_html=True)
    with st.expander("Model Information", expanded=True):
        st.markdown(
            "<p> Algoritma yang digunakan : <span style = 'color : #ff4b4b'> Logistic Regression</span></p>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", "0.79")
        col2.metric("Recall", "0.68")
        col3.metric("Precision", "0.60")
        col4.metric("F1 Score", "0.64")
        st.write(
            "<p style = 'margin : 0px' ><b style = 'color : #ff4b4b'>Accuracy :</b> Model memprediksi benar 79 dari customer yang ada</p>", unsafe_allow_html=True)
        st.write(
            "<p style = 'margin : 0px'><b style = 'color : #ff4b4b'>Recall :</b>  Model gagal memprediksi 32 customer dari 100 customer yang sebenarnya akan churn (False Negative)</p>", unsafe_allow_html=True)
        st.write(
            "<p style = 'margin : 0px'><b style = 'color : #ff4b4b'>Precision :</b> Model gagal memprediksi 40 dari 100 customer yang sebenarnya tidak akan churn (False Positive)</p>", unsafe_allow_html=True)
        st.write("<p><b style = 'color : #ff4b4b'>F1 Score : </b>gabungan dari Recall dan Precision</p>",
                 unsafe_allow_html=True)
        st.markdown("<h5> Data Training </h5>", unsafe_allow_html=True)
        df = pd.read_csv('../data/data.csv', index_col=0)
        st.write(df.head())
    with st.expander("Feature Importance", expanded=True):
        feat_imp = pd.read_csv("/data/feat_imp.csv", index_col=0)
        fig = plt.figure(figsize=(10, 10))
        sns.barplot(x=feat_imp['importance'], y=feat_imp['feature'])
        plt.title('Feature Importance')
        plt.xlabel('Feature')
        plt.ylabel('Importance')
        st.pyplot(fig)

    st.markdown("<h3 style = 'color : #ff4b4b'> Data Insight </h3>",
                unsafe_allow_html=True)
    with st.expander("Contract Vs Churn", expanded=True):
        col1_contract, col2_contract = st.columns(2)
        with col1_contract:
            fig, ax = plt.subplots(figsize=(6, 3))
            sns.countplot(x="Contract", hue="Churn",
                          data=df, palette=["#008bfb", "#ff4b4b"], dodge=False).set_ylabel("")
            st.pyplot(fig)
        with col2_contract:
            st.write('Grafik disamping merupakan grafik jumlah customer yang churn berdsarkan kontraknya, dapat dilihat bahwa  customer yang memiliki kontrak Month-to-Month memiliki jumlah Churn yang lebih tinggi daripada kontrak lainnya. bisa dilihat juga kontrak two year memiliki jumlah customer churn yang sedikit. ')

    with st.expander("Metode pembayaran dengan persentase churn tinggi", expanded=True):
        col1_payment, col2_payment = st.columns(2)
        with col1_payment:
            fig, ax = plt.subplots(figsize=(10, 3))
            sns.countplot(x="PaymentMethod", hue="Churn",
                          data=df, dodge=False, palette=["#008bfb", "#ff4b4b"]).set_ylabel("")
            st.pyplot(fig)
        with col2_payment:
            st.write("Grafik disamping emrpakan grafik jumlah customer dengan metode pembayarannya, dapat dilihat bahwa di data ini terdapat 4 metode pembayaran. Dari keempat metode tersebut, metode pembayaran menggunakan elektronik check memiliki jumlah customer yang Churn yang lebih banyak daripada metode pembayaran lainnya.")
    with st.expander("Karakteristik pelanggan berdasarkan biaya bulanan", expanded=True):
        col1_month, col2_month = st.columns(2)
        with col1_month:
            fig, axes = plt.subplots(figsize=(6, 3))
            ax1 = sns.kdeplot(
                x="MonthlyCharges", data=df[df.Churn == "Yes"], color="#ff4b4b", label="Churn")
            ax2 = sns.kdeplot(
                x="MonthlyCharges", data=df[df.Churn == "No"], color="#008bfb", label="Not Churn")
            ax1.legend()
            ax1.set_ylabel("")
            ax2.set_ylabel("")
            st.pyplot(fig)
        with col2_month:
            st.write("Grafik disamping merupakan distribusi pembayaran bulanan tiap customer, grafik disamping menunjukan bahwa customer yang akan churn cenderung memiliki pembayaran bulanan di angka 60-120, sedangkan untuk customer yang tidak churn, ada di angka < 40.")
    with st.expander("Proporsi Customer yang Churn dan tidak", expanded=True):
        col1_churn, col2_churn = st.columns(2)
        with col1_churn:
            # make pie chart
            labels = 'Churn', 'Not Churn'
            sizes = [df[df.Churn == "Yes"].shape[0],
                     df[df.Churn == "No"].shape[0]]
            colors = ["#ff4b4b", "#008bfb"]
            explode = (0.1, 0)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
            ax1.axis('equal')
            st.pyplot(fig1)
        with col2_churn:
            st.write("Grafik disamping merupakan proporsi customer yang churn dan tidak churn, dapat dilihat bahwa di data ini customer yang tidak churn, memiliki presentase yang lebih besar daripada customer yang churn, oleh karena itu, pengukuran menggunakan accuracy dirasa kurang tepat.")
