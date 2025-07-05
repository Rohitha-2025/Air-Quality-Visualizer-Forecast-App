import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Air Quality Monitoring & AQI Predictor")
st.markdown("📊 This app visualizes AQI levels and predicts Air Quality Index based on pollutant data.")

file = st.file_uploader("📁 Upload your AQI CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("🔍 Preview of Uploaded Data")
    st.write(df.head())

    X = df[['PM2.5', 'PM10', 'NO2', 'SO2']]
    y = df['AQI']
    model = LinearRegression()
    model.fit(X, y)

    if 'Date' in df.columns:
        st.subheader("📈 AQI Over Time")
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['AQI'], marker='o', color='green')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    st.subheader("🧮 Predict AQI from Pollutant Levels")
    pm25 = st.number_input("PM2.5", 0.0, 500.0, 80.0)
    pm10 = st.number_input("PM10", 0.0, 500.0, 120.0)
    no2 = st.number_input("NO2", 0.0, 200.0, 25.0)
    so2 = st.number_input("SO2", 0.0, 200.0, 7.0)

    if st.button("Predict AQI"):
        pred = model.predict([[pm25, pm10, no2, so2]])
        st.success(f"🌬️ Predicted AQI: {round(pred[0], 2)}")


