% clear all
% close all
% clc
% 
% caso='4B';
% R=0.1;
% NTU=0.2;
% N_p=2;
% N_r=25;

function y = pignotti_4bc(caso, R, NTU, N_p, N_r)

N=N_p*N_r;
rho=exp(-NTU/N);
lambda=R*N_r*(1-rho);

for k=0:N
    a(k+1,1,1)=0;
    alpha(k+1,1,1)=0;
end
for q=1:N_r
    tau(N_p,q,1)=1;
end

for l=1:2
    for j=1:N_r
        for p=1:N_p
            for q=1:N_r
                if (l==1) && (p==1) && (N_p~=1)
                    if (q~=j)
                        tau(1,q,1)=0;
                    else
                        tau(1,j,1)=1;
                    end
                end
                if (l==1)
                    tau(p+1,q,1)=1;
                end
                if (mod(N_p,2) == 0)
                    iN=N_p/2;
                    N_b(q)=(iN-1)*N_r-1+q;
                    N_c(q)=N_b(q);
                    N_a(q)=N_c(q)-1;
                    N_alpha=iN*N_r-1;
                    N_beta=N_alpha;
                    N_gamma=N_beta;
                else
                    iN=(N_p+1)/2;
                    N_b(q)=(iN-1)*N_r-1+q;
                    N_c(q)=N_b(q);
                    N_a(q)=N_c(q)-1;
                    N_alpha=(iN-1)*N_r-1;
                    N_beta=N_alpha;
                    N_gamma=N_beta;
                end
                if (N_a(q) < 0)
                    N_a(q)=0;
                end
                if (N_b(q) < 0)
                    N_b(q)=0;
                    N_c(q)=0;
                end
                if (N_alpha < 0)
                    N_alpha=0;
                    N_beta=0;
                    N_gamma=0;
                end
                                        
                s_beta(p,q)=0;
                for k=0:N_beta
                    s_beta1=0;
                    for j1=k:N_beta
                        s_beta1=s_beta1+(alpha(j1+1,p,q))*(factorial(j1)*(-1/(2*lambda))^(j1-k));
                    end
                    beta(k+1,p,q)=(1/(2*factorial(k)))*s_beta1;
                    s_beta(p,q)=s_beta(p,q)+beta(k+1,p,q);
                    gamma(k+1,p,q)=rho*alpha(k+1,p,q)+(1-rho)*beta(k+1,p,q);
                    if (q~=N_r)
                        alpha(k+1,p,q+1)=gamma(k+1,p,q);  
                    end
                end
                
