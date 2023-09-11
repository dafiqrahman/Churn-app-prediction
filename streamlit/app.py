import streamlit as st
import os
# Custom imports

# st.set_page_config(layout="wide")
# Create an instance of the app

# Title of the main page
st.markdown("<h1 style='text-align: center;'>Churn Prediction Application</h1>",
            unsafe_allow_html=True)

st.markdown("<h2 style = 'color : #ff4b4b'>  Latar Belakang</h2>",
            unsafe_allow_html=True)
st.write("Keberadaan pelanggan bagi sebuah perusahaan sangat vital. Pelanggan adalah konsumen yang akan menggunakan jasa atau produk yang ditawarkan dan dijual. Setelah mendapatkan pelanggan sesuai yang diharapkan, ada masalah lain yang harus dihadapi, yakni apakah pelanggan tersebut loyal atau memilih Churn.")

st.markdown("<p><span style = 'color : #ff4b4b;font-weight : 700'>Customer Churn didefinisikan sebagai kecenderungan pelanggan untuk berhenti melakukan bisnis dengan sebuah perusahaan.</span> Hal ini telah menjadi isu penting yang merupakan salah satu tantangan utama oleh banyak perusahaan di era global ini.mendapatkan pelanggan baru jauh lebih sulit dibandingkan dengan mempertahankan pelanggan lama, serta biaya yang dikeluarkan perusahaan lima kali lipat lebih banyak dibandingkan dengan memuaskan dan mempertahankan pelanggan lama.</p>", unsafe_allow_html=True)

st.write(" Oleh karena itu perlu dilakukan prediksi untuk mengetahui kecenderungan apakah customer akan churn atau tidak. Hal ini dapat bermanfaat bagi perusahaan dalam menentukan kebijakan apa yang akan diambil, seperti langkah promosi yang efektif.")

st.markdown("<h2 style = 'color : #ff4b4b'>Data yang digunakan</h2>",
            unsafe_allow_html=True)
st.write(' Dataset yang digunakan untuk kasus ini adalah dataset yang didapatkan dari situs kaggle. Data ini berisi mengenai informasi pelanggan dari perusahaan telekomunikasi seperti demografi dari customer, layanan yang digunakan oleh customer, serta informasi pembayaran dari customer.')
st.write('perlu diketahui bahwa dataset ini bukan merupakan data real dari perusahaan, melainkan data sample yang dibuat oleh IBM, hal ini dikarenakan sulit untuk mencari data real dari suatu perusahaan. Meskipun demikian, kita bisa mendapat gambaran bagaimana cara membuat model untuk memprediksi churn.')
