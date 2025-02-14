# **Artigo Sekulic (1990)**  
O artigo apresenta uma análise da **qualidade da transformação de energia** em trocadores de calor a partir da **Segunda Lei da Termodinâmica**. A abordagem usa a geração de entropia como uma métrica quantitativa para avaliar a eficiência do processo de troca térmica.

---

## **Correlação Principal**  

A irreversibilidade no processo de troca de calor pode ser quantificada pela **geração de entropia**, dada por:

$$
S = S_{\Delta T} + S_{\Delta P}
$$

onde  $` S_{\Delta T} `$representa a irreversibilidade devido às diferenças de temperatura e $` S_{\Delta P} `$ inclui o efeito da queda de pressão.

Para a troca de calor entre dois fluxos de gás, considerando apenas a diferença de temperatura como fonte de irreversibilidade, a entropia gerada pode ser expressa como:

```math
S_{\Delta T} = (\dot{m} c_p)^2 \left[ \omega \ln\left(1 + \epsilon (T - 1)\right) + \ln\left(1 + \omega e (T - 1)\right) \right]
```

A qualidade da transformação de energia no trocador é quantificada pela **Norma de Reversibilidade da Troca de Calor (HERN)**:

```math
\text{HERN} = 1 - \frac{S}{S_{\text{máx}}}
```

onde $` S_{\text{máx}} `$ representa a maior geração de entropia possível para o sistema.

---

## **Modelos Implementados**  

1. **Qualidade da Transformação de Energia**  
   - A qualidade da troca térmica é expressa como \( HERN \), que varia entre **0** (processo totalmente irreversível) e **1** (reversível).  
   - Esse parâmetro permite comparar diferentes configurações de trocadores de calor.

2. **Correlação com o Número de Unidades de Transferência de Calor (NTU)**  
   - O artigo demonstra que a irreversibilidade pode ser minimizada ajustando o **NTU**, otimizando a relação entre o tamanho do trocador e a qualidade da conversão de energia.

3. **Influência do Tipo de Fluxo**  
   - A análise inclui diferentes arranjos de fluxo, como **contracorrente, cocorrente e fluxo cruzado**, demonstrando que **trocadores de fluxo contracorrente possuem menor geração de entropia**.

---

## **Resultados e Conclusões**  

- A **geração de entropia cresce** à medida que se aumenta a **diferença de temperatura entre os fluxos**.  
- Para um mesmo \( NTU \), a **eficiência de conversão de energia é maior em trocadores contracorrente** em comparação a cocorrente.  
- O método HERN **fornece um critério quantitativo para avaliar e otimizar trocadores de calor**, sendo aplicável a diferentes configurações industriais.  
- A otimização da **relação de capacidades térmicas $` \dot{C} `$** entre os fluidos minimiza a geração de entropia.  

---

>[!Important]  
>* O conceito de **HERN** permite uma avaliação mais refinada da eficiência energética de trocadores de calor.  
>* A análise baseia-se na **Segunda Lei da Termodinâmica**, indo além da eficiência tradicional baseada apenas na Primeira Lei.  

>[!tip]  
>Para um projeto otimizado, o **número de unidades de transferência \( NTU \) e a relação de capacidades térmicas** devem ser ajustados para minimizar a geração de entropia.  

>[!Warning]  
>Minimizar a irreversibilidade pode aumentar o **tamanho físico do trocador de calor**, afetando custos e viabilidade de fabricação.  

>[!Note]  
>Este trabalho expande estudos anteriores, como o de **Bejan (1977)**, e aplica a análise entrópica a **diferentes tipos de trocadores de calor**.  

---

## **Referências**  

1. Bejan, A. *Entropy Generation Through Heat and Fluid Flow*. Wiley, New York, 1982.  
2. Kays, W. M., & London, A. L. *Compact Heat Exchangers*. McGraw-Hill, 1984.  
3. Sekulic, D. P. *Entropy Generation in a Heat Exchanger*. Heat Transfer Engineering, 1986.  
4. Zubair, S. M., et al. *Thermoeconomic Optimization of Heat Exchangers*. ASME, 1987.  
5. London, A. L. *Economics and the Second Law: An Engineering View*. Int. J. Heat and Mass Transfer, 1982.  
6. Hatsopoulos, G. N., & Keenan, J. H. *Principles of General Thermodynamics*. Wiley, 1965.  
