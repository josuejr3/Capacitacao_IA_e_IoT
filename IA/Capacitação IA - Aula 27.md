
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

	Topologias diferentes podem resolver o mesmo problema. 

-  Regra mais usada: backpropagation





































