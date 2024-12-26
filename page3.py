from CASOS import C1B1C as B1C1 #type: ignore
from CASOS import C1A as A1 #type: ignore
from CASOS import C2B2C as B2C2 #type: ignore
from CASOS import C2A as A2 #type: ignore
from CASOS import C3A3B3C as A3B3C3 #type: ignore
import pandas as pd
import numpy as np
import streamlit as st

#?____________________________________________________________________________

R  = [0.1,0.2,0.4,0.5,0.6,0.8,0.9,1,1.5,2,3,4,5]


def DF(FI,PI):
    F=np.concatenate(FI)
    P=np.concatenate(PI)
    grupos = np.concatenate([np.full(len(T),f'R ={R[i]}') for i,T in enumerate(PI)])

    dic = {
        "P":P,
        "F":F,
        "R":grupos
    }

    data = pd.DataFrame(dic)
    return data

st.set_page_config(layout = "wide", page_title="GRAFICOS TCC")
st.header("GRAFICOS CONFIGURAÇÕES TROCADORES DE CALOR",divider="red")
slider1 = st.sidebar.slider("Número de pasos", 1,10)
st.sidebar.write("Np = ",slider1)
slider2 = st.sidebar.slider("Número de tubos", 1,10)
st.sidebar.write("Nr = ",slider2)
Np = slider1
Nr = slider2

col1,col2,col3 = st.columns([0.3,0.3,0.3])
chbox2 = col1.checkbox("PLOT CASO 1A")
if chbox2:
    FA1,PA1 = A1.array_1A(Np,Nr,R)
    dfA1 = DF(FA1,PA1)
    col1.scatter_chart(dfA1, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R" ,size=10)

chbox3 = col2.checkbox("PLOT CASO 1B")
if chbox3:
    FB1,PB1 = B1C1.array_1B1C(Np,Nr,'1B',R)
    dfB1 = DF(FB1,PB1)
    col2.scatter_chart(dfB1, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)
    
chbox4 = col3.checkbox("PLOT CASO 1C")
if chbox4:
    FC1,PC1 = B1C1.array_1B1C(Np,Nr,'1C',R)
    dfC1 = DF(FC1,PC1)
    col3.scatter_chart(dfC1, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)
col1.markdown("F.I  misturado/F.E  misturado")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E  misturado")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E  misturado")    


st.header("", divider = "blue")
col1,col2,col3 = st.columns([0.3,0.3,0.3])
chbox5 = col1.checkbox("PLOT CASO 2A")
if chbox5:
    FA2,PA2 = A2.array_2A(Np,Nr,R)
    dfA2 = DF(FA2,PA2)
    col1.scatter_chart(dfA2, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)

chbox6 = col2.checkbox("PLOT CASO 2B")
if chbox6:
    FB2,PB2 = B2C2.array_2B2C(Np,Nr,'2B',R)
    dfB2 = DF(FB2,PB2)
    col2.scatter_chart(dfB2, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)
    
chbox7 = col3.checkbox("PLOT CASO 2C")
if chbox7:
    FC2,PC2 = B2C2.array_2B2C(Np,Nr,'2C',R)
    dfC2 = DF(FC2,PC2)
    col3.scatter_chart(dfC2, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)

col1.markdown("F.I  misturado/F.E misturado (C.C)")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E misturado (C.C)")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E misturado (C.C)")   

st.header("", divider = "blue")

col1,col2,col3 = st.columns([0.3,0.3,0.3])
chbox8 = col1.checkbox("PLOT CASO 3A")
if chbox8:
    FA3,PA3 = A3B3C3.array_3A3B3C(Np,Nr,'3A',R)
    dfA3 = DF(FA3,PA3)
    col1.scatter_chart(dfA3, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)
chbox9 = col2.checkbox("PLOT CASO 3B")
if chbox9:
    FB3,PB3 = A3B3C3.array_3A3B3C(Np,Nr,'3B',R)
    dfB3 = DF(FB3,PB3)
    col2.scatter_chart(dfB3, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)
    
chbox10 = col3.checkbox("PLOT CASO 3C")
if chbox10:
    FC3,PC3 = A3B3C3.array_3A3B3C(Np,Nr,'3C',R)
    dfC3 = DF(FC3,PC3)
    col3.scatter_chart(dfC3, x="P", y="F",x_label="P [-]",y_label="F [-]",color="R",width=10,size=10)

col1.markdown("F.I  misturado / F.E Não misturado")    
col2.markdown("F.I  não misturado com uma Ordem Idêntica das Fileras / F.E Não misturado")    
col3.markdown("F.I  não misturado com uma Ordem Inversa das Fileras / F.E Não misturado")    
st.header("",divider= "blue")


