from CASOS import C1B1C,C1A,C2B2C,C2A,C3A3B3C    
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

cores = {
    '1A':"blue",'1B': "red", '1C':"green", '2A':"purple", '2B':"orange",
    '2C':"cyan",'3A': "magenta", '3B':"lime", '3C':"brown"
}



def figure_add(df,R_list,fig,case):
    for R in R_list:
        fig.add_trace(go.Scatter(x=df[f'P[{R}]'],y=df[f'F[{R}]']
                                         ,mode='lines',line=dict(color=cores[case]), 
                                         name = f'{case}'if R == R_list[0] else None ,
                                        showlegend = bool(R == R_list[0])))
def plot_abacos(fig,slect,Np,Nr,R_list):
    for case  in slect:
        if case == '1A':
            df = C1A.array_1A(Np,Nr,R_list)
            figure_add(df,R_list,fig,case)
        elif case == '1B':
            df= C1B1C.array_1B1C(Np,Nr,'1B',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '1C':
            df= C1B1C.array_1B1C(Np,Nr,'1C',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '2A':
            df = C2A.array_2A(Np,Nr,R_list)
            figure_add(df,R_list,fig,case)
        elif case == '2B':
            df = C2B2C.array_2B2C(Np,Nr,'2B',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '2C':
            df = C2B2C.array_2B2C(Np,Nr,'2C',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '3A':
            df = C3A3B3C.array_3A3B3C(Np,Nr,'3A',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '3B':
            df = C3A3B3C.array_3A3B3C(Np,Nr,'3B',R_list)
            figure_add(df,R_list,fig,case)
        elif case == '3C':
            df= C3A3B3C.array_3A3B3C(Np,Nr,'3C',R_list)
            figure_add(df,R_list,fig,case)

    fig.update_traces(marker=dict(size=10), textposition='top center')
    fig.update_xaxes(title ="P [-]",title_font=dict(color="black",size=18,family="Times New Roman"), 
                      showgrid=True, gridcolor="gray", gridwidth=0.3,zeroline=True,zerolinecolor="black",zerolinewidth=3)
    fig.update_yaxes(title ="F [-]",title_font=dict(color="black",size=18,family="Times New Roman"),
                     showgrid=True,gridcolor="gray",gridwidth=0.3,zeroline=True, zerolinecolor="black",zerolinewidth=3)
    fig.update_layout(title = 'PLOT CASOS PINGONATTI ',title_font=dict(family="Times New Roman",size=24,color="black"),
                      title_x=0.3,font=dict(family="Times New Roman",size=14,color="black"))


R_list = [0.1,0.3,0.8,2,4.0]

Np= st.sidebar.select_slider('Número de Pasos',options=np.arange(1,21))
Nr= st.sidebar.select_slider('Número de Tubos',options=np.arange(1,21))
df = C3A3B3C.array_3A3B3C(Np,Nr,'3B',R_list)
col1,col2 = st.columns([0.3,0.7])
with col1:
    caso = st.multiselect('Casos Pingonalli',['1A','1B','1C','2A','2B','2C','3A','3B','3C'])

with col2:
    
    fig = go.Figure()
    plot_abacos(fig,caso,Np,Nr,R_list)
    st.plotly_chart(fig)