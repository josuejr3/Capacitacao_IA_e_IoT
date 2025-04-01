
####                                        *Árvores de Decisão - Parte 1*

~={cyan}Árvore de decisão=~

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
-  Cada percurso na árvore (da raiz até a folha) corresponde a uma~={red} regra de classificação=~.
- Como usamos X e Y para definir os rótulos A1 e A2 significa que é um algoritmo de ~={red}aprendizado supervisionado=~. 
-  A árvore lida bem com datasets que possuem algum tipo de ruído, como dados faltantes ou mal mensurados;
-  Usados em diagnósticos médicos, diagnósticos de equipamentos e análise de creditos.

~={cyan}Procedimento de Construção de uma Árvore de Decisão=~

1. Escolha de Atributo;
2. Estender a árvore adicionando um ramo para cada valor do atributo;
3. Passar os exemplos para as folhas (tendo em conta o valor do atributo escolhido)
4. Para cada folha
	1. Se todos são da mesma classe, associar essa classe à folha
	2. Senão, repetir os passos 1 a 4

<mark style="background: #FF5582A6;">Obs: é possível definir uma parada para evitar o overfitting</mark>

![[Pasted image 20250401085949.png]]

Nesse exemplo de dataset o valor de X2 é pouco relevante, uma vez que quem define a classe (Y)  é X1, isto é, X1 tem mais peso no valor da definição da classe Y.

~={cyan}Como é feita a métrica de um atributo em relação as classes? (como saber se é um bom atributo)=~

Antes de mais nada...

~={red}-  Uma divisão que mantêm as proporções de classes em todas as aprtições é inutil;=~
~={green}-  Uma divisão onde em cada partição todos os exemplos são da mesma classe tem utilidade máxima.=~

Na prática uma divisão dessa forma é dificil de acontecer. Porém, podemos procurar o melhor atributo que se aproxima disso.

<mark style="background: #FF5582A6;">Obs: os níveis da árvore referem-se aos atributos de um dataset. ELES PODEM SE REPETIR ao longo da estrutura.</mark>

![[Pasted image 20250401091643.png]]

No exemplo acima, não há como definir o melhor atributo, tendo em vista que é necessário fazer o cálculo. 

----

~={cyan}Critérios para escolha de atributo=~

O cálculos para os atributos são para todos os atributos da árvore. E além disso, os valores desses atributos definem ~={blue}partições=~ (galhos) do conjunto de exemplos.

Como critérios para escolha de atributo usamos o seguinte

-  Ganho de Informação

O ganho de informação mede a redução da ~={blue}Entropia=~ causada pela ~={blue}partição=~ dos exemplos de acordo com os valores do atributo

*~={blue}"A entropia define como é que está a aleatoriedade de um sistema físico, ou seja, ela mede a aleatoriedade de uma variável"=~*

O atributo que possuir meu maior valor de ganho de informação será o que vai ser usado como nó.

~={purple}ENTROPIA=~

$$
 Entropia (S) = - ((p+) * log 2 (p+) - ((p-) * log2 (p-)))
$$

Sendo S uma amostra dos exemplos de treinamento, A entropia vai medir a *"impureza"* de S.

-  p+ é a proporção de exemplos positivos em S
-  p- é a proporção de exemplos negativos em S

Nesse caso, utilizamos apenas a proporção de duas classes, porém, se tivessemos mais classes, como por exemplo: alto, médio e baixo, seriam três "partes".

> ~={green}Exemplo=~

Se p+ = 1, p- = 0

A entropia é 0 (mínima)

Por outro lado, se possuimos p+ = p- = 0.5

Isso significa que a entropia é 1 (máxima)

![[Pasted image 20250401094134.png]]

<mark style="background: #D2B3FFA6;">Dúvida</mark>

- Já que a entropia mede o quão desordenados está o meu atributo, eu poderia usar variância ou desvio padrão?

- A entropia é uma medida exclusiva de IA ou ela é vista na estátistica também?

---

-  Entropia é uma medida de aleatoriedade (IMPUREZA) de uma variável;
-  A entropia de uma variável nominal X que pode tomar *i* valores

$$
entropia(x) = - Σ pi *log2 (pi)
$$
-  Entropia tem máximo se pi = pij para qualquer i diferente de j
-  A entropia é mínima se existe um i tal que pi = 1
-  Com isso, temos que 0 * log2 0 = 0

---

> ~={green}Exemplo usando entropia para o caso "joga sim e joga não"=~

-  Suponha que S é uma coleção de 14 exemplos, incluindo 9 ~={blue}positivos=~ e 5 ~={red}negativos=~.

	Notação: [9+, 5-]       (1)

A entropia de S em relação a esta classificação booleana é dada por:

	Entropy([9+, 5-]) = -(9/14)log2(9/14) - (5/14)log2(5/14) = 0.940

Como o valor se aproximou de 1 um significa que ele não é um atributo tão bom para ser a raiz.

---

~={cyan}Ganho de Informação=~

A fórmula do ganho de informação baseada na entropia do atributo

$$
ganho(Exs, Atri) = entropia(Exs) - Σ (Exsv/Exs) * entropia (Exsv)
$$

Todo o somátorio é baseado em informações do atributo

-  Exsv - Número de exemplos com valor do atributo
-  Exs - Número de exemplos total

Sendo assim, a construção da árvore leva em consideração essa fórmula com objetivo de diminuir a entropia (aleatoriedade) da váriavel que define as classes.

![[Pasted image 20250401100455.png]]

<mark style="background: #FF5582A6;">Nesse exemplo, apesar de estarmos considerando três valores de atributos (chuva, nublado e sol) o Y só pode ser SIM (joga) ou (NÃO) não joga. Dessa forma fazemos o cálculo baseado nisso
</mark>

![[Pasted image 20250401100816.png]]

Funciona como se fosse uma proporção condicional. Sendo assim, temos que:

A QUANTIDADE DE JOGA se o tempo é SOL = 2/5
A QUANTIDADE DE NÃO JOGA se o tempo é SOL = 3/5

![[Pasted image 20250401100951.png]]

Por fim, a medida do ganho de informação é dada pela entropia das classes desejadas para Y que no caso foi a divisão em (1), subtraido da informação do tempo

![[Pasted image 20250401101759.png]]



































































































































































































































