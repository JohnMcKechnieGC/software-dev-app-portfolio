import streamlit as st

st.set_page_config(page_title="Apprentice Portfolio", page_icon="📚")

st.title("Welcome to Your Software Developer Apprentice Portfolio")
st.write("""
This web app is intended to help you record evidence against Knowledge, Skills, 
and Behaviours (KSBs) required for your apprenticeship portfolio.
Use the sidebar to navigate between pages.
""")
st.write("""
The app is an early prototype demonstrating some different ideas on how to record
evidence. Check out the individual pages for Knowledge, Skills, and Behaviours to
see the alternative designs.
""")

st.write("**Start by selecting a category from the sidebar:** Knowledge, Skills, or Behaviours.")
