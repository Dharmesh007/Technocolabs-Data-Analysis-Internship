# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:04:33 2021

@author: C Dharmesh Waran
"""

import streamlit as st
import pandas as pd
import shap
import pickle
import matplotlib.pyplot as plt
from PIL import Image

'''Welcome to this page'''

model = pickle.load(open(r'C:\Internship\Technocolabs\Dataset\NSRDB\SolarPred\xgb1.pkl','rb'))


st.write("""
# Solar Prediction App
This app predicts the **Solar Radiation Prediction**!
""")
st.write('---')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')


def user_input_features():
    Year = st.selectbox('Year',('2018','2019','2020','2021')) 
    Month = st.selectbox('Month',('1','2','3','4','5','6','7','8','9','10','11','12')) 
    Day = st.selectbox('Day',('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'))
    Hour = st.selectbox('Hour',('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'))
    Minute = st.selectbox('Minute',('0','30'))
    Cloud_Type = st.selectbox('Cloud Type',('0','1','2','3','4','5','6','7','8','9'))
    Dew_Point = st.number_input('Dew Point')
    Fill_Flag = st.selectbox('Fill Flag',('0','1','3','5'))
    Surface_Albedo = st.number_input("Surface Albedo")
    Wind_Speed = st.number_input("Wind Speed")
    Precipitable_Water = st.number_input("Precipitable Water")
    Wind_Direction = st.number_input("Wind Direction")
    Relative_Humidity = st.number_input("Relative Humidity") 
    Temperature = st.number_input("Temperature")  
    Pressure = st.number_input('Pressure (925-960)')
    data = {'Year': Year,
            'Month': Month,
            'Day': Day,
            'Hour': Hour,
            'Minute': Minute,
            'Cloud_Type': Cloud_Type,
            'Dew Point': Dew_Point,
            'Fill Flag': Fill_Flag,
            'Surface Albedo': Surface_Albedo,
            'Wind Speed': Wind_Speed,
            'Precipitable Water': Precipitable_Water,
            'Wind Direction': Wind_Direction,
            'Relative Humidity': Relative_Humidity,
            'Temperature': Temperature,
            'Pressure': Pressure
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

if st.button("Predict"):
    output = model.predict(df)
    output = int(output)
    st.success('The output is {}'.format(output))
    st.header('Prediction of Solar radiation')
    st.write(model)
    st.write('---')



