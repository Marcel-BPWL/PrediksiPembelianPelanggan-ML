import streamlit as st
import pandas as pd
import pickle
def app():
    option_basket = st.sidebar.selectbox(
     'Apakah pelanggan menambahkan item kedalam keranjang?',
    ('Yes', 'No'))
    option_promo = st.sidebar.selectbox(
     'Apakah pelanggan mengklik banner Promo?',
    ('Yes', 'No'))
    option_sign_in = st.sidebar.selectbox(
     'Apakah pelanggan melakukan Login?',
    ('Yes', 'No'))
    option_home = st.sidebar.selectbox(
     'Apakah pelanggan melihat halaman utama?',
    ('Yes', 'No'))
    option_repeat = st.sidebar.selectbox(
     'Apakah dia pelanggan tetap?',
     ('Yes', 'No'))
    if st.sidebar.button('Memprediksi Kemungkinan Pelanggan melakukan pembelian'):
        lookup_dict={"Yes":1,"No":0}
        dict = {'basket_add_detail':[lookup_dict[option_basket]],
            'promo_banner_click':[lookup_dict[option_promo]],
            'sign_in':[lookup_dict[option_sign_in]],
            "saw_homepage":[lookup_dict[option_home]],
            "returning_user":[lookup_dict[option_repeat]]
           }
        prediction_df = pd.DataFrame(dict)
        st.write("Detail pelanggan untuk prediksi keinginan melakukan pembelian")
        st.write(prediction_df)
        with open("propensity_model.pkl", 'rb') as pfile:  
            propensity_model_loaded=pickle.load(pfile)
        y_predicted=propensity_model_loaded.predict(prediction_df)
        if (y_predicted[0]==1):
            st.write("Pelanggan akan melakukan pemesanan dari situs web. Probabilitas pemesanan:")
            # st.write(y_predicted[0])
        else:
            st.write("Pelanggan tidak akan melakukan pemesanan dari situs web. Probabilitas pemesanan:")
            # st.write(y_predicted[0])
        st.write(propensity_model_loaded.predict_proba(prediction_df))
