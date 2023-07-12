import streamlit as st
from langchain.llms import OpenAI

from clarifai.auth.helper import ClarifaiAuthHelper
from clarifai.client import create_stub
from clarifai_utils.modules.css import ClarifaiStreamlitCSS
from clarifai.listing.lister import ClarifaiResourceLister
from clarifai.modules.css import ClarifaiStreamlitCSS
from google.protobuf import json_format, timestamp_pb2

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

# This must be within the display() function.
auth = ClarifaiAuthHelper.from_streamlit(st)
stub = create_stub(auth)
userDataObject = auth.get_user_app_id_proto()
lister = ClarifaiResourceLister(stub, auth.user_id, auth.app_id, page_size=16)

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

