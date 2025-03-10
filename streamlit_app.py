import streamlit as st
from query_processing import process_user_query
import subprocess

# Run query_processor.py before starting the app
subprocess.run(['python', 'query_processor.py'])

st.title("Tap Bonds Multiagent")

user_query = st.text_input("Ask your question:")

if st.button("Submit") and user_query:
    response = process_user_query(user_query)
    
    # Directly print the full response without truncation
    st.write("### Response:")
    st.text(response)

st.info("Enter a query and click Submit to get a response from the chatbot!")
