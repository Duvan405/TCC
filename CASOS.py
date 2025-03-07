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
    
def pignotti_4bc(caso, R, NTU, N_p, N_r):
    N = N_p * N_r
    rho:float = exp(-NTU / N)
    lambda_:float = R * N_r * (1 - rho)

    a = np.zeros((N + 1, N_p,N))
    alpha = np.zeros((N + 1, N+1, N_r+1))
    tau = np.zeros((N_p+1, N_r+1, 2))
    
    
    C = np.zeros((N_r, N_r))
    B = np.zeros((N_r, 1))
    
    for q in range(1,N_r+1):
        tau[N_p - 1, q-1, 0] = 1

    for l in range(1,3):
        b = np.zeros((N+1, N_p, N_r))
        c = np.zeros((N+1, N_p, N_r))
        for j in range(1,N_r+1):
            
            bet = np.zeros((N+1, N_p, N_r+1))
            for p in range(1,N_p+1):
                N_b = np.zeros(N_r)
                N_a = np.zeros(N_r)
                N_c = np.zeros(N_r)
                s_b = np.zeros((N_p, N_r))
                for q in range(1,N_r+1):
                    if l == 1 and p == 1 and N_p != 1:
                        if q != j:
                            tau[0, q-1, 0] = 0
                        else:
                            tau[0, j-1, 0] = 1

                    if l == 1:
                        tau[p, q-1, 0] = 1

                    if N_p % 2 == 0:
                        iN = N_p / 2
                        N_alpha =  iN  * N_r - 1
                    else:
                        iN = (N_p + 1) / 2
                        N_alpha =  (iN - 1) * N_r - 1

                    N_b[q-1] =  (iN - 1) * N_r - 1 + q
                    N_c[q-1] = N_b[q-1]
                    N_a[q-1] = N_c[q-1] - 1
                    N_beta = N_alpha
                  

                    if N_a[q-1]<0:
                        N_a[q-1] = 0
                    if N_b[q-1]<0:
                        N_b[q-1]= 0
                        N_b[q-1]= 0
                    if N_alpha<0:
                        N_alpha=0
                        N_beta=0
                        

                    s_beta = np.zeros((N_p, N_r))
                    
                    gamma = np.zeros((N+1, N+2, N_r+1))
                    for k in range(int(N_beta) + 1):
                        s_beta1 = 0
                        for j1 in range(k, int(N_beta + 1)):
                            s_beta1 += alpha[j1, p-1, q-1] * (factorial(j1) * (-1 / (2 * lambda_)) ** (j1 - k))
                        bet[k, p-1, q-1] = (1 / (2 * factorial(k))) * s_beta1
                        s_beta[p-1, q-1] += bet[k, p-1, q-1]
                        gamma[k, p-1, q-1] = rho * alpha[k, p-1, q-1] + (1 - rho) * bet[k, p-1, q-1]

                        if q != N_r :
                            alpha[k, p-1, q ] = gamma[k, p-1, q-1]
                    
                    for k in range(0,int(N_a[q-1]+1)):
                        s_beta1=0
                        for j1 in range(k,int(N_beta)):
                            s_beta1+=(alpha[j1,p-1,q-1])*(factorial(j1)*(-1/(2*lambda_))**(j1-k))

                        bet[k,p-1,q-1]=(1/(2*factorial(k)))*s_beta1
                        gamma[k,p-1,q-1]=rho*alpha[k,p-1,q-1]+(1-rho)*bet[k,p-1,q-1]
                        if q!=N_r:
                            alpha[k,p-1,q]=gamma[k,p-1,q-1]  

                    
        
                    
                    for k in range(int(N_b[q-1]) + 1):
                        if k >= 1:
                            b[k, p-1, q-1] = (lambda_ * a[k - 1, p-1, q-1]) / k
                            s_b[p-1, q-1] += b[k, p-1, q-1]
                        else:
                            b[0, p-1, q-1] = tau[p-1, q-1, 0] - bet[0, p-1, q-1]

                        c[k, p-1, q-1] = rho * a[k, p-1, q-1] + (1 - rho) * b[k, p-1, q-1]

                        if q != N_r :
                                a[k, p-1, q ] = c[k, p-1, q-1]
                                
                #!!!!!!!!!!!!!!!!!!!! fin q
                if p != N_p:
                    for k in range(0,int(N_alpha + 1)):
                        s_alpha = 0
                        for j1 in range(k, int(N_alpha + 1)):
                            s_alpha += c[j1, p-1, N_r - 1] * (factorial(j1) / factorial(j1 - k))
                        alpha[k, p , 0] = ((-1) ** k) * (exp(-lambda_) / factorial(k)) * s_alpha

                    for k in range(0,int(N_a[q-1]) + 1):
                        s_a = 0
                        for j1 in range(k, int(N_a[q-1]) + 1):
                            s_a += gamma[j1, p-1, N_r - 1] * (factorial(j1) / factorial(j1 - k))
                        a[k, p , 0] = (-1) ** k * (exp(lambda_) / factorial(k)) * s_a

                    for q in range(1,N_r+1):
                        s_beta[p,q-1] = 0  
                        for k in range(0,int(N_beta+1)):
                            s_beta1=0
                            for j1 in range(k,int(N_beta+1)):
                                s_beta1+=(alpha[j1,p,q-1])*(factorial(j1)*(-1/(2*lambda_))**(j1-k))
                            
                            bet[k,p,q-1]=(1/(2*factorial(k)))*s_beta1
                            s_beta[p,q-1]=s_beta[p,q-1]+bet[k,p,q-1]
                            gamma[k,p,q-1]=rho*alpha[k,p,q-1]+(1-rho)*bet[k,p,q-1]
                            if q!=N_r:
                                alpha[k,p,q]=gamma[k,p,q-1] 

                        for l1 in range (1,3):
                            s_b[p,q-1] = 0
                            for k in range(0,int(N_b[q-1]+1)):
                                if k>=1:
                                    b[k,p,q-1]=(lambda_*a[k-1,p,q-1])/k
                                    s_b[p,q-1]+=b[k,p,q-1]
                                else:
                                    b[0,p,q-1]=tau[p,q-1,0]-bet[0,p,q-1]
            
                                c[k,p,q-1]=rho*a[k,p,q-1]+(1-rho)*b[k,p,q-1]
                                if q!=N_r:
                                    a[k,p,q]=c[k,p,q-1]
                                
                            
                            tau[p,q-1,0]=exp(lambda_)*tau[p-1,q-1,0]-exp(2*lambda_)*s_beta[p,q-1]+bet[0,p,q-1]-s_b[p,q-1];
                        


            for p in range(1,N_p+1):
                if p != N_p :
                    for q in range(1,N_r+1):    
                        if caso == '4B':
                            tau[p, q-1, 1] = tau[p-1, q-1, 0]
                            
                        elif caso == '4C':
                            tau[p, q-1, 1] = tau[p-1, N_r - q, 0]
                        else:
                            tau[p, q-1, 1] = tau[p-1, q-1, 0]
            
            s_bi = np.zeros(N_r)
            s_betai = np.zeros(N_r)
            if N_p != 1 and l == 1:
                
                for i in range(1,N_r+1):
                    
                    for k in range(0,int(N_beta+1)):
                        s_betai[i-1] =s_betai[i-1] +  bet[k, N_p - 1, i-1]
                        
                    for k in range(1,int(N_b[i-1]+1)):
                        s_bi[i-1] += b[k, N_p - 1, i-1]
                    B[i-1,0] = 1
                    x = tau[N_p - 2, i-1, 0]
                    z = s_betai[i-1] 
                    w = bet[0, N_p - 1, i-1] 
                    y = s_bi[i-1]

                    C[i-1, j-1] = exp(lambda_) * tau[N_p - 2, i-1, 0] - exp(2 * lambda_) * s_betai[i-1] + np.mean(bet[0, N_p - 1, i-1]) - s_bi[i-1]
                    tau[N_p-1, i-1, 0] = C[i-1,0]

        if N_p!=1 and l==1:
            try:
                
                Cf = np.linalg.inv(C) @ B
            except np.linalg.LinAlgError:
                #print("La matriz C es singular. No se puede calcular su inversa.")
                Cf = np.linalg.pinv(C) @ B  # Usar pseudo-inversa como alternativa
            for j in range(1,N_r+1):
                tau[0,j-1,0]=Cf[j-1]



    sb2 = 0
    
    for q in range(1,N_r+1):
        sb1=0    
        for k in range(0,q):
            sb1 +=  b[k][0][q-1]
        
        tau[0, q-1, 1] = exp(-lambda_) * sb1
        
        sb2 = sb2 + tau[0, q-1, 1]

    tau_F = (1 / N_r) * sb2

    P = (1 - tau_F) / R
    if R == 1:
        chi = P / (1 - P)
    else:
        try:

            chi = (1 / (R - 1)) * log((1 - P) / (1 - R * P))
        except:
            chi=0
    F = chi / NTU

    return P, F

