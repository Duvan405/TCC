import streamlit as st
#holaaaaaaaaaa
pages = {

    "VISUALIZAÇÃO DE DADOS": [st.Page("page3.py",title = "Pag 2") , st.Page("page2.py",   title="Pag 1")] }
pg = st.navigation(pages)
pg.run()