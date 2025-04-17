
####                              *Aprendizado baseado em instâncias*

**~={cyan}Roteiro=~**

-  K-Nearest Neighbor (KNN, K vizinhos mais próximos);
-  Distância ponderada (variação do KNN);
-  Outras distâncias;
-  Aprendizagem *Lazy* e *Eager*.

Para esses algoritmos de KNN, o processo de aprendizagem consiste no armazenamento os dados de treinamento

Nesse caso, para árvores de decisão uma vez que a árvore esta construída o conjunto de treinamento não é mais útil. No KNN isso não ocorre.

~={blue}*Basicamente, os algoritmos de KNN pegam uma entrada (valor de teste) e comparam com os valores de treinamento*=~


~={green}Exemplo=~

~={green}Situação de caso em banco, um novo cliente chega para se cadastrar e ele será comparado com todos os que já estão cadastrados para saber qual será o perfil dele.

-  ~={green}Seleciona-se 5 clientes mais parecidos com X;
-  Se os 5 são bons pagadores, X também é;
-  Se a maioria dos 5 são bons pagadores, então X também pode ser.=~

O aprendizado baseado em instâncias constrói uma aproximação diferente da função objetivo para cada novo padrão de consulta

<mark style="background: #FF5582A6;">Obs 2: Esses algoritmos possuem alto custo computacional</mark>

-  O dataset de treinamento deve estar armazenado;
-  Sempre as distâncias são calculadas a cada vez que o algoritmo é testado (cálculos repetitivos);
-  Os cálculos de distância usam todos os atributos.

---

~={cyan}Distâncias=~


-  Distância Euclidiana

Dado um padrão Xq descrito pelo seguinte vetor de características (a1(Xq), a2(Xq), a3(Xq),..., aN(Xq))

E sabendo que aR(Xq) representa o r-ésimo atributo do padrão Xq

A distância entre os dois padrões xI e xJ é dada por 

![[Pasted image 20250417173807.png]]

Essa distânncia é basicamente a distância entre dois pontos que estudamos em algebra vetorial e geometria análitica.

~={green}Exemplo=~

![[Pasted image 20250417175210.png]]

Nesse exemplo, vamos identificar em qual categoria de Y o caso de teste vai se encaixar. (Xq é uma linha do dataset de testes).

~={red}(Lembrando que isso é para atributos numéricos)=~

-  Inicialmente deve ser feito o cálculo de distâncias do meu Xq para cada um dos cinco dados presentes na base de treinamento.

-  Os cálculos vão ser feitos seguindo a lógica X1 com X1, X2 com X2,... Xn com Xn

Após os cálculos temos os seguintes resultados 

	Para 1: sqrt(1,5 - 1,3)² + (3,2 - 2,5)² = 0,73
	Para 2: sqrt(1,2 - 1,3)² + (3,0 - 2,5)² = 0,51
	Para 3: sqrt(0,8 - 1,3)² + (2,8 - 2,5)² = 0,58
	Para 4: sqrt(1,0 - 1,3)² + (2,9 - 2,5)² = 0,50
	Para 5: sqrt(2,0 - 1,3)² + (2,1 - 2,5)² = 0,81

As distâncias obtidas representam o *Grau de similaridade do Xq (caso de teste)* com os casos de treinamento, quanto menor o valor mais próximo e parecido o Xq está dos casos de treinamento.


-  Como ficaria a classificação quanto aos valores de K para os NN?

1.  Para 1-NN (A primeira menor distância) - Vermelho (0.50)
2.  Para 2-NN (A segunda menor distância) - Vermelho (0.51)
3.  Para 3-NN (A terceira menor distância) - "Azzul" (0.58), porém, como a maioria deu vermelho, então classificamos como Vermelho.

E assim por diante. Lembrando que é importante sempre que K > 1 considerar todos os valores de Y.

Ou seja, para 1 NN vejo o valor com a menor distância, para 2 NN vejo os dois valores com menor distância e assim por diante...

![[Pasted image 20250417180932.png]]

<mark style="background: #D2B3FFA6;">E se a quantidade de vermelhos e azuis forem par, como eu escolho?</mark>

<mark style="background: #D2B3FFA6;">A depender do tamanho do dataset, eu poderia ignorar?</mark>

-  Uma das formas de resolver o problema é quando uma base for binária usar um número ímpar do K.
-  Porém, uma base com três classes, como a íris usar o K ímpar não resolve;
-  Quando isso ocorre, pode ser necessário escolher um dos dois, com 50% de chance de acertar.

O KNN acaba sendo uma forma de "ranquear" o top cinco que foi discutido anteriormente.

---

~={cyan}K-Nearest Neighbor=~

-  Ideia central é armazenar todo os exemplos de treinamento
-  Calcular as distâncias de atributos para cada exemplo e comparar com o teste
-  Não existe um algoritmo de treinamento, os valores são apenas guardados
- 

































