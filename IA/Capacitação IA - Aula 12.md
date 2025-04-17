
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

