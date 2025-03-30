
Dentre os campos de inteligência artificial, tem-se o ~={cyan}reconhecimento de faces=~. Para isso são utilizadas métricas de distâncias e marcações;

![[Pasted image 20250330122848.png]]

Depois de todas as métricas de distâncias estarem estabelecidas em uma matriz, esses valores são colocados em um algoritmo de aprendizagem de máquina para que ele possa entender de quem era a imagem.

-  Uma entidade que estamos analisando tem características, atributos e features que servem como coluna de uma matriz.

<mark style="background: #ABF7F7A6;">Como podemos ensinar uma máquina de uma maneira que elas aprendam com experiência?</mark>

*"Diz-se que um programa de computador aprende com a experiência **E** com relação a alguma classe de tarefas **T** e medida de desempenho **P**, se seu desempenho nas tarefas **T**, medido por **P**, melhora com a experiência **E**"* - Tom M. Mitchell.

- E - experiência (dados rotulados)

> ~={green}Exemplo: várias imagens de pessoas específicas (Imagem de X pessoa porque tem Y dimensões).=~

-  T - tarefas (reconhecer fotos das pessoas específicas nas imagens) (objetivo)

Para isso é usada medida de ~={cyan}desempenho=~

-  P - desempenho (taxa de acertos)

>~={green} Exemplo: 15 fotos de Thiago e 15 fotos de Carlos. A IA é treinada com dez fotos de cada e as cinco que sobraram de cada um são testadas, e do total ver quantas a IA irá acertar.=~

> ~={green}Outro exemplo=~

-  Tarefa T: classificar um e-mail como spam ou não;
-  Medida de desempenho P: percentual de e-mails corretamente classificados;
-  Experiência E: e-mail manualmente rotulados por humanos.

~={red}Obs: os dados são incertos e em muitos datasets há dados faltantes.=~

![[Pasted image 20250330130431.png]]

Na imagem acima, vemos que se trata de uma função exata, uma matemática "bruta", em que qualquer valor inserido terá um resultado. 

Em Machine Learning isso não existe, ~={red}não há =~uma função que represente todo o dataset. O que será feito é tentar criar uma função que ela possa ser ajustada de acordo com os dados. 

-  Basicamente, o aprendizado de máquina funciona como uma função que é generalizada para um conjunto de dados e com isso, um novo dado é usado (que não foi testado) e a função será capaz de reconhecer;

>~={green} Exemplo - gráfico porta AND=~

![[Pasted image 20250330131330.png]]

~={green}Nesse caso, como o espaço foi dividido em duas regiões, o ponto (0.8, 0.8) é considerado True (1).=~

![[Pasted image 20250330132227.png]]

~={green}Outro exemplo é a situação de identificação de um bom cliente em um banco.=~

<mark style="background: #ADCCFFA6;">Regressão X Classificação</mark>

Basicamente a diferença é que na regressão o Y possui intervalos contínuos, enquanto que na classificação os intervalos são discretos.

-  Regressão linear - cria uma reta que melhor representa os dados

![[Pasted image 20250330132904.png]]

Outra forma de usar funções

![[Pasted image 20250330133122.png]]

<mark style="background: #ADCCFFA6;">Aprendizado de Máquina é usado quando...</mark>

-  Existência de padrão
-  Não existe uma função que resolve o problema;
-  Dados (porém, eles devem estar organizados).

---

<mark style="background: #ABF7F7A6;">Tipos de Aprendizado</mark>

-  <mark style="background: #BBFABBA6;">Aprendizado supervisionado</mark>

	Possui esse nome, pois ele ajusta os parâmetros x1 e x2 usando o Y.

	-  Conjunto de treinamento com **rótulos associados**. Ex: Jose é bom pagador, Felipe é mal pagador...

	Para rótulos de classe discretos, esse problema é chamado de classificação. Já para valores contínuos ele é conhecido como regressão

	Base de Classificação

| X1  | X2  |    Y    |
| :-: | :-: | :-----: |
| 1.2 | 2.3 | **Bom** |
| 3.2 | 3.2 | **Mau** |
	 Base de Regressão

| **X1** | **X2** | **Y** |
| :----: | :----: | :---: |
|  1.2   |  2.3   |  4.2  |
|  3.2   |  3.2   |  3.1  |

-  <mark style="background: #BBFABBA6;">Aprendizado não-supervisionado</mark>

	Nesse tipo de algoritmo não são utilizados "y" como valor de referência/rótulo, tem-se apenas a entrada.

	O algoritmo tenta agrupar os dados de alguma maneira, formando agrupamentos ou **clusters**

	Após a definição de agrupamentos são feitas analises para entender o que cadagrupo representa no contexto do problema. 