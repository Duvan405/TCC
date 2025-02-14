# **Artigo Navarro et al. (2010)**  
O artigo apresenta uma análise da relação **Efetividade-NTU** para serpentinas de ar utilizadas em sistemas de **ar-condicionado e refrigeração**. O estudo utiliza um **programa de simulação baseado no volume de controle** para avaliar a efetividade térmica de serpentinas de geometria e arranjo de fluxo complexos, validando os resultados com **correlações de forma fechada**.

---

## **Correlação Principal**  

A efetividade térmica $`(\varepsilon)`$ é definida pela relação:

```math
\varepsilon = \frac{q}{q_{\text{max}}}
```

onde:
- $`( q )`$ é a taxa de transferência de calor real;
- $`( q_{	ext{max}} )`$ é a transferência máxima possível de calor;
- $`( C_{\min} )`$ é a menor capacidade térmica entre os fluidos;
- $`( T_{h,i} )`$ e $`( T_{c,i} )`$ são as temperaturas de entrada dos fluidos quente e frio, respectivamente.

A relação entre NTU e efetividade para diferentes configurações pode ser expressa por:

```math
NTU = \frac{UA}{C_{\min}}
```

onde:
- $`( U )`$ é o coeficiente global de transferência de calor;
- $`( A )`$ é a área total de troca térmica da serpentina.

Além disso, foram analisadas equações empíricas para **diferentes arranjos de fluxo cruzado**, considerando múltiplas fileiras de tubos.

---

## **Modelos Implementados**  

1. **Equações Governantes**  
   - O fluido no interior dos tubos é chamado de "fluido do tubo" e o ar circula externamente em um **arranjo de fluxo cruzado**.
   - O modelo divide a serpentina em **pequenos volumes finitos**, chamados de **elementos do tubo**.
   - A variação de temperatura ao longo do trocador é descrita pela equação:

```math
\frac{dT}{dx} = \frac{q}{m c_p}
```

2. **Procedimento Computacional**  
   - O programa de simulação lê as **propriedades geométricas da serpentina** e os **parâmetros de entrada**, como NTU e capacidade térmica.
   - A solução do sistema de equações diferenciais é obtida iterativamente para determinar as temperaturas de saída dos fluidos.
   - A efetividade térmica da serpentina é então calculada para cada configuração analisada.

3. **Configurações de Fluxo Analisadas**  
   - Diferentes números de **fileiras de tubos** e circuitos internos.
   - Comparação entre arranjos **misto-não misto** e **totalmente misturados**.
   - Avaliação do impacto do **número de fileiras** no desempenho térmico.

---

## **Resultados e Conclusões**  

- O modelo numérico foi validado com **correlações clássicas para fluxo cruzado** e apresentou **pequenos erros relativos**.
- Foi determinado que as **correlações existentes são adequadas apenas para serpentinas com até 4 fileiras**.
- Para serpentinas com **mais de 5 fileiras**, as **correlações fechadas apresentam desvios superiores a 10%**, tornando a simulação necessária.
- O estudo confirmou que **aumentar o número de fileiras melhora a efetividade térmica** da serpentina.

---

>[!Important]  
>* As correlações clássicas de **Efetividade-NTU** podem apresentar erros para serpentinas de geometria complexa.  
>* O modelo computacional desenvolvido fornece resultados mais precisos para serpentinas de **ar-condicionado e refrigeração**.  

>[!tip]  
>Para otimizar o desempenho térmico, recomenda-se ajustar **o número de fileiras e circuitos internos**.  

>[!Warning]  
>Os erros em **Efetividade-NTU** podem impactar o cálculo das propriedades térmicas do ar em experimentos.  

>[!Note]  
>O estudo destaca a importância do uso de modelos numéricos para o projeto de serpentinas com **vários circuitos e fileiras**.  

---

## **Referências**  

1. Navarro, H.A., Cabezas-Gómez, L., & Zoghbi Filho, J.R.B., *Effectiveness - NTU Data and Analysis for Air Conditioning and Refrigeration Air Coils*, J. Braz. Soc. Mech. Sci. & Eng., 2010.  
2. Kays, W.M., London, A.L., *Compact Heat Exchangers*, McGraw-Hill, 1998.  
3. Shah, R.K., Mueller, A.C., *Fundamentals of Heat Exchanger Design*, Wiley, 2003.  
4. Pignotti, A., Cordero, G.O., *Mean Temperature Difference in Multipass Crossflow*, ASME J. Heat Transfer, 1983.  
5. Stevens, R.A., Fernandez, J., Woolf, J.R., *Mean Temperature Difference in Crossflow Heat Exchangers*, ASME, 1957.  
