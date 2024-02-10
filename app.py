# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os 

load_dotenv()

# Function to load OpenAI model and get reponse

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response=llm(question)
    return response

# Initialize Stremlit app (for front-end)

st.set_page_config(page_title="Q&A Chatbot")
st.header("Langchain Application by Anish Mahapatra")

input = st.text_input("Input: ", key=input)
response = get_openai_response(input)

submit=st.button("Ask!")

# If the "Ask!"" button is clicked, then run the following
if submit:
    st.subheader("The response is")
    st.write(response)



