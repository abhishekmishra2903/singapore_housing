#importing necessary libraries

import streamlit as st
import datetime
import pickle

# loading the pickle regressor model
with open('C:\\Users\\Admin\\Documents\\Singapore_house\\regressor','rb') as f:
    model_regressor=pickle.load(f)

# loading the pickle file for flat_list    
with open('C:\\Users\\Admin\\Documents\\Singapore_house\\flat_type_list','rb') as f:
    flat_type_list=pickle.load(f)

# loading the pickle file for flat_model
with open('C:\\Users\\Admin\\Documents\\Singapore_house\\flat_model_list','rb') as f:
    flat_model_list=pickle.load(f)

# loading the pickle file for street name
with open('C:\\Users\\Admin\\Documents\\Singapore_house\\street_name_list','rb') as f:
    street_name_list=pickle.load(f)

# loading the pickle file for schema of dataframe of independent variables  
with open('C:\\Users\\Admin\\Documents\\Singapore_house\\df_schema','rb') as f:
    df_schema=pickle.load(f)

# streamlit header
st.header('	:house_buildings: Singapore Housing Price Prediction')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

# Arranging widgets into 4 columns
col11, col12, col13, col14 = st.columns(4)

# defining min and max date for date input widget
min_date = datetime.datetime(2020,1,1)
max_date = datetime.date(2025,12,31)

# placing date input widget and extracting month and year from it
with col11:    
    a_date = st.date_input("Pick a date", min_value=min_date, max_value=max_date)
    
month=a_date.month
year=a_date.year  

# placing flat_type widget
with col12:
    flat_type = st.selectbox('Type of flat',flat_type_list)
 
# placing flat_model widget
with col13:
    flat_model = st.selectbox('Flat model', flat_model_list)

#placing street_name widget
with col14:
    street_name = st.selectbox('Street name',street_name_list)
    
# defining 3 columns to arrange widgets
col21,col22,col23=st.columns(3)

# placing lease_year in tons
with col21:
    lease_year=st.number_input('Year of lease', min_value=1900, max_value=2023)

#placing floor area widget    
with col22:
    floor_area=st.number_input('Floor area in square metres',min_value=20, max_value=500)
 
#placing storey widget
with col23:
    storey=st.number_input('Storey of building',min_value=1, max_value=200)

switch=st.button('submit')

if switch==True:
    
# loading the input in empty dataframe of independent variables
    df_schema['month']=int(month)
    df_schema['year']=int(year)
    df_schema['storey_range']=int(storey)
    df_schema['floor_area_sqm']=int(floor_area)
    df_schema['lease_commence_date']=int(lease_year)
    df_schema[flat_type]=True
    df_schema[flat_model]=True
    df_schema[street_name]=True

# predicting and printing price    
    y_pred=model_regressor.predict(df_schema)
    st.subheader(f'The predicted price is {round(y_pred[0],2)} dollars')
