#### ~={cyan}                                         *Árvores de Decisão - Parte II=~

Cálculo do Ganho de Informação para Atributos Númericos

	Para organizar quando os dados são númericos é feita uma divisão binária. Ou seja, ao organizar os dados, haverá um valor de referência no atributo, valores menores vão para um ramo da árvore, e valores maiores para outro ramo.

-  Passos 

1. Ordenar de forma crescente os valores de um determinado atributo;
2. Qualquer ponto intermediário entre dois valores diferentes e consecutivos pode sr utilizado como possivel ponto de referência.

<mark style="background: #ABF7F7A6;">Normalmente usa-se o valor médio entre dois valores consecutivos e diferentes.</mark>

<mark style="background: #ABF7F7A6;">Dentre esses pontos, é escolhido o ponto de referência com maior ganho de informação.</mark>

> ~={green}Exemplo=~

![[Pasted image 20250402132238.png]]

- Nesse caso as divisões ocorreram quando:
	-  A temperatura e a classe "Joga se alteram"
	-  Somente a temperatura se altera
	
-  Considerando 70 e 71 (3 seta) tem-se que o ponto de referência é 70.5. Dessa forma, temos
	Temp < 70.5
	Temp > 70.5

Ok, mas como medir o ganho de informação?
	Com a base de dados separada, basta calcular a entropia dos dados

![[Pasted image 20250402133209.png]]

O ideal é fazer o cálculo para todas as divisões que vimos lá no dataset

---

~={blue}Quando parar a divisão dos exemplos?
=~
-  Todos os exemplos pertencem a mesma classe (a folha vira a classe);
-  Todos os exemplos tem os mesmos valores dos atributos;
-  O número de exemplos é inferior a um certo limite;
-  O mérito de todos os possíveis testes de partição dos exemplos é muito baixo (evita overfitting).

---

~={cyan}Árvore de Decisão - Algoritmo=~

-  Entrada - um conjunto de exemplos;
-  Saída - uma árvore de decisão;
-  Função GeraÁrvore(Exs):
	-  Se o critério_parada(Exs) = True; retorna Folha
	-  Escolhe o atributo que maximiza o critério_divisão(Exs) (maior ganho);
	-  Para cada partição i dos exemplos baseados n atributo escolhido: arvore = Gera_árvore(Exsi)
	-  Retorna um nó de decisão baseado no atributo escolhido e com descendentes árvore,
	-  Fim

---

~={blue}Overfitting - sobre-ajustamento=~

O overfitting é basicamente quando o algoritmo fica muito ajustado para um determinado conjunto de dados. Isso faz com que ele fique com ruído.

Com isso, o desempenho do algoritmo (a taxa de acertos), torna-se pior do que um mesmo algoritmo que tenha sido "menos treinado".

~={red}É preferível ter uma árvore com um nível a menos do que um nível a mais com a junção do overfitting=~

	- Em datasets sem ruído o numero de erros de treinamento pode ser 0. O algoritmo "decora" os dados.


	- Já quando tem ruído, essa capacidade vira um problema e vai chegar um nível de profundidade da árvore que as decisões vão ser baseadas em pequenos conjuntos de exemplos.

	- A capacidade de generalização para exemplos não utilizados no crescimento a árvore diminui.

<mark style="background: #FF5582A6;">Em resumo, a árvore não irá saber lidar com uma entrada diferente do que foi usado como testes.</mark>

![[Pasted image 20250402135550.png]]

Com o overfitting a árvore fica muito específica para um conjunto de dados.

Além do overfitting, pode ocorrer o ~={red}underfitting=~ que é uma árvore com uma taxa de erro maior, considerada uma árvore "preguiçosa".

<mark style="background: #D2B3FFA6;">Duvida
</mark>

Como saber o quão treinado o algoritmo está?

![[Pasted image 20250402141236.png]]

~={cyan}Navalha de Occam=~

Partindo do pressuposto que podemos criar n árvores de decisões com os dados que possuimos, qual a melhor para se escolher? 

-  Existem menos hipóteses simples do que complexas (poucos nós);
-  Se uma hipótese simples explica os dados é pouco provável que seja coincidência;
-  Uma hipótese complexa pode explicar os dados apenas por coincidencia.

---

~={blue}Formas de simplificar árvores=~

As árvores podem ser simplificadas de duas maneiras, a primeira parando o crescimento dela mais cedo (pre-pruning);

A segunda é construir a árvore completa e somente após isso podar ela (pós-pruning)

De acordo com Quinlan (1987) *"Growing and pruning is slower but more reliable"* o que significa que ir crescendo e ir podando é mais confiável. 

![[Pasted image 20250402142649.png]]

---

~={cyan}Análise geral sobre bibliotecas=~

Utilizaremos pandas, scikit-learn e entre outras bibliotecas

O pandas possui dois tipos de dados:

-  Dataframe - matriz
-  Series - coluna ou linha do Dataframe

Em relação ao scikit-learn ele aceita tanto dataframes, como também séries.

-  ~={purple}Os primeiros passos com ML podem ser realizados através do dataset "iris" que é basicamente fazer a identificação de uma flor do tipo iris a partir das medidas da petálas e cepálas;
=~
-  ~={purple}O dataset possui 150 mensurações, sendo 50 para cada uma das três espécies da flor;=~





























































































































































































