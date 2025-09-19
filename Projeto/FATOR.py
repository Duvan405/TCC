
import streamlit as st
from data import add_point_factor,state_items_F,params
from plot import reset_app,clear_plot_F
import numpy as np

col_bar  = st.sidebar.columns([0.5,0.5])
reset = col_bar[1].button('Reset App',type='primary',key='reset')
clear = col_bar[0].button('Clear Plot',type='primary',key='clear')

if clear:
    clear_plot_F() 

if reset:
    reset_app()

if 'fig_F' not in st.session_state:
    clear_plot_F() 


col1,col2 = st.columns([0.3,0.7])

with col1:
    st.markdown('<h1 style="text-align: center;">Figure Creation</h1>', unsafe_allow_html=True)

    with st.form('Variaveis'):
        nn = st.select_slider('Number of  Elements',options=np.arange(1,101),key='nn',value =50) 
        n = st.select_slider('Number of Heat Transfer Units `NTU`',options=np.arange(1,101),key='n', value=50) 
        t = st.number_input("Adicione um novo Número `R`",min_value=0.001,max_value=10.00,step=0.01)
        submit0 = st.form_submit_button('`Add`')

    if submit0:
        state_items_F(n=n,nn=nn,t=t)

    with st.form("parametros"):
        box1 = st.multiselect('Case',options=st.session_state['cases'],key='case_box_f1')
        R_box1 = st.multiselect('Heat Capacity `R`',options=st.session_state['R'],key='R_box_f1')
        Np1 = st.select_slider('Number of de Passes `Np`',options=np.arange(1,21),key='np1')
        Nr1 = st.select_slider('Number of de Tubes `Nr`',options=np.arange(1,21),key='nr1')
        cl = st.columns([0.5,0.5])
        submit1 = cl[0].form_submit_button('`Plot`')
        submit2 = cl[1].form_submit_button('`Correlation`')

    if submit1:
        add_point_factor( fig = st.session_state['fig_F'], box=box1 , Np=Np1 , Nr=Nr1 , R_box=R_box1)
   
        

with col2:
    st.markdown('<h1 style="text-align: center;">Visualization Screen</h1>', unsafe_allow_html=True)
    cnt = st.container(border=True)
    cnt.plotly_chart(st.session_state['fig_F'])

st.markdown("# Correlation Form") 
st.markdown("### $F(P,NTU)=1+a_1P +a_2NTU +a_3P^2 +a_4P.NTU +a_5NTU^2$") 
try:
    if submit2:
        params(case=box1,Np=Np1,Nr=Nr1,R_list=R_box1)
    st.table(st.session_state['df_F'])    
except:
    st.warning('It is not possible to establish or calculate a correlation. Try again with another parameters')