import streamlit as st
import numpy as np
from data import creat_list
from plotly import graph_objects as go

def reset_app():
    st.session_state.clear()
    st.cache_data.clear()
    creat_list()



def labels_F (fig_F):
    fig_F.update_layout(
    xaxis=dict(
        title="Effectiveness of temperatures P [-]", 
        title_font=dict(family="Times New Roman", size=20, color="black"),  
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"))
        ,
        yaxis=dict(
        title="Correction Fator F [-]",  
        title_font=dict(family="Times New Roman", size=20, color="black"), 
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"),
        ),width=900, height=775,
            legend=dict(
        font=dict(
            family="Times New Roman",
            size=15,  
            color="black")))
    fig_F.update_xaxes(range=[0,1])
    fig_F.update_yaxes(range=[0,1])


def labels_E (fig_E):
    fig_E.update_layout(
    xaxis=dict(
        title="Number of Heat Transfer Units NTU [-]", 
        title_font=dict(family="Times New Roman", size=20, color="black"),  
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"))
        ,
        yaxis=dict(
        title="Effectiveness ε [-]",  
        title_font=dict(family="Times New Roman", size=20, color="black"), 
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"),
        ),width=1150, height=855,
            legend=dict(
        font=dict(
            family="Times New Roman",
            size=15,  
            color="black")))
    fig_E.update_xaxes(range=[0,max(st.session_state['NTU_E'])])
    fig_E.update_yaxes(range=[0,1])

def labels_N(fig_N):
    fig_N.update_layout(
    xaxis=dict(
        title="Number of Heat Transfer Units NTU [-]", 
        title_font=dict(family="Times New Roman", size=20, color="black"),  
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"))
        ,
        yaxis=dict(
        title="Entropy Generation [-]",  
        title_font=dict(family="Times New Roman", size=20, color="black"), 
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"),
        ),width=900, height=600,
            legend=dict(
        font=dict(
            family="Times New Roman",
            size=15,  
            color="black")))
    fig_N.update_xaxes(range=[0,max(st.session_state['NTU_N'])])
    fig_N.update_yaxes(range=[0,1])


def clear_plot_N():
    fig_N =  go.Figure()
    labels_N(fig_N)
    st.session_state['fig_N']=fig_N

def clear_plot_F():
    fig_F =  go.Figure()
    labels_F(fig_F)
    st.session_state['fig_F']=fig_F

def clear_plot_E():
    fig_E =  go.Figure()
    labels_E(fig_E)
    st.session_state['fig_E']=fig_E  


