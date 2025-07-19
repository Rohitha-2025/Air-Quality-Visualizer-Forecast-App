# 🌍 Air Quality Visualizer & Forecast App

---

## 🚀 Project Overview

Developed a lightweight application providing real-time Air Quality Index (AQI), pollutant levels (PM2.5, PM10), and next-day forecasts for **underserved regions**. This project aims to empower users with critical environmental health information to make informed decisions.

---

## ✨ Features

* **Real-time AQI & Pollutant Levels:** Displays current Air Quality Index and levels of key pollutants like PM2.5 and PM10.
* **Next-Day Forecasts:** Provides predictive air quality information for the upcoming day using machine learning.
* **Localized Data:** Focuses on providing relevant data for small cities and rural areas.
* **User-Friendly Interface:** Designed for ease of use and accessibility.

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask / Streamlit - *choose one you're using*)
* **Data Sources:** Open AQ, data.gov.in
* **Machine Learning Models:** Linear Regression, Decision Trees

---

## ⚙️ Installation & Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt` after installing your backend libraries like Flask/Streamlit, requests, pandas, scikit-learn, etc.)*
4.  **Run the application:**
    * **If using Flask:**
        ```bash
        export FLASK_APP=app.py # Or your main Flask file
        flask run
        ```
    * **If using Streamlit:**
        ```bash
        streamlit run app.py # Or your main Streamlit file
        ```
5.  **Access the app:** Open your web browser and go to `http://127.0.0.1:5000` (for Flask) or the address provided by Streamlit.

---
