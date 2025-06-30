import streamlit as st
import pandas as pd
import plotly.express as px
import  pickle
from wordcloud import  WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title = "Ploting Demo")

st.title("Analytics")

new_df = pd.read_csv('datasets/data_viz1.csv')
# st.dataframe(new_df)
feature_text = pickle.load(open('datasets/feature_text.pkl' , 'rb'))
group_df = new_df.groupby('sector')[['price' , 'price_per_sqft' , 'built_up_area', 'latitude', 'longitude']].mean()
# st.dataframe(group_df)

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map", width=1200 , height=700 , hover_name=group_df.index)
st.plotly_chart(fig , use_container_width=True)

st.header('Features Wordcloud')

# Generate word cloud
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)

# Display in Streamlit using the figure
st.pyplot(fig)

st.header("Area vs Price")

property_type = st.selectbox('Select Property Type' , ['flat' , 'house'])
if property_type == 'house':
    fig2 = px.scatter(new_df[new_df['Property_type']=='house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    fig2.update_layout(xaxis=dict(range=[0, 12000]))
    st.plotly_chart(fig2 , use_container_width=True)

else:
    fig2 = px.scatter(new_df[new_df['Property_type']=='flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    fig2.update_layout(xaxis=dict(range=[0, 12000]))
    st.plotly_chart(fig2 , use_container_width=True)


st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)


st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)

st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['Property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['Property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)

st.header("💬 Feedback or Suggestions")
feedback = st.text_area("Leave your comments here:")
if st.button("Submit"):
    st.success("Thanks for your feedback!")
