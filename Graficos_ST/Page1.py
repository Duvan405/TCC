

from Casos import  (data_1A,data_1BC,data_2A,data_2BC,data_3ABC,data_EPI,data_NRTC,data_4A,data_4BC) 
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def point_plot(dic,slect,k,j):
    for i in slect: 
        fig_E.add_trace(go.Scatter(x=dic[k][i]['NTU'],y=dic[k][i]['EPI'],mode='lines+markers',name=f'{caso}:C={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

def ad_point_epi(slect_caso,slect_c,k):

    for j,caso in enumerate(slect_caso):
        if caso == '1A':
            dic_1A_C = data_EPI(dic_1A)
            point_plot(dic_1A_C,slect_c,k,j) 
    
        if caso == '1B':
 
            dic_1B_C= data_EPI(dic_1B)
            point_plot(dic_1B_C,slect_c,k,j) 
        
        if caso ==  '1C':
           
            dic_1C_C = data_EPI(dic_1C)
            point_plot(dic_1C_C,slect_c,k,j) 

        if caso == '2A':
          
            dic_2A_C = data_EPI(dic_2A)
            point_plot(dic_2A_C,slect_c,k,j) 

        if caso == '2B':
          
            dic_2B_C= data_EPI(dic_2B)
            point_plot(dic_2B_C,slect_c,k,j) 

        if caso == '2C':
    
            dic_2C_C = data_EPI(dic_2C)
            point_plot(dic_2C_C,slect_c,k,j) 
        
        if caso == '3A' :
   
            dic_3A_C = data_EPI(dic_3A)
            point_plot(dic_3A_C,slect_c,k,j) 
        
        if caso == '3B':
  
            dic_3B_C = data_EPI(dic_3B)
            point_plot(dic_3B_C,slect_c,k,j) 
        
        if caso == '3C':

            dic_3C_C= data_EPI(dic_3C)
            point_plot(dic_3C_C,slect_c,k,j) 
        
        if caso == '4A' :
   
            dic_4A_C = data_EPI(dic_4A)
            point_plot(dic_4A_C,slect_c,k,j) 
        
        if caso == '4B':
  
            dic_4B_C = data_EPI(dic_4B)
            point_plot(dic_4B_C,slect_c,k,j) 
        
        if caso == '4C':

            dic_4C_C= data_EPI(dic_4C)
            point_plot(dic_4C_C,slect_c,k,j) 
        
 
def point_plot_NTRC(dic,slect,z,rad,j):
    for i in slect: 
        fig_NRT.add_trace(go.Scatter(x=dic[z][i]['NTU'],y=dic[z][i][f'{rad}'],mode='lines+markers',name=f'{caso}:C={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
def ad_point_NTRC(slect_caso,slect,z,rad,tau):
       for j,caso in enumerate(slect_caso):
        if caso == '1A':
            dic_1A_C = data_EPI(dic_1A)
            dic_1A_N = data_NRTC(dic_1A_C,tau)
            point_plot_NTRC(dic_1A_N,slect,z,rad,j)
            
    
        if caso == '1B':
 
            dic_1B_C= data_EPI(dic_1B)
            dic_1B_N = data_NRTC(dic_1B_C,tau)
            point_plot_NTRC(dic_1B_N,slect,z,rad,j)
           
        
        if caso ==  '1C':
           
            dic_1C_C = data_EPI(dic_1C)
            dic_1C_N = data_NRTC(dic_1C_C,tau)
            point_plot_NTRC(dic_1C_N,slect,z,rad,j)
           

        if caso == '2A':
          
            dic_2A_C = data_EPI(dic_2A)
            dic_2A_N = data_NRTC(dic_2A_C,tau)
            point_plot_NTRC(dic_2A_N,slect,z,rad,j)
            

        if caso == '2B':
          
            dic_2B_C= data_EPI(dic_2B)
            dic_2B_N = data_NRTC(dic_2B_C,tau)
            point_plot_NTRC(dic_2B_N,slect,z,rad,j)
            

        if caso == '2C':
    
            dic_2C_C = data_EPI(dic_2C)
            dic_2C_N = data_NRTC(dic_2C_C,tau)
            point_plot_NTRC(dic_2C_N,slect,z,rad,j)
            
        
        if caso == '3A' :
   
            dic_3A_C = data_EPI(dic_3A)
            dic_3A_N = data_NRTC(dic_3A_C,tau)
            point_plot_NTRC(dic_3A_N,slect,z,rad,j)
             

        if caso == '3B':
  
            dic_3B_C = data_EPI(dic_3B)
            dic_3B_N = data_NRTC(dic_3B_C,tau) 
            point_plot_NTRC(dic_3B_N,slect,z,rad,j)
        
        if caso == '3C':

            dic_3C_C= data_EPI(dic_3C)
            dic_3C_N = data_NRTC(dic_3C_C,tau)
            point_plot_NTRC(dic_3C_N,slect,z,rad,j)

        if caso == '4A' :
   
            dic_4A_C = data_EPI(dic_4A)
            dic_4A_N = data_NRTC(dic_4A_C,tau)
            point_plot_NTRC(dic_4A_N,slect,z,rad,j)
             

        if caso == '4B':
  
            dic_4B_C = data_EPI(dic_4B)
            dic_4B_N = data_NRTC(dic_4B_C,tau) 
            point_plot_NTRC(dic_4B_N,slect,z,rad,j)
        
        if caso == '4C':

            dic_4C_C= data_EPI(dic_4C)
            dic_4C_N = data_NRTC(dic_4C_C,tau)
            point_plot_NTRC(dic_4C_N,slect,z,rad,j)
barra_tempo = st.empty()
casos_list = ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
R_list = [0.1,0.2,0.5,0.8,1,2,3,4]
CF_list = []
CQ_list = []
marker_list = ['hash',"square",'diamond','diamond','pentagon','x','hexagon','triangle','star','hourglass','bowtie','hexagon2'] 
slect_caso  = st.sidebar.multiselect('Casos Pignotti',casos_list,key='box_casos')
N_p = st.sidebar.select_slider('Número de Pasos `Np`',options=np.arange(1,21))
N_r = st.sidebar.select_slider('Número de Tubos `Nr`',options=np.arange(1,21))
with st.sidebar.expander("Imagems casos Pignotti (1983)"):
    st.image('casos pignatti.PNG')
    

for R in R_list:
    if R <= 1:
        CF_list.append(round(R,3))
    else:
        CQ_list.append(round(1/R,3))

st.sidebar.markdown('Development by: duvancastro@usp.br')
tab1 , tab2 , tab3 =st.tabs(['Factor de Correção','Efectividade','Entropía'])
barra_tempo.progress(25,"please, Wait")
fig_F = go.Figure()
fig_F.update_layout(
title="Casos Pignotti(1984)",  
title_font=dict(family="Times New Roman", size=20, color="black"),  
xaxis=dict(
    title="P [-]", 
    title_font=dict(family="Times New Roman", size=18, color="black"),  
    showgrid=True, 
    gridcolor="gray", 
    gridwidth=0.5,  
    tickfont=dict(family="Times New Roman", size=14, color="black"))
    ,
    yaxis=dict(
    title="Factor de Correção F [-]",  
    title_font=dict(family="Times New Roman", size=18, color="black"), 
    showgrid=True, 
    gridcolor="gray", 
    gridwidth=0.5,  
    tickfont=dict(family="Times New Roman", size=14, color="black"),
    ),)  
fig_F.update_xaxes(range=[0,1])
fig_F.update_yaxes(range=[0,1])

barra_tempo.progress(50,"please, Wait")
fig_E = go.Figure()
fig_E.update_layout(
title="Efectividade",  
title_font=dict(family="Times New Roman", size=20, color="black"),  
xaxis=dict(
    title="NTU [-]", 
    title_font=dict(family="Times New Roman", size=18, color="black"),  
    showgrid=True, 
    gridcolor="gray", 
    gridwidth=0.5,  
    tickfont=dict(family="Times New Roman", size=14, color="black"))
    ,
    yaxis=dict(
    title=r"ε   "+"[-]",  
    title_font=dict(family="Times New Roman", size=18, color="black"), 
    showgrid=True, 
    gridcolor="gray", 
    gridwidth=0.5,  
    tickfont=dict(family="Times New Roman", size=14, color="black"),
    ),)
fig_E.update_xaxes(range=[0,10])
fig_E.update_yaxes(range=[0,1])  


fig_NRT = go.Figure()
def config_plot(titley):
    fig_NRT.update_layout(
    title="Geração de Entropía",  
    title_font=dict(family="Times New Roman", size=20, color="black"),  
    xaxis=dict(
        title="NTU [-]", 
        title_font=dict(family="Times New Roman", size=18, color="black"),  
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"))
        ,
        yaxis=dict(
        title=f"{titley}",  
        title_font=dict(family="Times New Roman", size=18, color="black"), 
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=14, color="black"),
        ),)
fig_NRT.update_xaxes(range=[0,10])
fig_NRT.update_yaxes(range=[0,1])  

    
with tab1:
    col1_F,col2_F = st.columns([0.4,0.6])


    with col1_F:
        slect_RF = st.multiselect('Parâmetro `R`',R_list,key='para_r')      

    with col2_F:
        for j,caso in enumerate(slect_caso):
            if caso == '1A':
                dic_1A = {}
                dic_1A = data_1A(N_p,N_r,R_list)
    
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_1A[i]['P'],y=dic_1A[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

            if caso == '1B':
                dic_1B={}
                dic_1B = data_1BC(N_p,N_r,'1B',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_1B[i]['P'],y=dic_1B[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso ==  '1C':
                dic_1B={}
                dic_1C = data_1BC(N_p,N_r,'1C',R_list)
               
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_1C[i]['P'],y=dic_1C[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

            if caso == '2A':
                dic_2A = data_2A(N_p,N_r,R_list)
               
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_2A[i]['P'],y=dic_2A[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

            if caso == '2B':
            
                dic_2B = data_2BC(N_p,N_r,'2B',R_list)
             
                for i in slect_RF: 
                     fig_F.add_trace(go.Scatter(x=dic_2B[i]['P'],y=dic_2B[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

            if caso == '2C':

                dic_2C = data_2BC(N_p,N_r,'2C',R_list)
              
                for i in slect_RF: 
                     fig_F.add_trace(go.Scatter(x=dic_2C[i]['P'],y=dic_2C[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso == '3A' :

                dic_3A = data_3ABC(N_p,N_r,'3A',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_3A[i]['P'],y=dic_3A[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso == '3B':

                dic_3B = data_3ABC(N_p,N_r,'3B',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_3B[i]['P'],y=dic_3B[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso == '3C':

                dic_3C = data_3ABC(N_p,N_r,'3C',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_3C[i]['P'],y=dic_3C[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            if caso == '4A' :

                dic_4A = data_4A(N_p,N_r,R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_4A[i]['P'],y=dic_4A[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso == '4B':

                dic_4B = data_4BC(N_p,N_r,'4B',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_4B[i]['P'],y=dic_4B[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            
            if caso == '4C':

                dic_4C = data_4BC(N_p,N_r,'4C',R_list)
                
                for i in slect_RF: 
                    fig_F.add_trace(go.Scatter(x=dic_4C[i]['P'],y=dic_4C[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
            

        st.plotly_chart(fig_F,use_container_width= True)
barra_tempo.progress(75,"Please, Wait")
with tab2:

    col1_E,col2_E = st.columns([0.4,0.6])

    with col1_E:
        rad = st.radio('Seleção do Tipo plot',['Cmin = CF','Cmin = CQ'])
        
        if rad == 'Cmin = CF':
            slect_CF = st.multiselect('Parâmetro `C*`',CF_list,key='slec_cf')
            k=0
            ad_point_epi(slect_caso,slect_CF,k)
        elif rad == 'Cmin = CQ':
            slect_CQ = st.multiselect('Parâmetro `C*`',CQ_list,key='slec_cq')
            k=1
            ad_point_epi(slect_caso,slect_CQ,k)
    with col2_E:
        st.plotly_chart(fig_E,use_container_width=True)
with tab3:
    
    col1_NRT,col2_NRT = st.columns([0.4,0.6])

    with col1_NRT:
        Col1_aux,col2_aux = st.columns([0.5,0.5])
        rad1 = Col1_aux.radio('Seleção do Tipo plot',['Cmin = CF','Cmin = CQ'],key='rad1')
        rad2 = col2_aux.radio('',['HERN','Ys'],key ='rad2' )
        config_plot(rad2)
        
        
        if rad == 'Cmin = CF':
            slect_NRTF = st.multiselect('Parâmetro `C*`',CF_list,key='slec_cf_2')
            z=0
            tau = st.slider("Parâmetro `τ`", 0.01, 1.0, 0.01, step = 0.01,key = 'tau')
            ad_point_NTRC(slect_caso,slect_NRTF,z,rad2,tau)
            
        elif rad == 'Cmin = CQ':
            slect_NRTQ = st.multiselect('Parâmetro `C*`',CQ_list,key='slec_cq_2')
            z=1
            tau = st.slider("Parâmetro `τ`", 0.01, 1.0, 0.01, step = 0.01,key = 'tau')
            ad_point_NTRC(slect_caso,slect_NRTQ,z,rad2,tau)

    with col2_NRT:

        st.plotly_chart(fig_NRT,use_container_width=True)
barra_tempo.progress(100,"Ready")