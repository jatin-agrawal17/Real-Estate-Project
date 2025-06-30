import streamlit as st
import pickle
import pandas as pd
import numpy as np
import cloudpickle
import sklearn.compose._column_transformer as ct
import zipfile
import os
import cloudpickle

# Patch for _RemainderColsList error
if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    setattr(ct, "_RemainderColsList", _RemainderColsList)

st.set_page_config(page_title = 'Viz Demo')

with open('df.pkl' , 'rb') as file:
    df = pickle.load(file)



# Unzip and load pipeline.pkl from pipeline.zip
if not os.path.exists("pipeline.pkl"):
    with zipfile.ZipFile("pipeline.zip", "r") as zip_ref:
        zip_ref.extract("pipeline.pkl")

with open('pipeline.pkl', 'rb') as file:
    pipeline = cloudpickle.load(file)


# st.dataframe(df)

st.header("Enter your Inputs")
# property_type
property_type = st.selectbox('Property Type', ['flat' , 'house'])

# sector
sector = st.selectbox('Sector' , sorted(df['sector'].unique().tolist()))

# bedroom
bedroom = float(st.selectbox('Number of Bedroom' , sorted(df['bedRoom'].unique().tolist())))

#bathroom
bathroom = float(st.selectbox('Number of Bathroom' , sorted(df['bathroom'].unique().tolist())))

#balcony
balcony = st.selectbox('Balconies' , sorted(df['balcony'].unique().tolist()))

# agePoseesion
agePosession = st.selectbox('Property Age' , sorted(df['agePossession'].unique().tolist()))

# built_up area
built_up_area = float(st.number_input("Built Up Area"))

#serventRoom
servent_room = float(st.selectbox('Servent Room' , [0.0,1.0]))

# store room
store_room = float(st.selectbox('Store Room' , [0.0,1.0]))

# furnishing_type
furnishing_type = st.selectbox('Furnishing Type' , sorted(df['furnishing_type'].unique().tolist()))

# luxury_category
luxury_category = st.selectbox('Luxury Category' , sorted(df['luxury_category'].unique().tolist()))

# floor_category
floor_category = st.selectbox('floor Category' , sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type, sector, bedroom, bathroom, balcony, agePosession, built_up_area, servent_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The Price of Flat is between {} Cr and {} Cr".format(round(low,2) , round(high,2)))



