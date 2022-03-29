import streamlit as st
import pandas as pd
import numpy as np
import shap
import pickle


def app():
    with open('./streamlit/styling/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    #import model
    with open('./streamlit/model/model_logreg.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('./streamlit/model/proc.pkl', 'rb') as b:
        proc = pickle.load(b)

    with open('./streamlit/model/explainer.pkl', 'rb') as e:
        explainer_sh = pickle.load(e)

    # set streamlit layout size

    st.markdown("<h2 style = 'color : #ff4b4b'>  Individual Customer Prediction </h2>",
                unsafe_allow_html=True)

    st.write("page ini digunakan untuk memprediksi secara individual apakah customer akan cenderung churn atau tidak.")
    st.write("dengan menggunakan individual prediction, kita dapat mengetahui secara lebih detail bagaimana model bisa memprediksi bahwa customer tersebut akan churn atau sebaliknya.")

    left_column, right_column = st.columns(2)

    # Or even better, call Streamlit functions inside a "with" block:
    with left_column:
        st.markdown('<h4 style = "color:  #ff4b4b">Informasi Mengenai Pembayaran</h4>',
                    unsafe_allow_html=True)
        # contract form
        contract = st.selectbox(
            'Customer Contract',
            ['Month-to-month', 'One year', "Two year"],
            key="contract"
        )

        # payment form
        payment = st.selectbox(
            'Payment Method',
            ['Electronic check', 'Mailed check',
             "Bank transfer (automatic)", "Credit card (automatic)"],
            key="payment"
        )

        month_charge = st.number_input(
            'Monthly Charge', min_value=0.0, max_value=800.0, step=50.0)
        total_charge = st.number_input(
            'Total Charge', min_value=0.0, max_value=8000.0, step=1000.0)

    with right_column:
        st.markdown('<h4 style = "color:  #ff4b4b">Informasi Mengenai Layanan</h4>',
                    unsafe_allow_html=True)
        # add multiple checkbox streamlit
        is_internet = st.selectbox(
            'is Customer have internet Service?',
            ['DSL', "Fiber optic", "No"],
            key='internet'
        )
        options_is_internet = []
        list_internet = ['Online Security', 'Online Backup', 'Device Protection',
                         'Tech Support', "Streaming Tv", "Streaming Movies"]
        internet_col = []
        if is_internet != 'No':
            options_is_internet = st.multiselect(
                'List Customer Internet Services',
                list_internet,
            )
            for i in list_internet:
                if i in options_is_internet:
                    internet_col.append("Yes")
                else:
                    internet_col.append("No")
        else:
            for i in list_internet:
                internet_col.append("No internet service")

        is_phone = st.selectbox(
            'is Customer have phone Service?',
            ['Yes', "No"],
            key='phone'
        )
        phone_col = []
        options_is_phone = []
        list_phone = ['Multiple Lines']
        if is_phone != 'No':
            options_is_phone = st.multiselect(
                'List Customer Phone Services',
                list_phone,
            )
            for i in list_phone:
                if i in options_is_phone:
                    phone_col.append("Yes")
                else:
                    phone_col.append("No")
        else:
            phone_col.append("No phone service")

    st.markdown('<h4 style = "color:  #ff4b4b"> Hasil Input Data </h4>',
                unsafe_allow_html=True)
    with st.spinner("Loading..."):
        df = pd.DataFrame(
            {
                "PhoneService": [is_phone],
                "MultipleLines": [phone_col[0]],
                "InternetService": [is_internet],
                "OnlineSecurity": [internet_col[0]],
                "OnlineBackup": [internet_col[1]],
                "DeviceProtection": [internet_col[2]],
                "TechSupport": [internet_col[3]],
                "StreamingTV": [internet_col[4]],
                "StreamingMovies": [internet_col[5]],
                "Contract": [contract],
                "PaymentMethod": [payment],
                "MonthlyCharges": [month_charge],
                "TotalCharges": [total_charge]}
        )
        st.dataframe(df)

    st.write('---')
    # create submit button
    st.markdown('<h4 style = "color:  #ff4b4b">Prediksi Customer</h4>',
                unsafe_allow_html=True)

    if st.button('Prediksi'):
        # create dataframe
        # predict
        prediction = model.predict(df)
        pred = ['Not Churn', 'Churn']
        col1, col2, col3, col4 = st.columns(4)
        col1.metric('Prediksi', pred[prediction[0]])
        col2.metric('Probabilitas', round(model.predict_proba(df)[0][1], 2))
        col3.metric('precision', "0.60")
        col4.metric("Recall", "0.68")
        # use 1 row of data here. Could use multiple rows if desired
        st.markdown(
            '<h4 style = "color:  #ff4b4b">Model Explaination</h4>', unsafe_allow_html=True)
        st.write("dengan menggunakan library SHAP, kita bisa melihat mengapa model ini memprediksi customer akan churna atau sebaliknya. Kita bisa melihat variabel variabel mana saja yang berpengaruh besar terhadap prediksi yang dibuat oleh model")
        st.write('warna merah menandakan bahwa variabel tersebut mempengaruhi model untuk memprediksi customer akan churn, dan sebaliknya untuk yang berwarna biru')
        #data_for_prediction_array = data_for_prediction.values.reshape(1, -1)
        with st.spinner("Processing..."):
            data_for_prediction = proc.transform(df)
            shap_values = explainer_sh(data_for_prediction)
            shap_values[0].data[0] = df.MonthlyCharges
            shap_values[0].data[1] = df.TotalCharges
            st.set_option('deprecation.showPyplotGlobalUse', False)
            a = shap.plots.waterfall(shap_values[0][:, 1])
            # set width
            st.pyplot(a)
