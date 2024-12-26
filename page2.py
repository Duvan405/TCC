from CASOS import C1B1C as B1C1 #type: ignore
from CASOS import C1A as A1 #type: ignore
from CASOS import C2B2C as B2C2 #type: ignore
from CASOS import C2A as A2 #type: ignore
from CASOS import C3A3B3C as A3B3C3 #type: ignore
import pandas as pd
import numpy as np
import streamlit as st


valores = np.array([round(x * 0.1, 1) for x in range(1, 11)] + list(range(1, 11)))
st.header("CASO 1A",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPA1 = col1.slider("Número de pasos [1A]",1,20)
NRA1 = col1.slider("Número de tubos [1A]",1,20)
CA1 = col1.select_slider("R [1A]",options = valores,value=1)
FA1,PA1 = A1.comp_1A(NPA1,NRA1,CA1)
dictA1 = {"FA1":FA1,"PA1":PA1}
dfA1 = pd.DataFrame(dictA1)
col2.line_chart(dfA1,x="PA1",y="FA1")


st.header("CASO 1B",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPB1 = col1.slider("Número de pasos [1B]",1,20)
NRB1 = col1.slider("Número de tubos [1B]",1,20)
CB1 = col1.select_slider("R [1B]",options = valores,value=1)
FB1,PB1 = B1C1.comp_1B1C(NPB1,NRB1,"1B",CB1)
dictB1 = {"FB1":FB1,"PB1":PB1}
dfB1 = pd.DataFrame(dictB1)
col2.line_chart(dfB1,x="PB1",y="FB1")


st.header("CASO 1C",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPC1 = col1.slider("Número de pasos [1C]",1,20)
NRC1 = col1.slider("Número de tubos [1C]",1,20)
CC1 = col1.select_slider("R [1C]",options = valores,value=1)
FC1,PC1 = B1C1.comp_1B1C(NPC1,NRC1,"1C",CC1)
dictC1 = {"FC1":FC1,"PC1":PC1}
dfC1 = pd.DataFrame(dictC1)
col2.line_chart(dfC1,x="PC1",y="FC1")


st.header("CASO 2A",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPA2 = col1.slider("Número de pasos [2A]",1,20)
NRA2 = col1.slider("Número de tubos [2A]",1,20)
CA2 = col1.select_slider("R [2A]",options = valores,value=1)
FA2,PA2 = A2.comp_2A(NPA2,NRA2,CA2)
dictA2 = {"FA2":FA2,"PA2":PA2}
dfA2 = pd.DataFrame(dictA2)
col2.line_chart(dfA2,x="PA2",y="FA2")


st.header("CASO 2B",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPB2 = col1.slider("Número de pasos [2B]",1,20)
NRB2 = col1.slider("Número de tubos [2B]",1,20)
CB2 = col1.select_slider("R [2B]",options = valores,value=1)
FB2,PB2 = B2C2.comp_2B2C(NPB1,NRB1,"2B",CB1)
dictB2 = {"FB2":FB2,"PB2":PB2}
dfB2 = pd.DataFrame(dictB2)
col2.line_chart(dfB2,x="PB2",y="FB2")


st.header("CASO 2C",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPC2 = col1.slider("Número de pasos [2C]",1,20)
NPC2 = col1.slider("Número de tubos [2C]",1,20)
CC2 = col1.select_slider("R [2C]",options = valores,value=1)
FC2,PC2 = B2C2.comp_2B2C(NPC2,NPC2,"2C",CC2)
dictC2 = {"FC2":FC2,"PC2":PC2}
dfC2 = pd.DataFrame(dictC2)
col2.line_chart(dfC2,x="PC2",y="FC2")


st.header("CASO 3A",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPA3 = col1.slider("Número de pasos [3A]",1,20)
NRA3 = col1.slider("Número de tubos [3A]",1,20)
CA3 = col1.select_slider("R [3A]",options = valores,value=1)
FA3,PA3 = A3B3C3.comp_3A3B3C(NPA3,NRA3,"3A",CA3)
dictA3 = {"FA3":FA3,"PA3":PA3}
dfA3 = pd.DataFrame(dictA3)
col2.line_chart(dfA3,x="PA3",y="FA3")


st.header("CASO 3B",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPB3 = col1.slider("Número de pasos [3B]",1,20)
NRB3 = col1.slider("Número de tubos [3B]",1,20)
CB3 = col1.select_slider("R [3B]",options = valores,value=1)
FB3,PB3 = A3B3C3.comp_3A3B3C(NPB3,NRB3,"3B",CB3)
dictB3 = {"FB3":FB3,"PB3":PB3}
dfB3 = pd.DataFrame(dictB3)
col2.line_chart(dfB3,x="PB3",y="FB3")


st.header("CASO 3C",divider="red")
col1,col2 = st.columns([0.3,0.5])
NPC3 = col1.slider("Número de pasos [3C]",1,20)
NRC3 = col1.slider("Número de tubos [3C]",1,20)
CC3 = col1.select_slider("R [3C]",options = valores,value=1)
FC3,PC3 = A3B3C3.comp_3A3B3C(NPC3,NRC3,"3C",CC3)
dictC3 = {"FC3":FC3,"PC3":PC3}
dfC3 = pd.DataFrame(dictC3)
col2.line_chart(dfC3,x="PC3",y="FC3")

