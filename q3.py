import streamlit as st
import google.generativeai as genai
model=genai.GenerativeModel("gemini-1.5-flash")
def app():
 st.title("AI based travel iterary generator")
place=st.text_input("enter your destination")
day=st.text_input("enter your duration")
click=st.button("search")
if click:
   genai.configure(api_key="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ") 
   model=genai.GenerativeModel("gemini-1.5-flash")
response=model.generate_content(f"give the information of place{place}with duration{day} and also give food recomendation and activties information")
st.write(response.text)