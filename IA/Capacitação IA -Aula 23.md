
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
-  As funções de ativações dos perceptrons são apenas funções lineares justamente por esse tipo de rede neural possui apenas um único neurônio
	-  a(t + 1) = f (u(i)(t)) - f de ui em relação ao t



































