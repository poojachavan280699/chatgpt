'''import streamlit as st
import openai
from streamlit_chat import message
import json
from random import randint

# Set up your OpenAI API key
openai.api_key = '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'

st.set_page_config(page_title="Document Analysis (Model: GPT-3.5-turbo)", page_icon=":robot:", layout="wide")
st.header("Chat with your Financial Documents- Annual Reports 📄")

# ...

# Initialize session_state keys if not present
if 'generated' not in st.session_state:
    st.session_state.generated = []
if 'past' not in st.session_state:
    st.session_state.past = []
if 'widget_key' not in st.session_state:
    st.session_state.widget_key = str(randint(1000, 100000000))

# Sidebar - the clear button will flush the memory of the conversation
st.sidebar.title("Sidebar")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

if clear_button:
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.widget_key = str(randint(1000, 100000000))
    # Clear the conversation memory here if applicable

# ...

# Define user_input and submit_button
user_input = st.text_input("User Input:")
submit_button = st.button("Submit")

# Dummy value for kendra_rag
kendra_rag = "This is a sample Kendra retrieval result."

# ...

# Chat history container
with st.container():
    if st.session_state.generated:
        for i in range(len(st.session_state.generated)):
            message(st.session_state.past[i], is_user=True, key=str(i) + '_user')
            message(st.session_state.generated[i], key=str(i))
'''
import os
import openai
import PyPDF2

openai.api_key = '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' 

folder_path = 'C:/Users/hande/OneDrive/Desktop/chatGptPooja/Bank Financial Statements/'  

file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_question = input("You: ")
    
    if user_question.lower() == 'exit':
        print("Assistant: Goodbye!")
        break

    found = False
    
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if file_name.lower().endswith('.pdf'):
            pdf_text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text()
            
            
            
            if user_question in pdf_text:
                assistant_reply = "Answer from PDF file " + file_name + ": " + pdf_text
                found = True
                print("assistant_reply", assistant_reply)
                break
    
    if not found:
        conversation.append({"role": "user", "content": user_question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        print("OpenAI Response:", response)  # Debugging line
        
        assistant_reply = response['choices'][0]['message']['content']

    print("Assistant:", assistant_reply)