def caso_4A(R,NTU,N_p,N_r):
    # Cálculos iniciales
    N = N_p * N_r
    rho = exp(-NTU / N)
    lambda_ = R * N_r * (1 - rho)
    
    
    tau_F = np.zeros(N_p+1)
    tau_F[0] = 1
    alpha = np.zeros((N + 1, N_p + 1, N_r + 1))
    a = np.zeros((N+1,N_p+1,N_r + 1))
    a1= np.zeros((N+2,N_r+1))
    a2= np.zeros((N+1,N_p+1,N_r))
    b = np.zeros((N+1,N_p+1,N_r + 1))
    b1 = np.zeros((N+1,N_r+1))
    b2 = np.zeros((N+1,N_p+1 ,N_r+1))
    c = np.zeros((N+1,N_p+1,N_r + 1))
    c1 = np.zeros((N+1,N_r+1))
    c2 = np.zeros((N+1,N_p+1,N_r+1))
    beta = np.zeros((N + 1, N_p + 1, N_r + 1))
    tau = np.zeros((N_p , 1))
    s_b2 = np.zeros((N_p,N_r))
    N_b = np.zeros(N_r)
    N_c = np.zeros(N_r)
    N_a = np.zeros(N_r)
    f = np.zeros(N_p + 1)
    g = np.zeros(N_p + 1)
    s_g = np.zeros(N_p )
    s_b1 = np.zeros(N_p )
    
    
    for p in range(1, N_p + 1):
        tau[p-1, 0] = 1
        for l in range(1, 3):
            
            
            s_beta = np.zeros((N_p + 1, N_r + 1))
            gamma = np.zeros((N + 1, N + 2, N_r + 1))
            for q in range(1, N_r + 1):  
                  
                
                if N_p % 2 == 0:
                    i = N_p / 2
                    N_b[q-1] = (i - 1) * N_r - 1 + q
                    N_c[q-1] = N_b[q-1]
                    N_a[q-1] = N_c[q-1] - 1
                    N_alpha = i * N_r - 1
                    N_beta = N_alpha
                    N_gamma=N_beta
                   
                else:
                    i = (N_p + 1) / 2
                    N_b[q-1] = (i - 1) * N_r - 1 + q
                    N_c[q-1] = N_b[q-1]
                    N_a[q-1] = N_c[q-1] - 1
                    N_alpha = (i - 1) * N_r - 1
                    N_beta = N_alpha
                    N_gamma=N_beta
                

                if N_a[q-1] < 0:
                    N_a[q-1] = 0

                if N_b[q-1] < 0:
                    N_b[q-1] = 0
                    N_c[q-1] = 0
                
                if N_alpha < 0:
                    N_alpha = 0
                    N_beta = 0
                    N_gamma = 0
                
                s_beta[p,q] = 0  
                for k in range(0, int(N_beta + 1)):
                    s_beta1 = 0
                    for j in range(k, int(N_beta + 1)):
                        s_beta1 += alpha[j, p-1, q-1] * factorial(j) * (-1 / (2 * lambda_)) ** (j - k)
                    beta[k, p-1, q-1] = (1 / (2 * factorial(k))) * s_beta1
                    s_beta[p-1, q-1] += beta[k, p-1, q-1]
                    gamma[k, p-1, q-1] = rho * alpha[k, p-1, q-1] + (1 - rho) * beta[k, p-1, q-1]
                    if q != N_r:
                        alpha[k, p-1, q ] = gamma[k, p-1, q-1]

                for k in range(0,int( N_a[q-1] + 1)):
                    s_beta1 = 0
                    for j in range(k, int(N_beta + 1)):
                        s_beta1 += alpha[j, p-1, q-1] * factorial(j) * (-1 / (2 * lambda_)) ** (j - k)
                    beta[k, p-1, q-1] = (1 / (2 * factorial(k))) * s_beta1
                    gamma[k, p-1, q-1] = rho * alpha[k, p-1, q-1] + (1 - rho) * beta[k, p-1, q-1]
                    if q != N_r:
                        alpha[k, p-1, q ] = gamma[k, p-1, q-1]


                
                s_b2[p-1,q-1] = 0

                for k in range(0, int(N_b[q-1] + 1)):
                    a1[k+1,1]=0
                    a2[k, p-1, 0] = a[k, p-1, 0]
                    
                    if k >= 1:
                        b[k, p-1, q-1] = (lambda_ * a[k - 1, p-1, q-1]) / k
                        b1[k, q-1] = (lambda_ * a1[k - 1, q-1]) / k
                        b2[k, p-1, q-1] = (lambda_ * a2[k - 1, p-1, q-1]) / k
                    else:
                        b[0, p-1, q-1] = tau[p-1, 0] - beta[0, p-1, q-1]
                        b1[0, q-1] = 1
                        b2[0, p-1, q-1] = -beta[0, p-1, q-1]
                    s_b2[p-1, q-1] += b2[k, p-1, q-1]
                    c[k, p-1, q-1] = rho * a[k, p-1, q-1] + (1 - rho) * b[k, p-1, q-1]
                    c1[k, q-1] = rho * a1[k, q-1] + (1 - rho) * b1[k, q-1]
                    c2[k, p-1, q-1] = rho * a2[k, p-1, q-1] + (1 - rho) * b2[k, p-1, q-1]
                    if q != N_r:
                        a[k, p-1, q ] = c[k, p-1, q-1]
                        a1[k, q ] = c1[k, q-1]
                        a2[k, p-1, q] = c2[k, p-1, q-1]

            if p != N_p:
                for k in range(0, int(N_alpha + 1)):
                    s_alpha = 0
                    for j in range(k, int(N_alpha + 1)):
                        s_alpha += c[j, p-1, N_r-1] * (factorial(j) / factorial(j - k))
                    alpha[k, p , 0] = ((-1) ** k) * (exp(-lambda_) / factorial(k)) * s_alpha

                for k in range(0, int(N_a[q-1] + 1)):
                    s_a = 0
                    for j in range(k, int(N_a[q-1] + 1)):
                        s_a += gamma[j, p-1, N_r-1] * (factorial(j) / factorial(j - k))
                    a[k, p , 0] = ((-1) ** k) * (exp(lambda_) / factorial(k)) * s_a
            
            
            s_g[p-1]=0
            s_b1[p-1] = 0
            for q in range(1, N_r + 1):
                s_g[p-1] += (exp(-lambda_) * s_b2[p-1, q-1] + exp(lambda_) * s_beta[p-1, q-1])
                for k in range(0, q):
                    s_b1[p-1] += b1[k, q-1]
            
            
            f[p-1] = (exp(-lambda_) / N_r) * s_b1[p-1]
            g[p-1] = (1 / N_r) * s_g[p-1]
            tau[p-1, 0] = (tau_F[p-1] - g[p-1]) / f[p-1]
            tau_F[p]=tau[p-1, 0]

    # Cálculos finales
    P = (tau[N_p-1, 0] - 1) / (R * tau[N_p-1, 0])
    if R == 1:
        chi = P / (1 - P)
    else:
        chi = (1 / (R - 1)) * log((1 - P) / (1 - R * P))

    F = chi / NTU
    return F,P



