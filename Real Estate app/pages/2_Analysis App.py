import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Streamlit page title
st.set_page_config(page_title="Ploting Demo")
st.title("Analytics")

# Determine the base path (back to project root from /pages/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct full file paths
csv_path = os.path.join(BASE_DIR, 'datasets', 'data_viz1.csv')
pkl_path = os.path.join(BASE_DIR, 'datasets', 'feature_text.pkl')

# Load the data
new_df = pd.read_csv(csv_path)
feature_text = pickle.load(open(pkl_path, 'rb'))

# Group data by sector for map visualization
group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()

# Map visualization
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map", width=1200, height=700, hover_name=group_df.index)
st.plotly_chart(fig, use_container_width=True)

# Wordcloud section
st.header('Features Wordcloud')
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

fig_wc, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig_wc)

# Area vs Price scatter plot
st.header("Area vs Price")
property_type = st.selectbox('Select Property Type', ['flat', 'house'])
filtered_df = new_df[new_df['Property_type'] == property_type]
fig2 = px.scatter(filtered_df, x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
fig2.update_layout(xaxis=dict(range=[0, 12000]))
st.plotly_chart(fig2, use_container_width=True)

# BHK Pie Chart
st.header('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')
selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig3 = px.pie(new_df, names='bedRoom')
else:
    fig3 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
st.plotly_chart(fig3, use_container_width=True)

# Side by Side BHK Price Comparison
st.header('Side by Side BHK price comparison')
fig4 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig4, use_container_width=True)

# Distplot by property type
st.header('Side by Side Distplot for property type')
fig5 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['Property_type'] == 'house']['price'], label='house')
sns.distplot(new_df[new_df['Property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig5)

# Feedback section
st.header("💬 Feedback or Suggestions")
feedback = st.text_area("Leave your comments here:")
if st.button("Submit"):
    st.success("Thanks for your feedback!")
