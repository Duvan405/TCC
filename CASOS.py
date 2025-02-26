import numpy as np
import pandas as pd
from math import exp, factorial, log

nN = 500
NTU = np.geomspace(0.0001, 400, nN)

class C1A:
    def parametro_1A(N_p,N_r,R):
        N = N_p * N_r
        rho = np.exp(-NTU/N)
        lmbda = R * N_r * (1 - rho)
        R_r = N_r * R
        P_r = (1 - np.exp(-lmbda)) / R_r
        P_p = 1 - (1 - P_r) ** N_r
        P = (1 - (1 - P_p * (1 + R)) ** N_p) / (1 + R)
        if R == 1:
            chi = P / (1 - P)
        
        else:
            chi = (1 / (R - 1)) * np.log((1 - P) / (1 - R * P))

        F = chi / NTU
        return F,P
    def array_1A(N_p,N_r,R_list):
        df = pd.DataFrame({})
        for R in R_list:
            df[f'F[{R}]'],df[f'P[{R}]'] = C1A.parametro_1A(N_p,N_r,R)
        return df
    
class C1B1C:
    def parametro_1B1C(caso, R, NTU, N_p, N_r):
        N = N_p * N_r
        rho = np.exp(-NTU / N)
        lambda_val = R * N_r * (1 - rho)
        R_r = N_r * R
        P_r = (1 - np.exp(-lambda_val)) / R_r
        P_p = 1 - (1 - P_r) ** N_r
        Pt_r = P_r * R_r
        theta_I = np.zeros((N_p + 1, N_r + 1))
        tau_I = np.ones((N_p + 1, N_r + 1))
        theta_F = np.zeros((N_p, N_r))
        tau_F = np.zeros((N_p, N_r))
        
        for p in range(N_p):
            for q in range(N_r):
                tau_F[p, q] = Pt_r * theta_I[p, q] + (1 - Pt_r) * tau_I[p, q]
                theta_F[p, q] = (1 - P_r) * theta_I[p, q] + P_r * tau_I[p, q]
                
                if q != N_r - 1:
                    theta_I[p, q + 1] = theta_F[p, q]
            
            for q in range(N_r):
                if p != N_p - 1:
                    if caso == '1B':
                        tau_I[p + 1, q] = tau_F[p, q]
                    elif caso == '1C':
                        tau_I[p + 1, q] = tau_F[p, N_r - 1 - q]
            theta_I[p + 1, 0] = theta_F[p, N_r - 1]
        P = theta_F[N_p - 1, N_r - 1]
        if R == 1:
            chi = P / (1 - P)
        else:
            chi = (1 / (R - 1)) * np.log((1 - P) / (1 - R * P))
        F = chi / NTU
        return P, F
    def array_1B1C(Np,Nr,caso,R_list):
        P = np.zeros((len(R_list), nN))
        F = np.zeros((len(R_list), nN))
        df = pd.DataFrame({})
        for i,R in enumerate(R_list):
            for j in range(nN):
                P[i, j], F[i, j] = C1B1C.parametro_1B1C(caso, R_list[i], NTU[j], Np, Nr)
            df[f'F[{R}]'],df[f'P[{R}]']  = F[i,:] , P[i,:]
        return df

class C2A:
    def factores_2A(Np,Nr,R):
        N = Np * Nr
        rho = np.exp(-NTU / N)
        lmbda = R * Nr * (1 - rho)
        R_r = Nr * R
        P_r = (1 - np.exp(-lmbda)) / R_r
        P_p = 1 - (1 - P_r) ** Nr

        if R == 1:
            P = P_p / (P_p + (1 - P_p) / Np)
            chi = P / (1 - P)
        else:
            P = (1 - ((1 - P_p) / (1 - R * P_p)) ** Np) / (1 - R * ((1 - P_p) / (1 - R * P_p)) ** Np)
            chi = (1 / (R - 1)) * np.log((1 - P) / (1 - R * P))
        F = chi / NTU
        return F,P
    def array_2A(Np,Nr,R):
        df = pd.DataFrame({})
        for R in R:
            df[f'F[{R}]'],df[f'P[{R}]'] = C2A.factores_2A(Np,Nr,R)
        return df
    
