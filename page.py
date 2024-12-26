import streamlit as st
pages = {

    "VISUALIZAÇÃO DE DADOS": [st.Page("STREAM_GRAFICOS.py", title="Pag 1"),
                    st.Page("page2.py",   title="Pag 2")]
        }
pg = st.navigation(pages)
pg.run()