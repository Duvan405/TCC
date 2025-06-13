

from Casos import  (data_1A,data_1BC,data_2A,data_2BC,data_3ABC,data_EPI,data_NRTC,data_4A,data_4BC) 
import streamlit as st # type: ignore
import numpy as np
import requests
from PIL import Image
from io import BytesIO
import plotly.graph_objects as go # type: ignore

st.set_page_config(layout='wide')
url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Feesc.usp.br%2Finstitucional%2Fidentidade_visual.php&psig=AOvVaw3OFC1Dq2sB2OrXVD2AhxjY&ust=1749944750295000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCTnavK740DFQAAAAAdAAAAABAE"
response = requests.get(url)
log = Image.open(BytesIO(response.content))
st.logo(log)
barra_tempo = st.sidebar.empty()
barra_tempo.progress(25,"please, Wait")
def point_plot(dic,slect,k,j,caso):
    for i in slect: 
        fig_E.add_trace(go.Scatter(x=dic[k][i]['NTU'],y=dic[k][i]['EPI'],mode='lines+markers',name=f'{caso}:C={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))

def ad_point_epi(slect_caso,slect_c,k):

    for j,caso in enumerate(slect_caso):
        if caso == '1A':
            dic_1A_C = data_EPI(data_1A(N_p,N_r,R_list))
            point_plot(dic_1A_C,slect_c,k,j,caso) 
    
        if caso == '1B':
 
            dic_1B_C= data_EPI(data_1BC(N_p,N_r,'1B',R_list))
            point_plot(dic_1B_C,slect_c,k,j,caso) 
        
        if caso ==  '1C':
           
            dic_1C_C = data_EPI(data_1BC(N_p,N_r,'1c',R_list))
            point_plot(dic_1C_C,slect_c,k,j,caso) 

        if caso == '2A':
          
            dic_2A_C = data_EPI(data_2A(N_p,N_r,R_list))
            point_plot(dic_2A_C,slect_c,k,j,caso) 

        if caso == '2B':
          
            dic_2B_C= data_EPI(data_2BC(N_p,N_r,'2B',R_list))
            point_plot(dic_2B_C,slect_c,k,j,caso) 

        if caso == '2C':
    
            dic_2C_C = data_EPI(data_2BC(N_p,N_r,'2C',R_list))
            point_plot(dic_2C_C,slect_c,k,j,caso) 
        
        if caso == '3A' :
   
            dic_3A_C = data_EPI(data_3ABC(N_p,N_r,'3A',R_list))
            point_plot(dic_3A_C,slect_c,k,j,caso) 
        
        if caso == '3B':
  
            dic_3B_C = data_EPI(data_3ABC(N_p,N_r,'3B',R_list))
            point_plot(dic_3B_C,slect_c,k,j,caso) 
        
        if caso == '3C':

            dic_3C_C= data_EPI(data_3ABC(N_p,N_r,'3C',R_list))
            point_plot(dic_3C_C,slect_c,k,j,caso) 
        
        if caso == '4A' :
   
            dic_4A_C = data_EPI(data_4A(N_p,N_r,R_list))
            point_plot(dic_4A_C,slect_c,k,j,caso) 
        
        if caso == '4B':
  
            dic_4B_C = data_EPI(data_4BC(N_p,N_r,'4B',R_list))
            point_plot(dic_4B_C,slect_c,k,j,caso) 
        
        if caso == '4C':

            dic_4C_C= data_EPI(data_4BC(N_p,N_r,'4C',R_list))
            point_plot(dic_4C_C,slect_c,k,j,caso)         

def point_plot_NTRC(fig_NRT,dic,slect,z,rad,j,caso):
    for i in slect: 
        fig_NRT.add_trace(go.Scatter(x=dic[z][i]['NTU'],y=dic[z][i][f'{rad}'],mode='lines+markers',name=f'{caso}:C={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
    return fig_NRT
def ad_point_NTRC(fig_NRT,N_p,N_r,R_list,slect_caso,slect,z,rad,tau):
    for j,caso in enumerate(slect_caso):
        if caso == '1A':
            dic_1A_N = data_NRTC(data_EPI(data_1A(N_p,N_r,R_list)),tau)
            fig_NRT =point_plot_NTRC(fig_NRT,dic_1A_N,slect,z,rad,j,caso)
            
        if caso == '1B':
            dic_1B_N = data_NRTC(data_EPI(data_1BC(N_p,N_r,'1B',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_1B_N,slect,z,rad,j,caso)
        
        if caso ==  '1C':
            dic_1C_N = data_NRTC(data_EPI(data_1BC(N_p,N_r,'1C',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_1C_N,slect,z,rad,j,caso)
        
        if caso == '2A':
            dic_2A_N = data_NRTC(data_EPI(data_2A(N_p,N_r,R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_2A_N,slect,z,rad,j,caso)
            
        if caso == '2B':
            dic_2B_N = data_NRTC(data_EPI(data_2BC(N_p,N_r,'2B',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_2B_N,slect,z,rad,j,caso)
            
        if caso == '2C':
            dic_2C_N = data_NRTC(data_EPI(data_2BC(N_p,N_r,'2C',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_2C_N,slect,z,rad,j,caso)
            
        if caso == '3A' :
            dic_3A_N = data_NRTC(data_EPI(data_3ABC(N_p,N_r,'3A',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_3A_N,slect,z,rad,j,caso)
            
        if caso == '3B':
            dic_3B_N = data_NRTC(data_EPI(data_3ABC(N_p,N_r,'3B',R_list)),tau) 
            fig_NRT=point_plot_NTRC(fig_NRT,dic_3B_N,slect,z,rad,j,caso)
        
        if caso == '3C':
            dic_3C_N = data_NRTC(data_EPI(data_3ABC(N_p,N_r,'3C',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_3C_N,slect,z,rad,j,caso)

        if caso == '4A' :
            dic_4A_N = data_NRTC(data_EPI(data_4A(N_p,N_r,R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_4A_N,slect,z,rad,j,caso)
            

        if caso == '4B':
            dic_4B_N = data_NRTC(data_EPI(data_4BC(N_p,N_r,'4B',R_list)),tau) 
            fig_NRT=point_plot_NTRC(fig_NRT,dic_4B_N,slect,z,rad,j,caso)
        
        if caso == '4C':
            dic_4C_N = data_NRTC(data_EPI(data_4BC(N_p,N_r,'4C',R_list)),tau)
            fig_NRT=point_plot_NTRC(fig_NRT,dic_4C_N,slect,z,rad,j,caso)

    return fig_NRT

def config_plot(titley,fig_NRT):
    fig_NRT.update_layout(
    title="Geração de Entropía",  
    title_font=dict(family="Times New Roman", size=20, color="black"),  
    xaxis=dict(
        title="NTU [-]", 
        title_font=dict(family="Times New Roman", size=18, color="black"),  
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=18, color="black"))
        ,
        yaxis=dict(
        title=f"{titley}",  
        title_font=dict(family="Times New Roman", size=18, color="black"), 
        showgrid=True, 
        gridcolor="gray", 
        gridwidth=0.5,  
        tickfont=dict(family="Times New Roman", size=18, color="black"),
        ),)   
    return fig_NRT

casos_list = ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
R_list = [0.2,0.4,0.6,0.8,1.0,1/0.8,round(1/0.6,2),1/0.4,1/0.2]
CF_list = []
CQ_list = []
marker_list = ['hash',"square",'diamond','diamond','pentagon','x','hexagon','triangle','star','hourglass','bowtie','hexagon2'] 
slect_caso  = st.sidebar.multiselect('Case Selection',casos_list,key='box_casos')
N_p = st.sidebar.select_slider('Number of de Passes `Np`',options=np.arange(1,21))
N_r = st.sidebar.select_slider('Number of Tubes `Nt`',options=np.arange(1,21))
with st.sidebar.expander("Proposed Arrangements"):
    st.image('casos.PNG')

st.sidebar.markdown('**Developed by:** duvancastro@usp.br')
st.sidebar.markdown('**Guided by Prof.PhD:** lubencg@sc.usp.br')
st.sidebar.image('grupo.png',width=400)

for R in R_list:
    if R <= 1:
        CF_list.append(round(R,3))
    else:
        CQ_list.append(round(1/R,3))


tab1 , tab2 , tab3 =st.tabs(['Correction Fator','Effectiveness','Entropy'])


fig_F = go.Figure()
fig_F.update_layout(

xaxis=dict(
    title="Effectiveness of temperatures [-]", 
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
    ),width=900, height=600)  
fig_F.update_xaxes(range=[0,1])
fig_F.update_yaxes(range=[0,1])

barra_tempo.progress(50,"please, Wait")

fig_E = go.Figure()
fig_E.update_layout(width=900, height=600,
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
    title=r"ε       "+"[-]",  
    title_font=dict(family="Times New Roman", size=18, color="black"), 
    showgrid=True, 
    gridcolor="gray", 
    gridwidth=0.5,  
    tickfont=dict(family="Times New Roman", size=14, color="black"),
    ),)
fig_E.update_xaxes(range=[0,10])
fig_E.update_yaxes(range=[0,1])  

fig_NRT = go.Figure()
fig_NRT.update_layout(width=900, height=600)
fig_NRT.update_xaxes(range=[0,10])
fig_NRT.update_yaxes(range=[0,1])

with tab1:
    col1_F,col2_F = st.columns([0.3,0.7])
    with col1_F:
        slect_RF = st.multiselect('Heat Capacity `R`',R_list,key='para_r')      
        btn_f = st.button('Click New Plot',type='primary',key='btnf',)

    with col2_F:
        if btn_f:
            for j,caso in enumerate(slect_caso):
                if caso == '1A':
                    dic_1A = data_1A(N_p,N_r,R_list)
                    for i in slect_RF: 
                        fig_F.add_trace(go.Scatter(x=dic_1A[i]['P'],y=dic_1A[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
                if caso == '1B':
                    dic_1B = data_1BC(N_p,N_r,'1B',R_list)
                    for i in slect_RF: 
                        fig_F.add_trace(go.Scatter(x=dic_1B[i]['P'],y=dic_1B[i]['F'],mode='lines+markers',name=f'{caso}:R={i}',marker= dict(symbol=f'{marker_list[j]}-open',size=5)))
                
                if caso ==  '1C':
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
            st.session_state['fig_F'] =fig_F 
        try:
            st.plotly_chart(st.session_state['fig_F'],use_container_width= True)
        except:
            st.plotly_chart(fig_F,use_container_width= True)

barra_tempo.progress(75,"Please, Wait")
with tab2:

    col1_E,col2_E = st.columns([0.3,0.7])

    with col1_E:
        rad = st.radio('Plot Type Selection',['Cmin = CF','Cmin = CQ'])
        if rad == 'Cmin = CF':
            slect_CF = st.multiselect('Thermal Capacitance Ratio `C*`',CF_list,key='slec_cf')
            k=0
            btne = st.button('Click New Plot',type='primary',key='btne')
            if btne :
                ad_point_epi(slect_caso,slect_CF,k)
                st.session_state['fig_E'] = fig_E
        elif rad == 'Cmin = CQ':
            slect_CQ = st.multiselect('Thermal Capacitance Ratio `C*`',CQ_list,key='slec_cq')
            k=1
            btne = st.button('Click New Plot',type='primary',key='btne')
            if btne :
                ad_point_epi(slect_caso,slect_CQ,k)
                st.session_state['fig_E'] = fig_E
    
    with col2_E:
        try:
            st.plotly_chart(st.session_state['fig_E'],use_container_width=True)
        except:    
            st.plotly_chart(fig_E,use_container_width=True)

with tab3:
    
    col1_NRT,col2_NRT = st.columns([0.3,0.7])

    with col1_NRT:
        col1_aux,col2_aux = st.columns([0.5,0.5])
        rad1 = col1_aux.radio('Plot Type Selection',['Cmin = CF','Cmin = CQ'],key='rad1')
        rad2 = col2_aux.radio('',['HERN','Ys'],key ='rad2' )
        
        if rad1 == 'Cmin = CF':
            slect_NRTF = st.multiselect('Thermal Capacitance Ratio`C*`',CF_list,key='slec_cf_2')
            z=0
            tau = st.slider("Inlet Temperature Ratio `τ`", 0.01, 1.0, 0.01, step = 0.01,key = 'tau')
            btn_N = st.button('Click For New Plot',type='primary',key='btnn')
            if btn_N:
                fig_NRT=ad_point_NTRC(fig_NRT,N_p,N_r,R_list,slect_caso,slect_NRTF,z,rad2,tau)
                fig_NRT=config_plot(rad2,fig_NRT)
                st.session_state['fig_NRT']=fig_NRT
            
        elif rad1 == 'Cmin = CQ':
            slect_NRTQ = st.multiselect('Thermal Capacitance Ratio `C*`',CQ_list,key='slec_cq_2')
            z=1
            tau = st.slider("Inlet Temperature Ratio `τ`", 0.01, 1.0, 0.01, step = 0.01,key = 'tau')
            btn_N = st.button('Click For New Plot',type='primary',key='btnn')
            if btn_N:
                fig_NRT=ad_point_NTRC(fig_NRT,N_p,N_r,R_list,slect_caso,slect_NRTQ,z,rad2,tau)
                fig_NRT=config_plot(rad2,fig_NRT)
                st.session_state['fig_NRT']=fig_NRT

    with col2_NRT:
        try:
            st.plotly_chart(st.session_state['fig_NRT'],use_container_width=True)
        except:
            st.plotly_chart(fig_NRT,use_container_width=True)
barra_tempo.progress(100,"Ready")
