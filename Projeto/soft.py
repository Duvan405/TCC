
import streamlit as st
from data import creat_list
from PIL import Image

if 'NTU_F' and 'NTU_E' and 'NTU_N' not in st.session_state:
    creat_list()

pg = st.navigation([
    st.Page("FATOR.py", title="Correction Factor F"),
    st.Page("EPSILON.py", title="Effectivity ε"),
    st.Page("HERN.py", title="Entropy Generation")])
     

st.set_page_config(layout='wide')
lg = Image.open('LOGO_USP.jpg')
st.logo(lg)
with st.sidebar.expander("Proposed Arrangements"):
    mg1=Image.open('casos.jpg')
    st.image(mg1)
st.sidebar.markdown('**Developed by:** duvancastro@usp.br')
st.sidebar.markdown('**Guided by Prof.PhD:** lubencg@sc.usp.br')
im2 = Image.open('grupo.jpg')
st.sidebar.image(im2)
pg.run()