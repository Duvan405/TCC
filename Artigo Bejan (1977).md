
# **Artigo Bejan (1977)**  
O artigo apresenta um método de projeto para trocadores de calor de fluxo contracorrente **gás-gás** baseado no conceito de **irreversibilidade termodinâmica**. A abordagem se diferencia dos métodos tradicionais ao focar na minimização da geração de entropia $`(N_s)`$ ao invés de especificar diretamente a troca de calor e as perdas de carga.

---

## **Correlação Principal**  

A irreversibilidade em sistemas térmicos está relacionada à **potência útil perdida** devido às imperfeições do trocador de calor. O artigo define a taxa de irreversibilidade $`I`$ como:

$$
I = T_0 \\dot{S}
$$

onde $`T_0`$ é a temperatura do ambiente e $$\dot{S}$$  é a taxa de geração de entropia.

A entropia produzida em um trocador de calor de fluxo contracorrente pode ser expressa como:

```math
S = \dot{C}_{\min} \left[ \ln{\left(\frac{T_{1,\text{out}}}{T_{1,\text{in}}}\right)} + \frac{R}{c_{p1}} \ln{\left(\frac{P_{1,\text{out}}}{P_{1,\text{in}}}\right)} \right] +
\dot{C}_{\max} \left[ \ln{\left(\frac{T_{2,\text{out}}}{T_{2,\text{in}}}\right)} + \frac{R}{c_{p2}} \ln{\left(\frac{P_{2,\text{out}}}{P_{2,\text{in}}}\right)} \right]
```
onde $`\dot{C}`$ representa a taxa de capacidade térmica e $` P `$ é a pressão absoluta.

A irreversibilidade pode ser normalizada como o **Número de Unidades de Geração de Entropia** $`N_s `$:

$$
N_s = \\frac{S}{\\dot{C}_{\\min}}
$$

O artigo também discute como minimizar $` N_s `$ variando os parâmetros geométricos do trocador de calor.

---

## **Modelos Implementados**  

1. **Troca térmica com irreversibilidade mínima**  
   - O método tradicional de projeto especifica a quantidade de calor transferida entre os fluidos e as perdas de carga permitidas.
   - O método de **minimização de $`( N_s )`$** define a irreversibilidade desejada como entrada, tornando a área de troca térmica e a potência de bombeamento variáveis de saída.

2. **Cálculo da irreversibilidade com base na geometria**  
   - O número de unidades de transferência de calor $`( NTU \\)`$ e a eficiência $`( \\varepsilon \\)`$ são combinados com as perdas por atrito para avaliar o desempenho do trocador.

3. **Influência do regime de fluxo**  
   - A análise destaca que a irreversibilidade pode ser minimizada ajustando o **comprimento do canal de fluxo** $`( L \\)`$ e o **raio hidráulico** $`( r_h \\)`$ do trocador.

---

## **Resultados e Conclusões**  

- O método $`( N_s \\)`$ permite otimizar diretamente a troca entre **eficiência energética** e **custos de fabricação**.  
- O tamanho do trocador de calor necessário aumenta à medida que se busca minimizar as perdas entrópicas.  
- A abordagem é compatível com **ciclos de Brayton** e **refrigeração criogênica**, onde a eficiência é crítica.  
- Para um trocador de calor eficiente, a **área de troca térmica cresce proporcionalmente a $`( 1/N_s^2 \\)`$**.

---

>[!Important]  
>* O método apresentado é baseado na minimização da geração de entropia $`( N_s \\)`$, permitindo um design energeticamente eficiente.  
>* Aplicável a trocadores de calor gás-gás em **ciclos de potência e criogênicos**.  
>* O cálculo de irreversibilidade considera tanto a **diferença de temperatura** quanto as **perdas de carga**.  

>[!tip]  
>Para otimizar um trocador de calor, os parâmetros **$`( L \\)`$** (comprimento) e **$`( r_h \\)`$** (raio hidráulico) devem ser ajustados para minimizar $`( N_s \\)`$.  

>[!Warning]  
>Minimizar $`( N_s \\)`$ pode aumentar significativamente a **área de troca térmica**, o que impacta os custos de fabricação e o tamanho do equipamento.  

>[!Note]  
>O trabalho de Bejan foi um dos primeiros a formular uma abordagem explícita para projetar trocadores de calor considerando diretamente a **termodinâmica irreversível**.  

---

## **Referências**  

1. Kays, W. M., & London, A. L. *Compact Heat Exchangers*. McGraw-Hill, New York, 1964.  
2. Fraas, A. P., & Ozisik, M. N. *Heat Exchanger Design*. Wiley, New York, 1963.  
3. Van Wylen, G. J., & Sonntag, R. E. *Fundamentals of Classical Thermodynamics*. Wiley, New York, 1973.  
4. McClintock, F. A. "The Design of Heat Exchangers for Minimum Ir­reversibility", Paper No. 51-A-108, ASME, 1951.  
5. Bejan, A. & Smith, J. L., Jr. "Thermodynamic Optimization of Mechanical Supports for Cryogenic Apparatus", *Cryogenics*, Vol. 14, Mar. 1974.  
6. Hilal, M. A. & Boom, R. W. "Optimization of Mechanical Supports for Large Superconductive Magnets", *Advances in Cryogenic Engineering*, Vol. 22, Plenum, New York, 1976.  
7. Reynolds, W. C. & Perkins, H. C. *Engineering Thermodynamics*, McGraw-Hill, New York, 1970.  
8. Socolow, R. H., et al. "Efficient Use of Energy", *Physics Today*, Aug. 1975.  

---


