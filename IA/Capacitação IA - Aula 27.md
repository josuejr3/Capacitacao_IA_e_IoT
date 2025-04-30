
#####                                                          <span style="color:rgb(0, 255, 64)">Multi-Layer Perceptrons</span>

###### <span style="color:rgb(0, 255, 64)">Introdução</span>

Redes de múltiplas camadas não usamos mais a função linear. Como vão ser necessárias curvas ao invés de retas, priorizamos o uso das funções tangente hiperbólica e zigmoid logística. É a partir delas que vamos estruturar as curvas que delimitam os dados

![[Pasted image 20250429211825.png]]

---

-  Redes e uma única camadqa (perceptrons) só conseguem resolver problemas linearmente  separáveis. 

	Para resolver esse problema, podemos usar várias camadas. 

1. Camada 1 - uma rede perceptron para cada grupo de entradas formando uma separação linear.
2.  Camada 2 - uma rede combina as saídas das redes da primeira camada, produzindo a classificação final
	
	![[Pasted image 20250429212554.png]]'

###### <span style="color:rgb(0, 255, 64)">Função de ativação linear</span>

-  Cada camada computa uma função linear
	-  ~={red}Composição de funções lineares é uma função linear=~
			Para rede neurais de multiplas camadas (MLP) vamos evitar usar funções lineares.
	-  Sempre vai existir uma rede com ***uma camada*** equivalente a uma rede multicamadas com **funções de ativação lineares.**

-  ~={red}A função de ativação não pode ser linear=~
-  Deve informar os erros para as camadas inferiores da rede
	-  ~={red}Função sigmóide
	-  Função tangente hiperbólica=~

	![[Pasted image 20250429214115.png]]

Em relação ao treinamento, exitem muitos algoritmos de treinamento que podem ser usados. Em sua maioria, os algoritmos são supervisionados e um dos mais conhecidos é o ~={blue}_Backpropagation_=~

-  ~={blue}Treinamento Estático=~

	MLPs com formatos e tamanhos diferentes podem utilizar a mesma regra de aprendizado

	*Topologias diferentes podem resolver o mesmo problema.* 

-  Regra mais usada: backpropagation

###### <span style="color:rgb(0, 255, 64)">Backpropagation - (Fase de Treinamento)</span>

O backpropagation é um algoritmo de treinamento para MLPs e ele é dividido em dois momentos.

-  Fase forward 

Pega cada uma das linhas do dataset e leva para a rede neural. Após chegar no final (e como estamos treinando) ele retorna. 

-  Fase backward

É a fase que começa quando o valor da rede neural foi obtido, ele usa o valor do erro obtido e vai ajustando os pesos a partir do final da rede neural até o começo no sentindo de "voltando". ~={red}Essa fase só existe no treinamento.
=~
![[Pasted image 20250429215522.png]]

Ainda em relação a MLP temos o seguinte

-  Rede é treinada com pares *entrada-saída*
-  Cada entrada de treinamento está associada a uma ~={red}saída desejada=~.
-  Treinamento em duas fases, cada uma percorrendo a rede em um sentido.

	![[Pasted image 20250429220059.png]]

-  A quantidade de camadas intermediárias pode mudar de implementação para implementação.

	![[Pasted image 20250429220400.png]]

---
###### <span style="color:rgb(0, 255, 64)">Procedimento</span>

~={cyan}FORWARD=~

- Entrada é apresentada à primeira camada da rede;
	-  Após os neurônios da camada i calcularem seus sinais de saída, os neurônios da camada i + 1 calculam seus sinais de saída.

- Saidas produzidas pelos neurônios da última camada são comparadas às saídas desejadas;

~={red}Erro - para cada neurônio da camada de saída é calculado.=~

~={cyan}BACKWARD=~

- A partir da última camada
	-  O nó ajusta seu peso de modo a reduzir o erro
	-  Nós das camadas anteriores tem seu erro definido por:
		- Erros dos nós da camada seguinte conectados a ele, ponderado pelos pesos das conexões entre eles.

No backpropagation temos dois estados de ativação

-  1 (+1) = Ativo
-  0 (-1) = Inativo




























