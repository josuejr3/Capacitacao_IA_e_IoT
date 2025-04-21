
####                                         *~={cyan}Introdução à Redes Neurais Artificiais=~*

##### <span style="color:rgb(0, 255, 64)">O que são redes neurais artificiais?</span>

Redes neurais (RNA) são modelos de computação (e portanto, matemáticos) com propriedades peculiares.

-  Capacidade de se adaptar ou aprender;
-  Generalizar;
-  Agrupar ou organizar dados.

Além disso, RNA são estruturas distribuídas formadas por um grande número de unidades de processamento conectadas entre si (nós ou neurônios)

-  Cada neurônio ou nó em uma rede neural possui um pequeno processamento matemático.

RNAs são inspiradas no cérebro humano. Compostas por várias unidades de processamento que nesse caso são os neurônios ou nós, e interligadas por várias conexões que são as sinapses.

![[Pasted image 20250421112519.png]]

-  Esse método se mostrou eficiente onde métodos tradicionais tem se mostrado inadequados.

![[Pasted image 20250421113517.png]]

##### <span style="color:rgb(0, 255, 64)">Características das RNAs</span>

-  Aprendem através de exemplos;
-  Adaptabilidade;
-  Capacidade de generalização;
-  Tolerância a falhas;
-  Implementação rápida.

##### <span style="color:rgb(0, 255, 64)">Conceitos básicos</span>

-  Estrutura geral das RNAs
	-  Unidades de processamento n(i) (nós)
		-  Estado de ativação a(i);
		-  Função de ativação F(i);
		-  Função de saída f(i)
	-  Conexões w(ij)
	-  Topologia.

##### <span style="color:rgb(0, 255, 64)">Neurônios como Unidades de Processamento</span>

Função: recebe entradas de um conjunto de unidades A, computa função sobre as entradas e envia o resultado para a unidade B.

*Rede neural artificial com um neurônio*

![[Pasted image 20250421114502.png]]

*Somátorio das entradas pelos pesos no neurônio*

![[Pasted image 20250421114514.png]]

-  Cada conexão da rede neural, terá um peso.

> ~={green}Exemplo - base íris=~

No exemplo da base de dados íris, ela possui 4 colunas, ou seja, quatro atributos. Dessa maneira, numa rede neural para um neurônio como vimos acima, cada uma das conexões vai representar um atributo da base íris e cada um deles com um peso associado.

-  Após ter o somátorio U, esse valor é aplicado a uma ~={blue}função de ativação=~ e a saída dessa função de ativação é aplicada a uma nova função de saída (y).


---

-  Inicialmente o neurônio deve ter um valor atribuido para que possamos saber se ele será "excitado" com as informações que vai receber através das sinapses. Para isso, faz o cálculo de pesos e valores de atributos e compara-se com o valor do neurônio.

<mark style="background: #D2B3FFA6;">Dúvida: porque o valor tem que ser no minimo teta para ativar?</mark>

![[Pasted image 20250421115857.png]]

~={blue}*O teta é o limiar de excitação ou Bias é o valor ou peso necessário para que a equação matemática das entradas pelos pesos consiga excitar o neurônio. =~

<mark style="background: #FF5582A6;">Obs: durante o aprendizado os valores de W e de teta vão ser alterados. 
</mark>

<mark style="background: #D2B3FFA6;">Dúvida: por que os pesos mudam em neurônios de uma mesma camada? eles podem ser iguais?</mark>

![[Pasted image 20250421121433.png]]

O u11 pode ser aplicado em uma função de ativação, (função linear), ou poder ser aplicado em uma função de ativ





























































