#### ~={cyan}Árvores de Decisão - Parte II=~

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
-  O mérito de todos os possíveis testes de partição dos exemplos é muito baixo.































