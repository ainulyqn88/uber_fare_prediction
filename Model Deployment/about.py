import streamlit as st
import streamlit.components.v1 as stc

# This page gives detail about the dataset 
# and the group involved in the process

about = """
        This app is created as Final Project of Hijau Daun in Digital Skola Batch 35.
        This app will give you a fare estimation
        for uber rides based in NYC area. 
        Simply insert your desired destination, time, and passenger count.
        The fare prediction process involves analyzing historical 
        data from previous trips to identify patterns and trends. 
        The prediction model was trained and tuned to give the most 
        accurate and reliable fare results.

        Dataset used is provided by [Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset/data).
        """

creator ="""
            ### About Us
            The creators:
            1. Arya Hendro Yudo
            2. Kharisma Kusuma Dewi
            3. Muhammad Ainul Yaqin
            4. Novandy
            5. Nyai Mukholisah
            6. Praditya
            """
def about_app():
    st.subheader("About the App")
    st.write(about)
    st.markdown(creator,unsafe_allow_html=True)