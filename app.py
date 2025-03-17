import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

def load_data():
    """Load and preprocess dataset."""
    df = pd.read_csv("yield_df.csv")
    df.drop(columns=["Sl.no"], inplace=True)
    
    # Encode categorical variables
    label_encoders = {}
    for col in ["Area", "Item"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    return df, label_encoders

def train_model(df):
    """Train the Random Forest model."""
    X = df.drop(columns=["hg/ha_yield"])
    y = df["hg/ha_yield"]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler

def main():
    st.title("Crop Yield Prediction App")
    
    df, label_encoders = load_data()
    model, scaler = train_model(df)
    
    # User inputs
    area = st.selectbox("Select Area", label_encoders["Area"].classes_)
    item = st.selectbox("Select Crop Item", label_encoders["Item"].classes_)
    year = st.number_input("Enter Year", min_value=1980, max_value=2030, step=1)
    rain_fall = st.number_input("Average Rainfall (mm/year)", min_value=0.0)
    pesticides = st.number_input("Pesticides Used (tonnes)", min_value=0.0)
    avg_temp = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
    
    if st.button("Predict Yield"):
        # Transform inputs
        input_data = np.array([
            label_encoders["Area"].transform([area])[0],
            label_encoders["Item"].transform([item])[0],
            year, rain_fall, pesticides, avg_temp
        ]).reshape(1, -1)
        
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        
        st.success(f"Predicted Crop Yield: {prediction:.2f} hg/ha")
    
if __name__ == "__main__":
    main()
