# **Artigo Cabezas-Gómez et al. (2012)**  
O artigo apresenta uma análise teórica de um novo arranjo de fluxo em trocadores de calor de fluxo cruzado, abrangendo várias fileiras de tubos. A performance térmica da configuração proposta é comparada com a de um arranjo típico de fluxo cruzado contracorrente, amplamente utilizado nas indústrias química, de refrigeração, automotiva e de ar-condicionado.

---

## **Correlação Principal**  

A efetividade térmica $`(\varepsilon)`$ pode ser expressa pela relação **Efetividade-Número de Unidades de Transferência (e-NTU)**, dada por:

```math
\varepsilon = \frac{q}{q_{\text{max}}}
```

onde:
- $`( q )`$ é a taxa de transferência de calor real;
- $`( q_{	ext{max}} )`$ é a transferência máxima possível de calor;
- $`( C_{\min} )`$ é a menor capacidade térmica entre os dois fluidos;
- $`( T_{h,i} )`$ e $`( T_{c,i} )`$ são as temperaturas de entrada dos fluidos quente e frio, respectivamente.

A relação entre NTU e efetividade pode ser determinada por:

```math
NTU = \frac{UA}{C_{\min}}
```

onde:
- $`( U )`$ é o coeficiente global de transferência de calor;
- $`( A )`$ é a área de troca térmica do trocador.

Além disso, o estudo também introduz o conceito de **dissipação de entransia**, usada como métrica para avaliar a irreversibilidade do processo térmico.

---

## **Modelos Implementados**  

1. **Equações Governantes**  
   - As equações fundamentais são formuladas para trocadores de calor de fluxo cruzado considerando um fluido misturado e outro não misturado.
   - A equação diferencial que governa a variação de temperatura ao longo do trocador é:

```math
\frac{dT}{dx} = \frac{q}{m c_p}
```

2. **Metodologia Numérica**  
   - O trocador de calor é dividido em um número finito de volumes de controle tridimensionais.
   - Cada elemento é modelado como um trocador de calor misto-não misto.
   - A solução é obtida numericamente por um esquema iterativo de marcha ao longo dos circuitos internos.
   - A dissipação de entransia é determinada por:

```math
DE* = 1 - \varepsilon \left( 1 + \frac{C*}{2} \right)
```

3. **Configurações de Fluxo Analisadas**  
   - Comparação entre o arranjo proposto e o fluxo cruzado contracorrente padrão.
   - Avaliação da influência do número de fileiras de tubos (de 2 a 6 passes).
   - Análise da distribuição do campo de diferença de temperatura (TDF) sobre o desempenho térmico.

---

## **Resultados e Conclusões**  

- O novo arranjo apresentou **maior efetividade térmica** em comparação com o fluxo cruzado contracorrente convencional.
- A redução da **dissipação de entransia** sugere menor irreversibilidade térmica no arranjo proposto.
- A metodologia numérica confirmou que **a uniformidade do campo de diferença de temperatura melhora a performance térmica**.
- Os resultados indicam que o novo arranjo pode ser aplicado a **trocadores de calor em sistemas de refrigeração e automotivos**.

---

>[!Important]  
>* A nova configuração melhora a eficiência térmica em trocadores de calor de fluxo cruzado.  
>* A análise mostra que a uniformidade da diferença de temperatura está diretamente ligada à efetividade térmica.  

>[!tip]  
>Para maximizar o desempenho térmico, recomenda-se ajustar **o número de passes** para reduzir a irreversibilidade térmica.  

>[!Warning]  
>A análise foi baseada apenas na transferência de calor; efeitos de queda de pressão não foram considerados.  

>[!Note]  
>Os resultados reforçam a importância do princípio de uniformidade da diferença de temperatura em trocadores de calor.  

---

## **Referências**  

1. Cabezas-Gómez, L., Navarro, H. A., & Hanriot, S. M., *Thermal performance of multipass parallel- and counter cross-flow heat exchangers*, ASME J. Heat Transfer, 2012.  
2. Guo, Z.-Y., Zhou, S.-Q., & Li, Z.-X., *Uniformity principle of temperature difference field in heat exchangers*, Int. J. Heat Mass Transfer, 2002.  
3. Sekulić, D. P., *The second law quality of energy transformation in a heat exchanger*, ASME J. Heat Transfer, 1990.  
4. Bejan, A., *The concept of irreversibility in heat exchanger design*, ASME J. Heat Transfer, 1977.  
5. Fakheri, A., *Heat exchanger efficiency*, ASME J. Heat Transfer, 2007.  
