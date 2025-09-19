import streamlit as st
import numpy as np
from data import add_point_epsilon,state_items_E,params_epsilon
from plot import reset_app,clear_plot_E


col_bar  = st.sidebar.columns([0.5,0.5])

reset = col_bar[1].button('Reset App',type='primary',key='reset')
clear = col_bar[0].button('Clear Plot',type='primary',key='clear')

if clear:
    clear_plot_E() 
if reset:
    reset_app()
if 'fig_E' not in st.session_state:
    clear_plot_E() 
col1,col2 = st.columns([0.3,0.7])

with col1:
    st.markdown('<h1 style="text-align: center;">Figure Creation</h1>', unsafe_allow_html=True)

    with st.form('Variaveis'):
        nn = st.select_slider('Número de Pontos',options=np.arange(1,101),key='nn',value =50) 
        n = st.select_slider('Number of Heat Transfer Units `NTU`',options=np.arange(1,21),key='n', value=10)
        C_min = st.radio(label='Select Type Plot',options= ['CF','CQ'],horizontal=True,label_visibility='visible') 
        t = st.number_input("Adicione um novo Número `C*`",min_value=0.001,max_value=1.00,step=0.01)
        submit0 = st.form_submit_button('Add')

    if submit0:
        state_items_E(n=n,nn=nn,t=t,C_min=C_min)

    with st.form("parametros"):
        box1 = st.multiselect('Case',options=st.session_state['cases'],key='case_box_f1')
        C_box1 = st.multiselect('Ratio of Thermal Capacitances `C*`', options = st.session_state[C_min],key='C_box')
        Np1 = st.select_slider('Number of de Passes `Np`',options=np.arange(1,21),key='np1')
        Nr1 = st.select_slider('Number of de Tubes `Nr`',options=np.arange(1,21),key='nr1')
        cl = st.columns([0.5,0.5])
        submit1 = cl[0].form_submit_button('`Plot`')
        submit2 = cl[1].form_submit_button('`Correlation`')

    if submit1:
        add_point_epsilon( fig = st.session_state['fig_E'], box=box1 , Np=Np1 , Nr=Nr1 , C_box=C_box1 , C_min=C_min)

with col2:
    st.markdown('<h1 style="text-align: center;">Visualization Screen</h1>', unsafe_allow_html=True)
    cnt = st.container(border=True)
    cnt.plotly_chart(st.session_state['fig_E'])


st.markdown("# Correlation Form") 
st.markdown("### $Epsilon(NTU) = a_1*(exp(-a_2*(1-exp(-a_3*NTU^{a_4}))))$")
try: 
    if submit2:
        params_epsilon(case=box1,Np=Np1,Nr=Nr1,C_box=C_box1,C_min=C_min)
    st.table(st.session_state['df_E'])    
except:
    st.warning('It is not possible to establish or calculate a correlation. Try again with another parameters')