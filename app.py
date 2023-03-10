# Simple Multi-Page Web Application using Streamlit

import streamlit as st
import training
import predict

#Title of the Application
st.title("Prediksi Pembelian Pelanggan")


#Choice of page
page_choices={"Ketahui lebih banyak tentang dataset":training,
              "Memprediksi Kemungkinan Pelanggan melakukan Pembelian":predict}


#Create radio button for the page choice
page_selection = st.radio("Go to", list(page_choices.keys()))


#Choosing the page based on the user selection from radio button
page = page_choices[page_selection]


#Display the page
with st.spinner(f'Loading {page_selection} ...'):
    page.app()

