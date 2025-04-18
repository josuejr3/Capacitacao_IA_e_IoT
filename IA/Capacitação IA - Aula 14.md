
####      *~={cyan}Aprendizado baseado em Instâncias - Distâncias para dados Categóricos=~*


-  Redes neutais trabalham apenas com atributos numéricos (não é possível trabalhar com dados categóricos);

~={cyan}Tipos de Dados=~

-  Dados numéricos
	-  Permite operações matemáticas, tais como: soma, subtração, multiplicação, divisão, igualdade, maior e menor que;

	-  Exemplos: altura e peso;

	-  Pode-se medir a dissimilaridade usando distância Euclidiana.

-  Dados categóricos
	-  Permite apenas operações de igualdade e diferença;

	-  Exemplos: sexo, estado civil e cor dos olhos.

Paraos dados categóricos ou é necessário buscar distâncias específicas para dados categóricos ou então transformar em atributos numéricos.

~={blue}Distância de Hamming=~

A distância de Hamming é um tipo de distância que pode ser usada para dados categóricos.

![[Pasted image 20250418143113.png]]

A distância de Hamming consiste em verificar se os atributos de treinamento são iguais aos de teste.

> ~={green}Exemplo=~

Um dataset de treinamento e de teste com cinco colunas categóricas. X1, X2, X3, X4 e X5. 

Se um atributo X1 do conjunto de treinamento for igual ao X1 do de teste, então dizemos que para aquele atributo a distância é de 0. 

Fazemos isso para todos os atributos categóricos e ao final somamos tudo. Sendo assim, se apenas X1, X3 e X5 forem iguais nos dois datasets. Dizemos que o dataset de teste tem 3 atributos iguais.

~={blue}VDM - Value Difference Metric=~

O VDM também serve para distância entre dados categóricos. Ele serve para descobrir quando dois valores tem distribuição igual entre as classes e geralmente é mais precisa que a distância de Hamming. 

![[Pasted image 20250418144145.png]]

![[Pasted image 20250418145028.png]]

-  Não há garantia que a distância VDM seja melhor do que a de Hamming para o caso acima.
-  O VDM pode ser aplicado a dados numéricos, porém, o atributo perde a precisão.
		Porém, o VDM para atributos numéricos pode criar um número de categórias muito grandes

	Caso mesmo assim ainda queira utilizar o VDM para dados numéricos será necessário discretizar, para isso basta seguir o procedimento abaixo.

![[Pasted image 20250418150710.png]]

~={cyan}Dados Categóricos - Python=~

-  A maioria dos algoritmos trabalham com dados numéricos;
-  Existem diversas formas de codificar categóricos em numéricos.

	~={blue}One-Hot Encoding - Features (atributos);=~
	~={blue}Integer Encoding - Target (classes).=~

<mark style="background: #FF5582A6;">OBS: Não usar INTEGER ENCODING COM FEATURES !!!</mark>

![[Pasted image 20250418152350.png]]

~={cyan}One-Hot Encoding 
=~
Cada valor categórico daquela característica ela se tornará uma coluna

![[Pasted image 20250418152532.png]]






























