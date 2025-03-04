import streamlit as st
import google.generativeai as genai
api_Key ="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ"
model=genai.GenerativeModel("gemini-1.5-flash")
def app():
 st.title("AI-Powered Resume Gnerator")

name=st.text_input("Enter your name")
skills=st.text_input("Enter your skills")
experience=st.text_area("Enter your work experience")
education=st.text_area("Enter your education")
click=st.button("Generate Resume")
if click:
   genai.configure(api_key="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ") 
   model=genai.GenerativeModel("gemini-1.5-flash")
prompt= f"Generate a resume for {name} with skills in {skills}, experience in work {experience} and education in {education}"
responce=model.generate_content(prompt)
st.markdown(responce)



