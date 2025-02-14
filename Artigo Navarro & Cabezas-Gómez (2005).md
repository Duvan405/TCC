# **Artigo Navarro & Cabezas-Gómez (2005)**  
O artigo apresenta uma nova metodologia numérica para o cálculo do desempenho térmico em trocadores de calor de fluxo cruzado. A metodologia proposta permite obter dados de efetividade para diversas configurações padrão e complexas de fluxo, validando os resultados com soluções analíticas.

---

## **Correlação Principal**  

A metodologia numérica baseia-se na divisão do trocador de calor em uma série de pequenas unidades de troca de calor de fluxo cruzado misto-não misto. A efetividade térmica $`(\varepsilon)`$ pode ser expressa pela relação **Efetividade-Número de Unidades de Transferência (e-NTU)**, dada por:

```math
\varepsilon = \frac{q}{q_{\text{max}}}
```

onde:
- $`( q )`$ é a taxa de transferência de calor real;
- $`( q_{	ext{max}} )`$ é a transferência máxima possível de calor;
- $`( C_{\min} )`$ é a menor capacidade térmica entre os dois fluidos;
- $`( T_{h,i} )`$ e $`( T_{c,i} )`$ são as temperaturas de entrada dos fluidos quente e frio, respectivamente.

A expressão para $`( q_{	ext{max}} )`$ é:

```math
q_{	ext{max}} = C_{\min} (T_{h,i} - T_{c,i})
```

A relação entre NTU e efetividade para diferentes configurações de fluxo pode ser determinada por:

```math
NTU = \frac{UA}{C_{\min}}
```

onde:
- $`( U )`$ é o coeficiente global de transferência de calor;
- $`( A )`$ é a área de troca térmica do trocador.

A equação fundamental para a transferência de calor pode ser expressa como:

```math
q = C_{\min} (T_{h,i} - T_{c,i}) (1 - e^{-NTU})
```

Essa equação mostra que a efetividade aumenta com o aumento do NTU, atingindo um valor assintótico.

---

## **Modelos Implementados**  

1. **Governação por Equações Diferenciais**  
   - As equações fundamentais são formuladas para trocadores de calor de fluxo cruzado onde um fluido está misturado e o outro não misturado.  
   - São utilizadas aproximações diferenciais para resolver a variação de temperatura ao longo do trocador.
   - A temperatura ao longo do trocador é determinada pela equação diferencial:

```math
\frac{dT}{dx} = \frac{q}{m c_p}
```

2. **Metodologia Numérica**  
   - O trocador de calor é discretizado em pequenos volumes de controle.
   - Cada volume é tratado como um trocador de calor misto-não misto.
   - A solução do sistema de equações diferenciais é obtida por métodos numéricos iterativos como o **método das diferenças finitas**.
   - O algoritmo é implementado para garantir a convergência dos resultados por meio de refinamento progressivo da malha.
   - A metodologia também considera a influência de variações nos coeficientes de transferência de calor ao longo do trocador.
   - A validação é feita comparando os valores simulados com soluções analíticas conhecidas e benchmarks experimentais.

3. **Configurações de Fluxo Analisadas**  
   - Trocadores de calor com diferentes números de passes e fileiras.
   - Modelagem de circuitos de tubos e padrões complexos de fluxo.
   - Avaliação da influência da geometria e arranjo dos fluidos no desempenho térmico.
   - Comparação entre diferentes arranjos de fluxo cruzado, contracorrente e paralelos para avaliação da eficiência térmica.

---

## **Resultados e Conclusões**  

- Os resultados da simulação foram comparados com equações analíticas existentes e apresentaram **erros muito pequenos**.
- Foram obtidos **novos dados de efetividade** para configurações de fluxo cruzado complexas.
- A metodologia mostrou-se aplicável a trocadores de calor industriais com diferentes configurações.
- A modelagem numérica permite prever **efetividade, NTU e taxa de transferência de calor** para diferentes geometrias.
- O refinamento da malha impacta diretamente na precisão dos cálculos, sendo um fator crítico na convergência dos resultados.
- A metodologia permite a adaptação para diferentes fluidos de trabalho, tornando-se uma ferramenta flexível para projetos térmicos.

---

>[!Important]  
>* A nova abordagem numérica permite obter **dados precisos de efetividade** para trocadores de calor de fluxo cruzado.  
>* A metodologia proposta pode ser aplicada a configurações industriais onde **soluções analíticas são difíceis de obter**.  

>[!tip]  
>Para otimizar um trocador de calor, recomenda-se ajustar **o número de passes e fileiras** para maximizar a efetividade térmica.  

>[!Warning]  
>Embora a modelagem numérica forneça resultados confiáveis, **a precisão depende da discretização do volume de controle**.  

>[!Note]  
>O método proposto amplia os estudos anteriores e fornece **novas soluções para configurações de fluxo cruzado complexas**.  

---

## **Referências**  

1. Th. Bes, *Thermal performance of codirected cross-flow heat exchangers*, Heat Mass Transfer, 1996.  
2. Sekulic, D.P., Shah, R.K., Pignotti, A., *A review of solution methods for determining effectiveness-NTU relationships for heat exchangers with complex flow arrangements*, Appl. Mech. Rev., 1999.  
3. Pignotti, A., Shah, R.K., *Effectiveness-number of transfer units relationships for heat exchanger complex flow arrangements*, Int. J. Heat Mass Transfer, 1992.  
4. Kays, W.M., London, A.L., *Compact Heat Exchangers*, McGraw Hill, 1998.  
5. Shah, R.K., Sekulic, D.P., *Handbook of Heat Transfer*, McGraw Hill, 1998.  
6. Shah, R.K., Pignotti, A., *Thermal analysis of complex cross-flow exchangers in terms of standard configurations*, ASME J. Heat Transfer, 1993.  
