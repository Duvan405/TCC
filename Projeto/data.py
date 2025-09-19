import numpy as np
import pandas as pd
import scipy as sp
from scipy.optimize import curve_fit 
from plotly import graph_objects as go
from casos import (data_1A,data_1BC,data_2A,data_2BC,data_3ABC,data_EPI,data_NRTC,data_4A,data_4BC) 
import streamlit as st
def modelo_fator(vars:tuple[float,float], a1:float, a2:float, a3:float, a4:float, a5:float)->np.array:
    P, NTU = vars
    return  (1+a1*P +a2*NTU +a3*P**2 +a4*P*NTU +a5*NTU**2)

def modelo_epsilon(NTU:np.array, a1:float, a2:float, a3:float,a4)->np.array:
    return (a1*(np.exp(-a2*(1-np.exp(-a3*NTU**a4)))))

def params_epsilon(case:list,Np:int,Nr:int,C_box:list,C_min:str)->pd.DataFrame:  
    df=st.session_state['df_E']
    if C_min =='CQ':
        C_box = np.round(np.array(C_box)**(-1),2)
    for caso in case:
        dic = data_EPI(compute_fator(N_p=Np,N_r=Nr,NTU=st.session_state['NTU_E'],R_list=C_box,case=caso))
        for C in C_box:
            list_cons, _ = curve_fit(modelo_epsilon,dic[C_min][C]['EPI'],dic[C_min][C]['NTU'])
            fila = {
                'Case' : caso,
                'C*'   : C,
                'C_min': C_min,
                'Np'   : Np,
                'Nr'   : Nr
                }
            for i, val in enumerate(list_cons, start=1):
                fila[f'a{i}'] = val
            df.loc[len(df)] = fila
    st.session_state['df_E']= df

def params(case:list,Np:int,Nr:int,R_list:list)->pd.DataFrame:
    df=st.session_state['df_F']
    for caso in case:
        dic = compute_fator(case=caso,N_p=Np,N_r=Nr,R_list=R_list,NTU=st.session_state['NTU_F'])
        for R in R_list:
            list_cons, _ = curve_fit(modelo_fator,(dic[R]['P'],dic[R]['NTU']), dic[R]['F'])
            fila = {
                'Case': caso,
                'R': R,
                'Np': Np,
                'Nr': Nr
            }
            for i, val in enumerate(list_cons, start=1):
                fila[f'a{i}'] = val
            df.loc[len(df)] = fila
    st.session_state['df_F']= df

def compute_fator(case:str,N_p:int,N_r:int,R_list:list,NTU:np.array)->dict:
    match case:
        case '1A':
            return data_1A(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU)
        case '1B'|'1C':
            return data_1BC(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU,caso=case)
        case '2A':
            return data_2A(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU)
        case '2B'|'2C':
            return data_2BC(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU,caso=case)
        case '3A'|'3B'|'3C':
            return data_3ABC(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU,caso=case)
        case '4A':  
            return data_4A(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU)  
        case '4B'|'4C':   
            return data_4BC(N_p=N_p,N_r=N_r,R_list=R_list,NTU=NTU,caso=case)


def creat_list():
    st.session_state['cases']= ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
    st.session_state['R'] =[0.2 , 0.4 , 0.6 , 0.8, 1.0, 1/0.8, 1/0.4 , 1/0.2]
    R = np.array(st.session_state['R'])
    st.session_state['CF'] = R[R <= 1].tolist()
    st.session_state['CQ'] = (1 / R[R > 1]).tolist()
    st.session_state['NTU_F'] = np.geomspace(0.001,50,50)
    st.session_state['NTU_E'] = np.geomspace(0.001,10,50)
    st.session_state['NTU_N'] = np.geomspace(0.001,10,50)
    st.session_state['df_F'] = pd.DataFrame(columns=['Case','R','Np','Nr','a1','a2','a3','a4','a5'])
    st.session_state['df_E'] = pd.DataFrame(columns=['Case','C*','C_min','Np','Nr','a1','a2','a3','a4'])

def add_point_factor( fig , box:list, Np:int , Nr:int , R_box:list):
    for case in box:
        dic = compute_fator(N_p=Np,N_r=Nr,NTU=st.session_state['NTU_F'],R_list=R_box,case=case)
        for i in dic: 
            fig.add_trace(go.Scatter(x=dic[i]['P'],y=dic[i]['F'] , mode='lines+markers',name=f'{case};(Np={Np},Nt={Nr});R={i}'))

def add_point_epsilon( fig , box:list, Np:int , Nr:int , C_box:list , C_min:str):
    if C_min=='CQ':
        C_box = np.round(np.array(C_box)**(-1),2)
    for case in box:
        dic = data_EPI(compute_fator(N_p=Np,N_r=Nr,NTU=st.session_state['NTU_E'],R_list=C_box,case=case))
        for i in dic[C_min]: 
            fig.add_trace( go.Scatter(x=dic[C_min][i]['NTU'] , y=dic[C_min][i]['EPI'] , mode='lines+markers',name=f'{case};(Np={Np},Nt={Nr});C*={i}'))

def add_point_hern( fig , box:list, Np:int , Nr:int , C_box:list , C_min:str , tau:float, tp:str ):
    if C_min=='CQ':
        C_box = np.round(np.array(C_box)**(-1),2)
    for case in box:
        dic = data_NRTC(dic=data_EPI(compute_fator(N_p=Np,N_r=Nr,NTU=st.session_state['NTU_N'],R_list=C_box,case=case)),r=tau)
        for i in dic[C_min]: 
            fig.add_trace( go.Scatter(x=dic[C_min][i]['NTU'] , y=dic[C_min][i][tp] , mode='lines+markers',name=f'{case};(Np={Np},Nt={Nr});C*={i};τ={tau}'))



def state_items_F(n:float,nn:float,t:float):
    st.session_state['NTU_F'] = np.geomspace(0.001,n,nn)
    if t not in st.session_state['R']:
        st.session_state['R'].append(t)
        st.session_state['R'] = sorted(st.session_state['R'])

def state_items_E(n:float,nn:float,t:float,C_min:str):
    st.session_state['NTU_E'] = np.geomspace(0.001,n,nn)
    if t not in st.session_state[C_min]:
        st.session_state[C_min].append(round(t,2))
        st.session_state[C_min] = sorted(st.session_state[C_min])

def state_items_N(n:float,nn:float,t:float,C_min:str):
    st.session_state['NTU_N'] = np.geomspace(0.001,n,nn)
    if t not in st.session_state[C_min]:
        st.session_state[C_min].append(round(t,2))
        st.session_state[C_min] = sorted(st.session_state[C_min])


