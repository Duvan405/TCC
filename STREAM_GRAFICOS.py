
#?_________________________LIBRERIAS__________________________________________
from CASOS import C1B1C as B1C1 #type: ignore
from CASOS import C1A as A1 #type: ignore
from CASOS import C2B2C as B2C2 #type: ignore
from CASOS import C2A as A2 #type: ignore
from CASOS import C3A3B3C as A3B3C3 #type: ignore
import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator #type: ignore
#?____________________________________________________________________________
def templete(F,P):
    fig,ax = plt.subplots() 
    for i,Re in enumerate(R):
        ax.plot(P[i,:],F[i,:], label = f'R={Re}')
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.05))
    ax.grid(which='both', axis='both', linestyle='--', linewidth=1)
    plt.ylabel('F [-]')
    plt.xlabel('P [-]')
    plt.legend()
    plt.xlim(0,1)
    plt.ylim(0,1)
    return fig


R  = [0.1,0.2,0.4,0.5,0.6,0.8,0.9,1,1.5,2,3,4,5]

st.set_page_config(layout = "wide", page_title="GRAFICOS TCC")
st.header("GRAFICOS CONFIGURAÇÕES TROCADORES DE CALOR",divider="red")
slider1 = st.sidebar.slider("Número de pasos", 1,10)
st.sidebar.write("Np = ",slider1)
slider2 = st.sidebar.slider("Número de tubos", 1,10)
st.sidebar.write("Nr = ",slider2)
Np = slider1
Nr = slider2
col1,col2,col3 = st.columns([0.33333,0.33333,0.3333])


chbox2 = col1.checkbox("PLOT CASO 1A")
if chbox2:
    FA1,PA1 = A1.array_1A(Np,Nr,R)
    g_1A = templete(FA1,PA1)
    col1.pyplot(g_1A)
    
chbox3 = col2.checkbox("PLOT CASO 1B")
if chbox3:
    FB1,PB1 = B1C1.array_1B1C(Np,Nr,'1B',R)
    g_1B = templete(FB1,PB1)
    col2.pyplot(g_1B)
    
chbox4 = col3.checkbox("PLOT CASO 1C")
if chbox4:
    FC1,PC1 = B1C1.array_1B1C(Np,Nr,'1C',R)
    g_1C = templete(FC1,PC1)
    col3.pyplot(g_1C)
col1.markdown("F.I  misturado/F.E  misturado")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E  misturado")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E  misturado")    


st.header("", divider = "blue")
col1,col2,col3 = st.columns([0.33333,0.33333,0.3333])

chbox5 = col1.checkbox("PLOT CASO 2A")
if chbox5:
    FA2,PA2 = A2.array_2A(Np,Nr,R)
    g_2A = templete(FA2,PA2)
    col1.pyplot(g_2A)
    
chbox6 = col2.checkbox("PLOT CASO 2B")
if chbox6:
    FB2,PB2 = B2C2.array_2B2C(Np,Nr,'2B',R)
    g_2B = templete(FB2,PB2)
    col2.pyplot(g_2B)
    
chbox7 = col3.checkbox("PLOT CASO 2C")
if chbox7:
    FC2,PC2 = B2C2.array_2B2C(Np,Nr,'2C',R)
    g_2C = templete(FC2,PC2)
    col3.pyplot(g_2C)

col1.markdown("F.I  misturado/F.E misturado (C.C)")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E misturado (C.C)")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E misturado (C.C)")   

st.header("", divider = "blue")

col1,col2,col3 = st.columns([0.33333,0.33333,0.3333])

chbox8 = col1.checkbox("PLOT CASO 3A")
if chbox8:
    FA3,PA3 = A3B3C3.array_3A3B3C(Np,Nr,'3A',R)
    g_3A = templete(FA3,PA3)
    col1.pyplot(g_3A)
    
chbox9 = col2.checkbox("PLOT CASO 3B")
if chbox9:
    FB3,PB3 = A3B3C3.array_3A3B3C(Np,Nr,'3B',R)
    g_3B = templete(FB3,PB3)
    col2.pyplot(g_3B)
    
chbox10 = col3.checkbox("PLOT CASO 3C")
if chbox10:
    FC3,PC3 = A3B3C3.array_3A3B3C(Np,Nr,'3C',R)
    g_3C = templete(FC3,PC3)
    col3.pyplot(g_3C)

col1.markdown("F.I  misturado / F.E Não misturado")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E Não misturado")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E Não misturado")    
st.header("",divider= "blue")


