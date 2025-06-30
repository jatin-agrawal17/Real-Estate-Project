import streamlit as st
import pickle
import pandas as pd
import numpy as np
import cloudpickle
import sklearn.compose._column_transformer as ct
import zipfile
import os

# Patch for _RemainderColsList error (for compatibility with sklearn versions)
if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    setattr(ct, "_RemainderColsList", _RemainderColsList)

# Page config
st.set_page_config(page_title='Viz Demo')

# Compute base directory regardless of working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load df.pkl safely
df_path = os.path.join(BASE_DIR, 'df.pkl')
with open(df_path, 'rb') as file:
    df = pickle.load(file)

# Extract and load pipeline.pkl from pipeline.zip if needed
pipeline_zip_path = os.path.join(BASE_DIR, 'pipeline.zip')
pipeline_pkl_path = os.path.join(BASE_DIR, 'pipeline.pkl')

if not os.path.exists(pipeline_pkl_path):
    with zipfile.ZipFile(pipeline_zip_path, "r") as zip_ref:
        zip_ref.extract("pipeline.pkl", path=BASE_DIR)

with open(pipeline_pkl_path, 'rb') as file:
    pipeline = cloudpickle.load(file)

# Input UI
st.header("Enter your Inputs")

property_type = st.selectbox('Property Type', ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedroom = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathroom', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
agePosession = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input("Built Up Area"))
servent_room = float(st.selectbox('Servent Room', [0.0, 1.0]))
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('floor Category', sorted(df['floor_category'].unique().tolist()))

# Prediction button
if st.button('Predict'):
    data = [[
        property_type, sector, bedroom, bathroom, balcony, agePosession,
        built_up_area, servent_room, store_room, furnishing_type,
        luxury_category, floor_category
    ]]

    columns = [
        'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'servant room', 'store room',
        'furnishing_type', 'luxury_category', 'floor_category'
    ]

    one_df = pd.DataFrame(data, columns=columns)
    base_price = np.expm1(pipeline.predict(one_df))[0]

    # Range estimation with ±22 lakh
    low = base_price - 0.22
    high = base_price + 0.22

    st.success(f"The Price of Flat is between ₹{round(low, 2)} Cr and ₹{round(high, 2)} Cr")