class C2B2C:

    def factores_2BC(Np,Nr,R,caso):
        P_x=[]
        F_y=[]
        for NUT in NTU:
            N = Np * Nr
            rho = np.exp(-NUT / N)
            lmbda = R * Nr * (1 - rho)
            R_r = Nr * R
            P_r = (1 - np.exp(-lmbda)) / R_r
            P_p = 1 - (1 - P_r) ** Nr
            Pt_r = P_r * R_r

            theta_F = np.zeros((Np, Nr))
            tau_I = np.ones((Np, Nr))
            tau_F = np.zeros((Np, Nr))
            theta_I = np.zeros((Np, Nr))

            for p in range(Np, 0, -1):
                for q in range(Nr, 0, -1):
                    theta_I[p-1, q-1] = theta_F[p-1, q-1] / (1 - P_r) - (tau_I[p-1, q-1] * P_r) / (1 - P_r)
                    tau_F[p-1, q-1] = Pt_r * theta_I[p-1, q-1] + (1 - Pt_r) * tau_I[p-1, q-1]
                    if q != 1:
                        theta_F[p-1, q-2] = theta_I[p-1, q-1]

                for q in range(1, Nr + 1):
                    if p != 1:
                        if caso == '2B':
                            tau_I[p-2, q-1] = tau_F[p-1, q-1]
                        elif caso == '2C':
                            tau_I[p-2, q-1] = tau_F[p-1, Nr-q]
                        else:
                            tau_I[p-2, q-1] = tau_F[p-1, q-1]

                        theta_F[p-2, Nr-1] = theta_I[p-1, 0]

            P = theta_I[0, 0] / (theta_I[0, 0] - 1)

            if R == 1:
                chi = P / (1 - P)
            else:
                chi = (1 / (R - 1)) * np.log((1 - P) / (1 - R * P))

            F = chi / NUT
            F_y=np.append(F_y,F)
            P_x=np.append(P_x,P)
            
        return F_y,P_x
    

    def array_2B2C(Np,Nr,caso,R_list):
        df= pd.DataFrame({})
        for R in R_list:
            df[f'F[{R}]'],df[f'P[{R}]'] = C2B2C.factores_2BC(Np,Nr,R,caso)
        return df
