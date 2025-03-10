function y = pignotti_4a(caso, R, NTU, N_p, N_r)

N=N_p*N_r;
rho=exp(-NTU/N);
lambda=R*N_r*(1-rho);

tau_F(1)=1;
for k=0:N
    a(k+1,1,1)=0;
    alpha(k+1,1,1)=0;
end

for p=1:N_p
    tau(p,1)=1;
    for l=1:2
        s_r=0;
        for q=1:N_r
            if (mod(N_p,2) == 0)
                i=N_p/2;
                N_b(q)=(i-1)*N_r-1+q;
                N_c(q)=N_b(q);
                N_a(q)=N_c(q)-1;
                N_alpha=i*N_r-1;
                N_beta=N_alpha;
                N_gamma=N_beta;
            else
                i=(N_p+1)/2;
                N_b(q)=(i-1)*N_r-1+q;
                N_c(q)=N_b(q);
                N_a(q)=N_c(q)-1;
                N_alpha=(i-1)*N_r-1;
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
                for j=k:N_beta
                    s_beta1=s_beta1+(alpha(j+1,p,q))*(factorial(j)*(-1/(2*lambda))^(j-k));
                end
                beta(k+1,p,q)=(1/(2*factorial(k)))*s_beta1;
                s_beta(p,q)=s_beta(p,q)+beta(k+1,p,q);
                gamma(k+1,p,q)=rho*alpha(k+1,p,q)+(1-rho)*beta(k+1,p,q);
                if (q~=N_r)
                    alpha(k+1,p,q+1)=gamma(k+1,p,q);  
                end
            end
            
            for k=0:N_a(q)
                s_beta1=0;
                for j=k:N_beta
                    s_beta1=s_beta1+(alpha(j+1,p,q))*(factorial(j)*(-1/(2*lambda))^(j-k));
                end
                beta(k+1,p,q)=(1/(2*factorial(k)))*s_beta1;
                gamma(k+1,p,q)=rho*alpha(k+1,p,q)+(1-rho)*beta(k+1,p,q);
                if (q~=N_r)
                    alpha(k+1,p,q+1)=gamma(k+1,p,q);  
                end
            end
        
            s_b2(p,q)=0;
            for k=0:N_b(q)
                a1(k+1,1)=0;
                a2(k+1,p,1)=a(k+1,p,1);
                if (k >= 1)
                    b(k+1,p,q)=(lambda*a(k,p,q))/k;
                    b1(k+1,q)=(lambda*a1(k,q))/k;
                    b2(k+1,p,q)=(lambda*a2(k,p,q))/k;
                else
                    b(1,p,q)=tau(p,1)-beta(1,p,q);
                    b1(1,q)=1;
                    b2(1,p,q)=-beta(1,p,q);
                end
                s_b2(p,q)=s_b2(p,q)+b2(k+1,p,q);
                c(k+1,p,q)=rho*a(k+1,p,q)+(1-rho)*b(k+1,p,q);
                c1(k+1,q)=rho*a1(k+1,q)+(1-rho)*b1(k+1,q);
                c2(k+1,p,q)=rho*a2(k+1,p,q)+(1-rho)*b2(k+1,p,q);
                if (q~=N_r)
                    a(k+1,p,q+1)=c(k+1,p,q);
                    a1(k+1,q+1)=c1(k+1,q);
                    a2(k+1,p,q+1)=c2(k+1,p,q);
                end
            end
        end
    
        if (p~=N_p)
            for k=0:N_alpha
                s_alpha=0;
                for j=k:N_alpha
                    s_alpha=s_alpha+(c(j+1,p,N_r)*(factorial(j)/factorial(j-k)));
                end
                alpha(k+1,p+1,1)=((-1)^k)*((exp(-lambda))/factorial(k))*s_alpha;
            end
            for k=0:N_a(q)
                s_a=0;
                for j=k:N_a(q)
                    s_a=s_a+(gamma(j+1,p,N_r)*(factorial(j)/factorial(j-k)));
                end
                a(k+1,p+1,1)=((-1)^k)*((exp(lambda))/factorial(k))*s_a;
            end
        end
    
        s_g(p)=0;
        s_b1(p)=0;
        for q=1:N_r
            s_g(p)=s_g(p)+(exp(-lambda)*s_b2(p,q)+exp(lambda)*s_beta(p,q));
            for k=0:q-1
                s_b1(p)=s_b1(p)+b1(k+1,q);
            end
        end
    
        f(p)=(exp(-lambda)/N_r)*s_b1(p);
        g(p)=(1/N_r)*(s_g(p));
        tau(p,1)=(tau_F(p)-g(p))/f(p);
        tau_F(p+1)=tau(p,1);
    end
end

P=(tau(N_p,1)-1)/(R*tau(N_p,1));
if (R == 1)
    chi=P/(1-P);
else
    chi=(1/(R-1))*log((1-P)/(1-R*P));
end
F=chi/NTU;

y=[P, F];