%               Cálculo de gamma para o proximo passo
                for k=0:N_a(q)
                    s_beta1=0;
                    for j1=k:N_beta
                        s_beta1=s_beta1+(alpha(j1+1,p,q))*(factorial(j1)*(-1/(2*lambda))^(j1-k));
                    end
                    beta(k+1,p,q)=(1/(2*factorial(k)))*s_beta1;
                    gamma(k+1,p,q)=rho*alpha(k+1,p,q)+(1-rho)*beta(k+1,p,q);
                    if (q~=N_r)
                        alpha(k+1,p,q+1)=gamma(k+1,p,q);  
                    end
                end
                   
                s_b(p,q)=0;
                for k=0:N_b(q)
                    if (k>=1)
                        b(k+1,p,q)=(lambda*a(k,p,q))/k;
                        s_b(p,q)=s_b(p,q)+b(k+1,p,q);
                    else
                        b(1,p,q)=tau(p,q,1)-beta(1,p,q);
                    end
                    c(k+1,p,q)=rho*a(k+1,p,q)+(1-rho)*b(k+1,p,q);
                    if (q~=N_r)
                        a(k+1,p,q+1)=c(k+1,p,q);
                    end
                end
            end
        
            if (p~=N_p)
                for k=0:N_alpha
                    s_alpha=0;
                    for j1=k:N_alpha
                        s_alpha=s_alpha+(c(j1+1,p,N_r)*(factorial(j1)/factorial(j1-k)));
                    end
                    alpha(k+1,p+1,1)=((-1)^k)*((exp(-lambda))/factorial(k))*s_alpha;
                end
                for k=0:N_a(q)
                    s_a=0;
                    for j1=k:N_a(q)
                        s_a=s_a+(gamma(j1+1,p,N_r)*(factorial(j1)/factorial(j1-k)));
                    end
                    a(k+1,p+1,1)=((-1)^k)*((exp(lambda))/factorial(k))*s_a;
                end
                
                for q=1:N_r
                    s_beta(p+1,q)=0;
                    for k=0:N_beta
                        s_beta1=0;
                        for j1=k:N_beta
                            s_beta1=s_beta1+(alpha(j1+1,p+1,q))*(factorial(j1)*(-1/(2*lambda))^(j1-k));
                        end
                        beta(k+1,p+1,q)=(1/(2*factorial(k)))*s_beta1;
                        s_beta(p+1,q)=s_beta(p+1,q)+beta(k+1,p+1,q);
                        gamma(k+1,p+1,q)=rho*alpha(k+1,p+1,q)+(1-rho)*beta(k+1,p+1,q);
                        if (q~=N_r)
                            alpha(k+1,p+1,q+1)=gamma(k+1,p+1,q);  
                        end
                    end
                    for l1=1:2
                        s_b(p+1,q)=0;
                        for k=0:N_b(q)
                            if (k>=1)
                                b(k+1,p+1,q)=(lambda*a(k,p+1,q))/k;
                                s_b(p+1,q)=s_b(p+1,q)+b(k+1,p+1,q);
                            else
                                b(1,p+1,q)=tau(p+1,q,1)-beta(1,p+1,q);
                            end
                            c(k+1,p+1,q)=rho*a(k+1,p+1,q)+(1-rho)*b(k+1,p+1,q);
                            if (q~=N_r)
                                a(k+1,p+1,q+1)=c(k+1,p+1,q);
                            end
                        end
                        tau(p+1,q,1)=exp(lambda)*tau(p,q,1)-exp(2*lambda)*s_beta(p+1,q)+beta(1,p+1,q)-s_b(p+1,q);
                    end
                end
            end
        end
        
        for p=1:N_p
            if (p~=N_p)
                for q=1:N_r
                    switch caso
                        case '4B'
                            tau(p+1,q,2)=tau(p,q,1);
                        case '4C'
                            tau(p+1,q,2)=tau(p,N_r+1-q,1);
                        otherwise
                            tau(p+1,q,2)=tau(p,q,1);
                    end
                end
            end
        end
        
        if (N_p~=1) && (l==1)
            for i=1:N_r
                s_betai(i)=0;
                s_bi(i)=0;
                for k=0:N_beta
                    s_betai(i)=s_betai(i)+beta(k+1,N_p,i);
                end
                for k=1:N_b(i)
                    s_bi(i)=s_bi(i)+b(k+1,N_p,i);
                end
                B(i,1)=1;
                C(i,j)=exp(lambda)*tau(N_p-1,i,1)-exp(2*lambda)*s_betai(i)+beta(1,N_p,i)-s_bi(i);
                tau(N_p,i,1)=C(i,1);
            end
        end
    end
    
    if (N_p~=1) && (l==1)
        Cf=inv(C)*B;
        for j=1:N_r
            tau(1,j,1)=Cf(j);
        end
    end
end

sb2=0;
for q=1:N_r
    sb1=0;
    for k=0:q-1
        sb1=sb1+b(k+1,1,q);
    end
    tau(1,q,2)=exp(-lambda)*sb1;
    sb2=sb2+tau(1,q,2);
end
tau_F=(1/N_r)*sb2;

P=(1-tau_F)/R;
if (R == 1)
    chi=P/(1-P);
else
    chi=(1/(R-1))*log((1-P)/(1-R*P));
end
F=chi/NTU;

y=[P, F];