class C3A3B3C:

    def pignotti_3abc(caso, R, NTU, N_p, N_r):
        N = N_p * N_r
        rho = exp(-NTU / N)
        lambda_ = R * N_r * (1 - rho)
        a = np.zeros((N + 1, N_p, N_r))       
        alpha = np.zeros((N + 1, N_p, N_r))   
        tau = np.ones((N_p, N_r, 2))              
        for p in range(1, N_p + 1):
            s_r = 0
            N_a = np.zeros(N_r)
            N_b = np.zeros(N_r)
            N_c = np.zeros(N_r)

            for q in range(1, N_r + 1):
                if N_p % 2 == 0:
                    i = N_p // 2
                    N_b[q-1] = (i - 1) * N_r - 1 + q
                    N_c[q-1] = N_b[q-1]
                    N_a[q-1] = N_c[q-1] - 1
                    N_alpha = i * N_r - 1
                    N_beta = N_alpha
                    N_gamma = N_beta
                else:
                    i = (N_p + 1) // 2
                    N_b[q-1] = (i - 1) * N_r - 1 + q
                    N_c[q-1] = N_b[q-1]
                    N_a[q-1] = N_c[q-1] - 1
                    N_alpha = (i - 1) * N_r - 1
                    N_beta = N_alpha
                    N_gamma = N_beta

                N_a[q-1] = max(0, N_a[q-1])
                N_b[q-1] = max(0, N_b[q-1])
                N_c[q-1] = max(0, N_c[q-1])
                N_alpha = max(0, N_alpha)
                N_beta = max(0, N_beta)
                N_gamma = max(0, N_gamma)

                if p == 1:
                    tau[0, q-1, 0] = 1

                s_beta = 0
                beta = np.zeros((N + 1, N_p, N_r))
                gamma = np.zeros((N + 1, N_p, N_r))

                for k in range(N_beta + 1):
                    s_beta1 = 0
                    for j in range(k, N_beta + 1):
                        s_beta1 += alpha[j, p-1, q-1] * (factorial(j) * (-1 / (2 * lambda_)) ** (j - k))
                    beta[k, p-1, q-1] = (1 / (2 * factorial(k))) * s_beta1
                    s_beta += beta[k, p-1, q-1]
                    gamma[k, p-1, q-1] = rho * alpha[k, p-1, q-1] + (1 - rho) * beta[k, p-1, q-1]

                    if q < N_r:
                        alpha[k, p-1, q] = gamma[k, p-1, q-1]

                s_b = 0
                b = np.zeros((N + 1, N_p, N_r))
                c = np.zeros((N + 1, N_p, N_r))

                for k in range(int(N_b[q-1]) + 1):
                    if k >= 1:
                        b[k, p-1, q-1] = (lambda_ * a[k-1, p-1, q-1]) / k
                    else:
                        b[0, p-1, q-1] = tau[p-1, q-1, 0] - beta[0, p-1, q-1]

                    s_b += b[k, p-1, q-1]
                    c[k, p-1, q-1] = rho * a[k, p-1, q-1] + (1 - rho) * b[k, p-1, q-1]

                    if q < N_r:
                        a[k, p-1, q] = c[k, p-1, q-1]

                tau[p-1, q-1, 1] = exp(-lambda_) * s_b + exp(lambda_) * s_beta
                s_r += tau[p-1, q-1, 1]

            tau_F = (1 / N_r) * s_r

            for q in range(1, N_r + 1):
                if p != N_p:
                    if caso == '3A':
                        tau[p, q-1, 0] = tau_F
                    elif caso == '3B':
                        tau[p, q-1, 0] = tau[p-1, q-1, 1]
                    elif caso == '3C':
                        tau[p, q-1, 0] = tau[p-1, N_r-q, 1]
                    else:
                        tau[p, q-1, 0] = tau_F

            if p != N_p:
                for k in range(N_alpha + 1):
                    s_alpha = 0
                    for j in range(k, N_alpha + 1):
                        s_alpha += c[j, p-1, N_r-1] * (factorial(j) / factorial(j - k))
                    alpha[k, p, 0] = (-1)**k * (exp(-lambda_) / factorial(k)) * s_alpha

                for k in range(int(N_a[q-1]) + 1):
                    s_a = 0
                    for j in range(k, int(N_a[q-1]) + 1):
                        s_a += gamma[j, p-1, N_r-1] * (factorial(j) / factorial(j - k))
                    a[k, p, 0] = (-1)**k * (exp(lambda_) / factorial(k)) * s_a

        P = (1 - tau_F) / R
        if R == 1:
            chi = P / (1 - P)
        else:
            chi = (1 / (R - 1)) * log((1 - P) / (1 - R * P))

        F = chi / NTU
        return F, P

    def array_3A3B3C( N_p, N_r,caso,R_list):
        F = np.zeros((len(R_list),nN))
        P = np.zeros((len(R_list),nN))
        df = pd.DataFrame({})
        for j,R  in enumerate(R_list):
            for i,NUT in enumerate(NTU):
                F[j,i],P[j,i] = C3A3B3C.pignotti_3abc(caso, R, NUT, N_p, N_r)
                
            df[f'F[{R}]'],df[f'P[{R}]']  = F[j,:] , P[j,:]
        return df
    




