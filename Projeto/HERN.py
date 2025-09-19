import streamlit as st
import numpy as np
from data import add_point_hern,state_items_N
from plot import reset_app,clear_plot_N

col_bar  = st.sidebar.columns([0.5,0.5])

reset = col_bar[1].button('Reset App',type='primary',key='reset')
clear = col_bar[0].button('Clear Plot',type='primary',key='clear')

if clear:
    clear_plot_N()

if reset:
    reset_app()

if 'fig_N' not in st.session_state:
    clear_plot_N()

col1,col2 = st.columns([0.3,0.7])
with col1:
    
    st.markdown('<h1 style="text-align: center;">Figure Creation</h1>', unsafe_allow_html=True)
    
    with st.form('Variaveis'):
        nn = st.select_slider('Número de Pontos',options=np.arange(1,101),key='nn',value =50) 
        n = st.select_slider('Number of Heat Transfer Units `NTU`',options=np.arange(1,21),key='n', value=10)
        C_min = st.radio(label='Select Minimum Thermal Capacitance',options= ['CF','CQ'],horizontal=True,label_visibility='visible')
        t = st.number_input("Adicione um novo Número `C*`",min_value=0.001,max_value=1.00,step=0.01)
        submit0 = st.form_submit_button('Add')

    if submit0:
        state_items_N(n=n,nn=nn,t=t,C_min=C_min)

    with st.form("parametros"):
        box1 = st.multiselect('Case',options=st.session_state['cases'],key='case_box_f1')

        C_box1 = st.multiselect('Ratio of Thermal Capacitances `C*`', options = st.session_state[C_min],key='C_box')
        Np1 = st.select_slider('Number of de Passes `Np`',options=np.arange(1,21),key='np1')
        Nr1 = st.select_slider('Number of de Tubes `Nr`',options=np.arange(1,21),key='nr1')
        tau =  st.number_input('Ratio Temperature `τ`' , min_value=0.001, max_value=1.00,step=0.01,key='tau')
        tp  =  st.radio(label='Select Type Plot',options= ['Ys','HERN'],horizontal=True,label_visibility='visible')
        submit1 =st.form_submit_button('Plot')

    if submit1:
        add_point_hern( fig = st.session_state['fig_N'], box=box1 , Np=Np1 , Nr=Nr1 , C_box=C_box1 , C_min=C_min,tau = tau,tp=tp)

with col2:
    st.markdown(f'<h1 style="text-align: center;">Visualization Screen</h1>', unsafe_allow_html=True)
    cnt = st.container(border=True)
    cnt.plotly_chart(st.session_state['fig_N'])

