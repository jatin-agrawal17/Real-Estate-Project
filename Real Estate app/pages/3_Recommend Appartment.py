import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Recommend Appartments")

# Determine base directory (go up one level from /pages/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, 'datasets')

# Load all pickle files with absolute path
location_df = pickle.load(open(os.path.join(DATASET_DIR, 'location_distance.pkl'), 'rb'))
cosine_sim1 = pickle.load(open(os.path.join(DATASET_DIR, 'cosine_sim1.pkl'), 'rb'))
cosine_sim2 = pickle.load(open(os.path.join(DATASET_DIR, 'cosine_sim2.pkl'), 'rb'))
cosine_sim3 = pickle.load(open(os.path.join(DATASET_DIR, 'cosine_sim3.pkl'), 'rb'))

# Recommender Function
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1.0 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    return recommendations_df

# UI: Search by Location and Radius
st.title('Select Location and Radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    for key, value in result_ser.items():
        st.text(f"{key} - {round(value / 1000)} kms")

# UI: Recommend Similar Properties
st.title('Recommend Appartments')
selected_appartment = st.selectbox('Select an appartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_appartment)
    st.dataframe(recommendation_df)
