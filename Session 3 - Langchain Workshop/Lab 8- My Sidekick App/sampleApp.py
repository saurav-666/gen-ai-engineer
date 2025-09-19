#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,
# pip install faiss-cpu
# streamlit run sampleApp.py


import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
import sys
sys.path.insert(1, '../../')
import init_creds as creds
import os
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def initialize():
   
    AZURE_OPENAI_API_KEY = creds.get_api_key()
    AZURE_OPENAI_ENDPOINT = creds.get_endpoint()
    # print(AZURE_OPENAI_API_KEY)
    # print(AZURE_OPENAI_ENDPOINT)
    
    if not AZURE_OPENAI_API_KEY:
        raise ValueError("No AZURE_OPENAI_API_KEY set for Azure OpenAI API")
    if not AZURE_OPENAI_ENDPOINT:
        raise ValueError("No AZURE_OPENAI_ENDPOINT set for Azure OpenAI API")


    os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
    os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = "gpt-4o-mini"
    os.environ["AZURE_OPENAI_API_VERSION"]="2024-07-01-preview"




    model = AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )
    loader=PyPDFLoader("../materials/NoushathDPNProfile.pdf")
    data=loader.load() 
  

    text_splitter = CharacterTextSplitter(chunk_size=200,
                                        chunk_overlap=20,
                                        length_function=len,
                                        separator=".")
    final_data= text_splitter.split_documents(data)
    
 
    embeddings = AzureOpenAIEmbeddings(
        model="text-embedding-3-large",
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )

    faissdb=FAISS.from_documents(final_data,embeddings)
    from langchain.chains import RetrievalQA
    ragChain=RetrievalQA.from_llm(llm=model,retriever=faissdb.as_retriever(search_kwargs={"k":1}), return_source_documents=True)
    return{"llm":model,"faissdb":faissdb,"chain":ragChain}

#Function to return the response
def load_answer(question,onlyLLM):
    initializeObj=initialize()
    if onlyLLM:
        return initializeObj["llm"].invoke(question).content

        
    else:
        output=initializeObj["chain"].invoke(input=question)
        return {"response":output["result"],"citations":output["source_documents"]}



#App UI starts here
st.set_page_config(page_title="My Sidekick", page_icon=":robot:")
st.header("My Sidekick")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
onlyLLM = st.checkbox('Query on pure LLM')
submit = st.button('Generate')  


#If generate button is clicked
if submit:
    response = load_answer(user_input,onlyLLM)
    st.subheader("Answer:")
    st.write(response)