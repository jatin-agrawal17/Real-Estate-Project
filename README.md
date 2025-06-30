
# 🏙️ Real Estate Price Predictor & Recommendation App

🏠 Real Estate Analytical App helps users estimate property prices for flats and houses of **Gurgaon** based on custom inputs like location, size, and amenities.   
📊 It features interactive analytics, including geo-based price visualizations and market trends.  
🧭 Users can also discover similar properties based on distance and recommendations from selected listings.

## 🚀 Live Demo

Click below to check it

https://real-estate-project-ksqcsjy4c7gj3xw7977a2m.streamlit.app/

## 🧠 How It Works

- Users can check the price of houses or flats by providing specific inputs such as sector, number of bedrooms, bathrooms, built-up area, and property type.

- An interactive geo map displays the **average price per square foot** for each sector, helping users compare locations visually.

- The app recommends properties that are geographically close to the selected one, allowing users to explore alternatives in nearby sectors based on distance.
## 🎯 Features

🏠 Smart price prediction for flats and houses using ML models

📍 Geo-map visualization of average price-per-sqft of sector-wise property  in Gurugram

📊 Interactive analytics including pie charts, scatter plots, and distribution graphs

💬 Feature word cloud to highlight common property amenities

🔎 Input-based filtering for BHK, area, furnishing type, and more

📌 Nearby property search using location and radius filters

🏢 Property recommendation system using cosine similarity and distance logic

⚠️ Input validation & error handling for better user experience

📋 Clean and responsive UI powered by Streamlit
## 🛠️ Technologies Used

| Technology       | Description |
|------------------|-------------|
| 🐍 **Python**     | Core programming language used for development. |
| 📊 **Pandas**     | For data manipulation and analysis. |
| 🔢 **NumPy**      | For numerical operations and array handling. |
| 📈 **Seaborn**    | For beautiful and informative statistical graphics. |
| 📉 **Matplotlib** | For plotting and visualizing static graphs. |
| 🌐 **Plotly**     | For creating interactive and responsive visualizations. |
| 🧵 **Streamlit**  | For building fast, interactive data apps. |
| 🧪 **Scikit-learn** | For building the recommendation engine and computing similarity. |
| 🧠 **Cosine Similarity** | Used to measure similarity between properties. |
| 🧊 **Pickle**     | For serializing and saving Python objects like models and data. |
| ☁️ **Cloudpickle** | Enhanced version of pickle used for saving complex functions and objects. |
| ☁️ **WordCloud**  | For generating word clouds to visualize features. |


## 📂 Project Structure


📦 Real-Estate-Project/  
├── Raw Datasets/ # Original datasets used in the project    
├── Data Cleaning/ # Scripts to clean and preprocess data   
├── Feature Engineering/ # Scripts for creating new features      
├── EDA/ # Exploratory Data Analysis notebooks  
├── Outlier Detection/ # Logic for detecting and handling outliers    
├── Missing Value Imputation/ # Techniques to handle missing data   
├── Feature Selection/ # Methods to reduce feature space    
├── Baseline Model/ # Basic baseline modeling for comparison    
├── Model Selection/ # Model comparison and evaluation    
├── Analytical module/ # Contains custom analysis logic    
├── Recommendation Module/ # Property recommendation system files  
├── Real Estate app/ # Streamlit files for real estate dashboard  
├──  requirements.txt # Python dependencies   
└──  README.md 
## 🖥️ Running Locally

### 🔧 Prerequisites
- Make sure you have **Python 3.x** and **pip** installed on your system.
- Recommended to use a **virtual environment** (optional).

---

### ⬇️ Step-by-step Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/jatin-agrawal17/Real-Estate-Project.git  
cd Real-Estate-Project
```
#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the App
```bash
streamlit run Home.py 
```


## 💡 Deployment Notes

Since pipeline.pkl is larger than GitHub’s file limit (100 MB), it is compressed into a .zip file. Ensure it’s unzipped before running locally or deploying to Streamlit Cloud.


## 📊 Dataset Used

[Raw Dataset](https://github.com/jatin-agrawal17/Real-Estate-Project/tree/main/Raw%20Datasets)
## 📌 Limitations

The app uses a preloaded dataset and does not fetch live or real-time property listings or prices.

The analysis is focused on a specific city which is **Gurgaon** and may not be applicable to other locations without modification.
## 🙌 Acknowledgements
Gained Knowledge about ML Algorithms

Inspired by content-based & collaborative filtering concepts

Special thanks to Streamlit for rapid UI prototyping


## 👤 Author

Jatin Agrawal  
📬 [LinkedIn](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

## 📎 License

This project is open-source and available under the MIT License.


