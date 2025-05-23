
##### *~={green}Regressão=~

Até agora estavmos estudando superfícies de decisão

-  KNN;
-  Árvores de Decisão;
-  MLP;
-  SVM.

E esse tipo de aprendizado pode ser representado por uma reta, como por exemplo uma função linear, ou função afim.

~={cyan}O objetivo de usar uma função linear e também a regressão linear é que tenhamos uma reta que passa pela maior quantidade de pontos possíveis.=~

~={blue}Regressão=~

Em resumo, regressão são funções que mapeiam as instâncias de um conjunto de dados em valores numéricos. 
É semelhante com a classificação, entretanto, a variável resposta é **contínua**.

~={cyan}Classificação X Regressão=~

Podemos identificar a diferença entre os dois tipos de análises a partir da seguinte pergunta. 

*"Em um banco, podemos fornecer crédito a um cliente? sim ou não. Se for fornecido, qual será o crédito?"*

-  A primeira pergunta pode ser considerada uma classificação, enquanto que a segunda é uma regressão.

![[Pasted image 20250523170737.png]]

<mark style="background: #FF5582A6;">Obs: séries temporais são um tipo específico de regressão.</mark>

![[Pasted image 20250523171251.png]]

##### *<span style="color:rgb(4, 255, 0)">Procedimento</span>*

O procedimento é semelhante a classificação

1.  Preparação e organização dos dados;
2.  Separação em treinamento e teste;
3.  Aproximação de funções objetivo, estimativas de desempenho.

	Uma função objetivo é uma função que melhor representa os dados.


##### <span style="color:rgb(4, 255, 0)">Exemplo de Aplicação</span>

-  Prever notas numéricas de filmes
-  Estimativa da probabilidade de um paciente sobreviver
-  Predição do risco para determinados investimentos
-  Estimativa de desempenho de atletas
-  Estimativa de crédito
-  Previsão do clima

![[Pasted image 20250523173434.png]]

##### <span style="color:rgb(4, 255, 0)">Outro exemplo de problema</span>

![[Pasted image 20250523173719.png]]

Nesse caso as variáveis X e y podem ter uma relação entre elas.

-  Positivamente relacionadas
	-  Quanto maior a renda, maior o consumo de água
-  Negativamente relacionadas
	-  Quanto menor a renda, menor o consumo de água

Ou então não há relação entre variáveis.

![[Pasted image 20250523173954.png]]

##### <span style="color:rgb(4, 255, 0)">Coeficiente de correlação entre variáveis de Pearson
</span>

É uma medida que avalia o quanto a "nuvem de pontos" no diagrama de dispersão aproxima-se de uma reta

O valor da correlação **r** situa-se entre -1 e +1.

-  r > 0 => correlação direta
-  r < 0 => correlação inversa
-  r = 0 => correlação nula (ausência de relacionamento linear)

![[Pasted image 20250523174422.png]]

![[Pasted image 20250523174655.png]]

##### <span style="color:rgb(4, 255, 0)">Correlação e Regressão</span>

![[Pasted image 20250523175031.png]]

Os parâmetros alfa e beta podem ser fixos ou variáveis

No caso acima, beta é o coeficiente angular que determina a angulação da reta, enquanto que o alfa determina o ponto em que ela cortará o eixo y.

##### <span style="color:rgb(4, 255, 0)">Como estimar o valor de alfa e beta?</span>



















































































































































