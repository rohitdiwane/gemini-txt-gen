import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("api_key")
genai.configure(api_key=os.getenv("api_key"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="QA Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")

submit=st.button("Generate the Answere")

if submit:
    
    response=get_gemini_response(input)
    st.subheader("Here is the  generated text:")
    st.write(response)

