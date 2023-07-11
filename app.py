import streamlit as st
from langchain.llms import OpenAI

from clarifai_utils.modules.css import ClarifaiStreamlitCSS

st.set_page_config(layout="wide")

ClarifaiStreamlitCSS.insert_default_css(st)

# st.markdown("Please select a specific page from the sidebar to the left")

st.title("Simple App to get started with Langchain")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")


def generate(input_text):
    llm = OpenAI(temperature=0.8, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "Suggest a Roadmap to learn Machine Learning?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate(text)
