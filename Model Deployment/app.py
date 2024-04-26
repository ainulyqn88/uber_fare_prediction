import streamlit as st
import streamlit.components.v1 as stc
from streamlit_option_menu import option_menu

from about import about_app
from fare_app import fare_app

heading = """
            <div style="padding: 20px; border-radius: 10px;background-color:#ADB5BD">
            <h1 style="color:white ;font-family:sans-serif;margin:0"> Uber Fare Estimate (NYC Area) </h1>
            """

def main():
    # Sidebar with option_menu
    stc.html(heading)
    with st.sidebar:
        choice = option_menu('Hijau Daun', ['Fare Prediction','About'], 
        icons = ['car-front-fill','info-circle-fill'],
        default_index = 0,
        menu_icon='house',
        styles={
            "nav-link": {"--hover-color": "#ADB5BD"},
            "nav-link-selected": {"background-color": "#b3e4a8"}
            }
        )
        st.markdown("---")
        # Create a horizontal layout
        col1, col2 = st.columns(2, gap="small")
    
        # Place the images in the columns
        col1.image("Group Logo.png", width=70)
        col2.image("DigitalSkola.png", width=100)
    if choice == "Fare Prediction":
        fare_app()
    elif choice == "About":
        about_app()
if __name__ == '__main__':
    main()

