
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

st.title("Air Quality Monitoring & AQI Predictor")
st.markdown("📊 This app visualizes AQI levels and predicts AQI based on pollutant data.")

file = st.file_uploader("📁 Upload your AQI CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("🔍 Preview of Uploaded Data")
    st.write(df.head())

    # Train the model
    X = df[['PM2.5', 'PM10', 'NO2', 'SO2']]
    y = df['AQI']
    model = LinearRegression()
    model.fit(X, y)

    # 📈 AQI Over Time Line Graph
    if 'Date' in df.columns:
        st.subheader("📈 AQI Over Time")
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['AQI'], marker='o', color='green')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 📊 PM2.5 vs PM10 Bar Chart
    st.subheader("📊 PM2.5 vs PM10 Bar Chart")
    x = np.arange(len(df))
    fig2, ax2 = plt.subplots()
    ax2.bar(x - 0.2, df['PM2.5'], width=0.4, label='PM2.5', color='skyblue')
    ax2.bar(x + 0.2, df['PM10'], width=0.4, label='PM10', color='orange')
    ax2.axhline(y=60, color='blue', linestyle='--', label='PM2.5 Safe Limit')
    ax2.axhline(y=100, color='red', linestyle='--', label='PM10 Safe Limit')
    ax2.set_xticks(x)
    ax2.set_xticklabels(df['Date'], rotation=45)
    ax2.set_ylabel("µg/m³")
    ax2.set_title("PM2.5 vs PM10 Levels with Safe Limits")
    ax2.legend()
    st.pyplot(fig2)

    # 🧮 AQI Prediction Inputs
    st.subheader("🧮 Predict AQI from Pollutants")
    pm25 = st.number_input("PM2.5", 0.0, 500.0, 80.0)
    pm10 = st.number_input("PM10", 0.0, 500.0, 120.0)
    no2 = st.number_input("NO2", 0.0, 200.0, 25.0)
    so2 = st.number_input("SO2", 0.0, 200.0, 7.0)

    if st.button("Predict AQI"):
        pred = model.predict([[pm25, pm10, no2, so2]])
        st.success(f"🌬️ Predicted AQI: {round(pred[0], 2)}")
