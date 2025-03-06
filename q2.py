print("hello")

import streamlit as st
import google.generativeai as genai
model=genai.GenerativeModel("gemini-1.5-flash")
def app():
 st.title("sentimant analysis of user input")
text=st.text_input("enter your text")
click=st.button("analyse")
if click:
   genai.configure(api_key="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ") 
   model=genai.GenerativeModel("gemini-1.5-flash")
response=model.generate_content(f"analyse sentiment of user input{text}")
st.write(response.text)