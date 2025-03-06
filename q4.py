import streamlit as st
import google.generativeai as genai
model=genai.GenerativeModel("gemini-1.5-flash")
st.title("code debugging helper")
code=st.text_area("enter your code")
click=st.button("search")
if click:
   genai.configure(api_key="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ") 
   model=genai.GenerativeModel("gemini-1.5-flash")
response=model.generate_content(f"identify and suggest fixes for errors of code{code} and show the corrected code")
st.write(response.text)