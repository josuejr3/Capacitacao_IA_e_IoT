
#### *~={cyan}                                                            Perceptrons=~*

-  A primeira camada em uma rede neural não contém neurônios de processamento. A camada se trata de uma camada de pré-processamento. 
-  É basicamente a camada que usa One Hot Encoding ou Label Encode

	![[Pasted image 20250423203630.png]]

-  O nó em azul (neurônio) faz a descriminação e a predição. Ele também é responsável pela reta observada no "hiperespaço".

<mark style="background: #FF5582A6;">Obs: o aprendizado de uma rede neural é basicamente o ajuste e a alteração dos pesos.</mark>

---

##### <span style="color:rgb(0, 255, 64)">Perceptrons</span>

Perceptrons são redes neurais que possuem um único neurônio. Ele pode ser considerado uma reta no espaço, dessa maneira, ele é eficiente quando podemos separar elementos linearmente.

-  Rede mais simples com classificação de padrões *linearmente separáveis*;
-  Utiliza modelo de McCulloch-Pitts como neurônio.

> ~={green}Exemplo de dataset que não podemos separar utilizando uma reta.=~

![[Pasted image 20250423205913.png]]

*Dataset banana - não são linearmente separáveis*

> ~={green}Exemplo de dataset que pode ser separado utilizando Perceptron (reta linar).=~

![[Pasted image 20250423210143.png]]

> ~={green}Outro exemplo para dados que não podem ser divididos linearmente (Perceptron)=~

![[Pasted image 20250423210303.png]]

*Nesse caso, foi usado perceptron, porém como não havia como separar de forma linear os dados a separação ficou "errada" ou "confusa". Dessa maneira, o perceptron vai errar bastante.*

-  Quando passamos para ver problemas de funções lógicas como AND ou XOR, temos o seguinte

![[Pasted image 20250423210959.png]]

	O AND é um problema que pode ser representado como uma função linear, ou seja, um Perceptron.

	Porém com o XOR não é possível fazer o mesmo, os dados do XOR não podem ser divididos com uma única reta. 

	Para resolver o problema do XOR é necessário utilizar múltiplas camadas

##### <span style="color:rgb(0, 255, 64)">Perceptrons, Estados e Funções</span>

-  Os perceptrons possuem dois estados de ativação
	-  1 = ativo
	-  -1  = inativo

-  As funções de ativações dos perceptrons são apenas funções lineares justamente por esse tipo de rede neural possui apenas um único neurônio (a função é basicamente o somatório u, entradas pelos pesos)

	![[Pasted image 20250423211713.png]]

-  As funções de saída vão ser uma função identidade, ou seja, se a função de ativação deu -1 então a função de saída é -1 também e o mesmo ocorre se for +1.

##### <span style="color:rgb(0, 255, 64)">Camadas do Perceptron</span>

O Perceptron possui duas camadas

-  A primeira camada se trata de um pré-processamento dos dados;
-  A segunda é a~={blue} camada de descriminação=~ e é onde os dados são processados.
	-  Essa camada possui um nó de saída;
	-  E pesos determinados após o aprendizado.

<mark style="background: #FF5582A6;">Obs: um perceptron ele pode ter vários neurônios, porém, uma única camada.</mark>

<mark style="background: #D2B3FFA6;">E qual a diferença nisso?</mark>

![[Pasted image 20250423212638.png]]

-  A camada de pré-processamento não vai ser utilizada, pois nos exemplos que estaremos fazendo vamos fazer o pré-processamento antes.

##### <span style="color:rgb(0, 255, 64)">Treinamento</span>

-  Atualização de erro e pesos

	![[Pasted image 20250423214154.png]]

	- n é uma constante chamada de taxa de aprendizado. Normalmente utiliza-se um valor baixo, como por ex: 0.001, 0.002, 0.005 e assim por diante...

		Esse n pode ser considerado como o grau de "violência" que eu quero que os pesos atualizem. Ou seja, se o valor desse parâmetro for muito alto, o valor do peso vai ser ajustado muito drasticamente para cima ou para baixo.

		~={blue}Em resumo, um valor de n é melhor para ir fazendo os ajustes do peso aos poucos.=~

		<mark style="background: #FF5582A6;">Tipo de parâmetro que evita-se mexer</mark>

	- x é o valor de entrada, ou seja, os valores que estão presentes nos ""nós"" em laranja. Ou seja, para atualizar o valor de w1 eu uso x1, para o de w2, x2 e assim por diante.
	- O erro é dado por (d - y) em que d é o valor desejado da saída durante o treinamento. Já o y é o valor que de fato apareceu.
	- Quando o valor de erro é 0, então o peso não é atualizado, pois a multiplicação total será de 0.
	- O novo W, ou seja, o peso, vai ser o peso anterior + o peso atual
	
```Python
delta_w = w_atual + w_proximo
delta_w = w_atual + 0 # se não teve erro
delta_w = delta_w + w_proximo # se houve o erro
```

##### <span style="color:rgb(0, 255, 64)">Algoritmo de Treinamento</span>

-  Inicia todas as conexões com peso (w) = 0
-  Repita
	-  Para cada par de treinamento (**X**, d)
		Com X sendo o vetor de entrada e d sendo o valor desejado
		- Calcular a saída y
		-  Se (d é diferente de y) então
			Atualize os peso até o erro ser aceitável ou até completar um número de ciclos que definimos.
			
Um ciclo nesse caso é definido como sendo o processamento de todos os dados do dataset

<mark style="background: #D2B3FFA6;">Por que os pesos tem que ser zerados ou aleatórios?</mark>

<mark style="background: #D2B3FFA6;">Se tiver mais classes de saída, ex: 3 como vou saber se as classes so são -1 e +1?</mark>

<mark style="background: #D2B3FFA6;">O padrão 001 seriam um "conjunto de atributos"?</mark>

![[Pasted image 20250423222707.png]]

<mark style="background: #D2B3FFA6;">O treinamento é feito até "acertar"?</mark>

![[Pasted image 20250423223111.png]]

> T~={green}estando os dados=~

![[Pasted image 20250423223458.png]]

<mark style="background: #D2B3FFA6;">O que acontece se eu tiver mais que um neurônio? na mesma camada?</mark>





