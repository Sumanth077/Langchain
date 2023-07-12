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

st.title("🦜 Simple Application to get started with Langchain")

st.sidebar.markdown("Made with UI Modules, a streamlit integration from [Clarifai](https://clarifai.com/) that helps you create and deploy beautiful AI web apps.")
st.sidebar.image(
    "https://rasahq.github.io/rasa-nlu-examples/square-logo.svg", width=100
)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")


def generate(text):
    llm = OpenAI(temperature=0.8, openai_api_key=openai_api_key)
    st.info(llm(text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are the potential risks and concerns surrounding AI development?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate(text)

