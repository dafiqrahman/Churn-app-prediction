import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

def predict_df(df):
    st.markdown("<h4>Preview Data</h4>", unsafe_allow_html=True)
    st.dataframe(df.head())
    output = ['Not Churn', 'Churn']
    columns_df = ["prediction"] + list(df.columns)
    if st.button("Batch Prediction"):
        with st.spinner("Processing..."):
            st.markdown("<h4>Preview Hasil Prediksi</h4>",
                        unsafe_allow_html=True)
            pred = model.predict(df)
            df["prediction"] = pred
            df['prediction'] = df.prediction.apply(lambda x: output[x])
            # reindex
            df = df.reindex(columns=columns_df)
            st.dataframe(df.head())

            @st.cache
            def convert_df(x):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return x.to_csv().encode('utf-8')

            csv = convert_df(df)
            # get datetime
            now = datetime.today().strftime('%Y-%m-%d')

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=f'Churn report {now}.csv',
                mime='text/csv',
            )

with open('model/model_logreg.pkl', 'rb') as f:
    model = pickle.load(f)

st.markdown("<h2 style = 'color : #ff4b4b'>  Batch Customer Prediction</h2>",
            unsafe_allow_html=True)
st.write("page ini digunakan untuk memprediksi secara Batch apakah customer akan cenderung churn atau tidak.")
st.write("dengan menggunakan Batch prediction, kita bisa memprediksi customer lebih dari 1 secara bersamaan, dan kita juga bisa mendownload hasil prediksi tersebut.")

upload_file = st.file_uploader("Upload your csv file", type=["csv"])
use_example_file = st.checkbox(
    "use example file", value=False, help="Use in-built example file")

if use_example_file:
    upload_file = "data/example.csv"
    df = pd.read_csv(upload_file)
    predict_df(df)
else:
    if upload_file is not None:
        df = pd.read_csv(upload_file)
        predict_df(df)
