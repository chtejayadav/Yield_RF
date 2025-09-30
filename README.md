Yield Prediction Using Random Forest
Overview

This is a small project I worked on to understand how machine learning can be used in agriculture. The main idea is to predict crop yield based on given data, and I used the Random Forest algorithm for this. The project covers some data analysis, model building, and also a simple web app so the results can be tested easily.

Project Structure

Here’s what you’ll find inside this repo:

1. Yield Data Analysis.ipynb → Notebook where I did exploratory data analysis (EDA).

2. Yield Data ML.ipynb → Notebook for training the Random Forest model.

app.py → Streamlit-based web app that lets you try predictions.

harvest-280.gif → Just a fun visualization I added for presentation.

requirements.txt → List of Python packages needed.

yield_df.csv → Dataset used for training and testing.

Installation

Clone this repository:

git clone https://github.com/your-username/Yield_RF.git
cd Yield_RF-main


(Optional but recommended) set up a virtual environment:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Usage
Notebooks

Open Jupyter and run the two notebooks in order:

1. Yield Data Analysis.ipynb

2. Yield Data ML.ipynb

Web App

Run the app locally with:

python app.py


This will open a local server in your browser where you can input values and get yield predictions.

Dependencies

Everything you need is listed in requirements.txt. Just install it once and you’re good to go.

Contributing

If you find bugs or have ideas to improve this project, feel free to fork and open a pull request. I’d be happy to collaborate.

Author

👨‍💻 CH TEJA YADAV
📧 Email: tejayadavch@gmail.com

🌐 GitHub: chtejayadav

👉 Try the live app here: Yield Prediction App
