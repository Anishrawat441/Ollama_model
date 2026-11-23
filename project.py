import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

prompt=ChatPromptTemplate.from_messages([('system :''You are an helpful AI assistant' ),
('human','question :{Question}')])

def generate_response(llm,temperature,query):
    model=Ollama(model=llm,temperature=temperature)
    parser=StrOutputParser()
    chain=prompt | model | parser
    result=chain.invoke({'Question':query})
    return result

st.title("Q And A Chatbot with Ollama")

query=st.text_input("What is your query")

st.sidebar.title("Settings")


temprature=st.sidebar.slider("Select Temperature :",min_value=0.0,max_value=2.0,value=0.8)
model_name=st.sidebar.selectbox("Model is :",['llama3.2:1b','gemma3','llama3.2','nomic-embed-text'])

response=generate_response(model_name,temprature,query)

if st.button("Answer"):
    if query:
      st.write(response)
    else:
       st.warning("Please Enter some Query")


