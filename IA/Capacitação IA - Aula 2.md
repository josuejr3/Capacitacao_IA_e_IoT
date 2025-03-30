
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

-  Basicamente, o aprendizado de máquina funciona como uma função que é generalizada para um conjunto de dados e com isso, um novo dado é usado (que não foi testado)