import streamlit as st
import numpy as np
from geopy.distance import geodesic as GD
import datetime

import joblib
import os

import folium
from streamlit_folium import st_folium

@st.cache_data
def load_ml_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model
def load_scaler(scaler_file):
    scaler = joblib.load(open(scaler_file, 'rb'))
    return scaler
def fare_app():
    st.subheader("Where to today?")
    st.write("Click on the map to choose your origin and destined location. Click the marker again to copy the coordinates and paste it below. Double click on the marker to delete it.")
    chosen = []

    ## Map
    m = folium.Map(
                 location=[40.7116, -73.9943],
                 zoom_start=13,
                 position='center'
                 )
    m.add_child(folium.ClickForMarker("<b>Current Location</b><br/> <b>Lat:</b> ${lat}<br /><b>Lng:</b> ${lng}"))
    
    col1, col2 = st.columns([2,1])
    with col1:
        st_data = st_folium(m,width = 600,height=400)
    with col2:
        lat1 = st.text_input("Paste the current latitude: ")
        lng1 = st.text_input("Paste the current longitude: ")
        lat2 = st.text_input("Paste the destination latitude: ")
        lng2 = st.text_input("Paste the destination longitude: ")
        distance = round(GD((lat1, lng1),(lat2, lng2)).km, 3)
        text_dist = str(distance)
        if lat1 and lng1 and lat2 and lng2 is not None:
            st.write("The total distance is: ",text_dist," km")
            chosen.append(distance)

    #calendar - col 1
    col1,col2 = st.columns([2,1])
    with col1:
        date_input = st.date_input("When will you be going?", min_value=datetime.date(2008,1,1), value=None)
        if date_input:
            year, month, weekday = date_input.year, date_input.month, date_input.weekday()
            chosen.append(year)
            chosen.append(month)
            chosen.append(weekday)
            
    #hour - col 2
    with col2:
        hour_input = st.time_input("What time will you be going?",value=None,step=60)
        if hour_input:
            hour = hour_input.hour
            chosen.append(hour)
    
    #passenger count
    passenger = st.number_input("How many passengers? ",1,6)
    chosen.append(passenger)

    # Rearranging and prediction
    if len(chosen) == 6:
        chosen = [chosen[5], chosen[1], chosen[2], chosen[3], chosen[4], chosen[0]]
        # Reshape and scale the features
        features = np.array(chosen).reshape(1, -1)
        scaler = load_scaler('robust_scaler.pkl')
        scaled_f = scaler.transform(features)
        #prediction
        model = load_ml_model('knn_scaler.pkl')
        prediction = model.predict(scaled_f)
        prediction = round(prediction.item(),2)
        text_pred = str(prediction)
        st.subheader("The estimated fare is $"+text_pred)

    