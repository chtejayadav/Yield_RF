import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, label, span {{
        color: white !important; /* Force white text */
    }}
    .stSelectbox div[data-testid="stMarkdownContainer"] * {{
        color: white !important; /* Keep dropdown values black !important*/
    }}
    /* Remove sidebar background */
    section[data-testid="stSidebar"] {{
        background-color: transparent !important;
        color: white !important;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set background image
image_path = "harvest-280.gif"  # Ensure the image exists in the same directory
set_background(image_path)

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
         # Display prediction result
    st.markdown(
    f'<p style="color:white; background-color:#28a745; padding:10px; border-radius:5px; font-size:16px; font-weight:bold;">🏥 Predicted Crop Yield: {prediction:.2f} hg/ha</p>', 
    unsafe_allow_html=True
)
    
if __name__ == "__main__":
    main()
