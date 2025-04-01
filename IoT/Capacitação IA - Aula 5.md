
####                                        *Árvores de Decisão - Parte 1*

-  Árvore de decisão

	-  Instâncias (exemplos/dataset) são representados por pares atributos (X, y)
	-  Fáceis de serem implementados.

A estratégia desse tipo de algoritmo é basicamente divisão e conquista, ou seja, será necessário colocar um nó na raiz da árvore e todos as possibilidades a partir da raiz são os caminhos.

As árvores consistem em basicamente quebrar o problema grande em menores (lembrando que para problemas de árvore usamos ~={red}recursividade=~).

![[Pasted image 20250401083439.png]]

Após treinar o algoritmo com um conjunto de dados, foi repassado um conjunto menor, visto na tabela da figura para que o algoritmo conseguesse identificar as cores corretas.

![[Pasted image 20250401083903.png]]

Foram usados na árvore para classificar o conjunto de dados que eu possuia (A1, A2, Cor)

<mark style="background: #FF5582A6;">Obs: cada caminho da raiz até uma decisão é uma REGRA, ou seja, um teste.</mark>

![[Pasted image 20250401084406.png]]

Algumas características importantes das árvores são:

-  Cada nó de decisão contém um teste de atributo;
-  Cada ramo descendente corresponde a um possível valor deste atreibuto;
-  Cada folha está associada a uma classe
-  Cada percurso na árvore (da raiz até a folha) corresponde a uma regra de classificação.
- Como usamos X e Y para definir os rótulos A1 e A2 significa que é um algoritmo de ~={red}aprendizado supervisionado=~. 
-  Conjunto 

































































