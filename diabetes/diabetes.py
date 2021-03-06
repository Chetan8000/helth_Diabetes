import joblib
import numpy as np
from diabetes import constant
import pickle
import streamlit as st
import time
import webbrowser

PKLPath = 'diabetes/diabetes_model.pkl'


def ValuePredictor(to_predict, size):
    '''	No. of Pregnencies
        Glucose Level
        Current Blood Pressure
        Enter the Body Mass Index
        Diabetes Pedigree Function
        Age
    '''
    if (size == 6):
        loaded_model = joblib.load(PKLPath)
        result = loaded_model.predict(to_predict)
    return result[0]


def main():
    #st.title("Know Your Chances Of Getting Diabetes In One Click!")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Know Your Chances Of Getting Diabetes In One Click </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    page_bg_img = '''
      <style>
 	body {
	background-image: url("https://user-images.githubusercontent.com/53088237/103136113-88b4c180-46e3-11eb-8780-4ae10bdbe304.jpeg");
	background-size: cover;
	}
	</style>
	'''

    # st.markdown(page_bg_img, unsafe_allow_html=True)

    status = st.radio('Select Gender', ('Male', 'Female'))
    if status == 'Female':
        no_pregnencies = st.number_input("No.of Pregnencies", value=0)
    else:
        no_pregnencies = 0

    # no_pregnencies = st.text_input("No. of Pregnencies", "")
    glucose_level = st.number_input("Glucose Level")
    current_bp = st.number_input("Current Blood Pressure")
    bmi = st.number_input("Enter the Body Mass Index")
    dpf = st.number_input("Diabetes Pedigree Function")
    age = st.number_input("Age")
    to_predict_list = [no_pregnencies, glucose_level, current_bp, bmi, dpf, age]
    size = len(to_predict_list)
    result = ""
    prediction = ""
    if st.button("Predict"):
        to_predict = np.array(to_predict_list).reshape(1, size)
        result = ValuePredictor(to_predict, size)
        if int(result) == 1:
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"

    st.success(prediction)
    if st.button("About Diabetes"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Diabetes")

    info_about = '''
    <div id="footer" class="text-center center-block">
          <p>© 2020 Author: Chetan Borse</p>
    </div>
    '''
    st.markdown(info_about, unsafe_allow_html=True)

    html = f"""<div
    <ul class="mylinks">
	<a href='https://github.com/Chetan8000/'><img src='data:image/png;base64,{constant.Github}'></a>
        <a href='https://www.linkedin.com/in/borsechetan800/'><img src='data:image/png;base64,{constant.LinkedIN}'></a>
    </ul>    </div>"""
    st.markdown(html, unsafe_allow_html=True)

