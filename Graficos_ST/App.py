import streamlit as st

pg = st.navigation([st.Page("Page1.py")])
st.set_page_config(layout='wide',page_title='TCC')
pg.run() 
