import streamlit as st
import llm_call
import prompt
import Caching_Pattern
query = st.text_input("Enter your query:")

prompt= prompt.call_prompt(query)
if query:
    try:
       answer = Caching_Pattern.cache_llm(prompt)
    except Exception as e:
        answer = f"Error:{str(e)}"
    st.write(answer)
