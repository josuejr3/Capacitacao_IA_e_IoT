
#####                                                       <span style="color:rgb(0, 255, 64)">Sistemas Embarcados - Interrupções Parte 2</span>

-  Continuação 

**![[Pasted image 20250428170738.png]]

*Interrupção gerada a cada um segundo - sempre que a interrução ocorre, a função vUpdateTime é chamada para tratar a interrupção*.


1.  Desabilitar as interrupções quando for adentrar na região crítica e habilitar novamente após sair dela.  (**~={red}O CASO ABAIXO NÃO HABILITA AS INTERRUPÇÕES NOVAMENTE, DEVIDO O RETURN DA FUNÇÃO=~**)

	![[Pasted image 20250428173300.png]]

Como a "solução" acima não resolve o problema, é ncessário pensar em outra maneira de habilitar e desabilitar as interrupções quando estamos na região crítica. 

	As vezes é necessário tomar precauções para não habilitar interrupções que estavam previamente desabilitadas.

	 Isso ocorre, pois a interurupção poderia ter sido desabilitada anteriormente por um trecho de código concorrente

Para resolver esse problema, criamos uma variável bool que vai identificar se a última interrupção está desabilitada ou não. 

Se ela estiver, ela permanecerá desativada. Se ela estivar ativada, desativamos com uma condicional.

![[Pasted image 20250428174746.png]]

-  Melhor forma, é a refatoração do código

![[Pasted image 20250428174911.png]]

Ainda há um problema nesse caso que é o seguinte

	Se considerarmos um long com um total de bits de 64, e o microprocessador de 32 bits, então o microprocessador tem só consegue manipular de uma única vez até 32 bits. Isso vai fazer com que o return que estamos usando seja "quebrado" em várias instruções.

<mark style="background: #D2B3FFA6;">O código acima, ficaria melhor usando um static toda vez que o tratamento de exceções fosse chamado?</mark>

Outra alternativa, seria ler a variável duas vezes, nesse caso lê a quantidade de segundos uma vez e depois lê de novo.

O que quer dizer se eu li o valor antes de entrar na zona crítica, ele deu um X e após sair da zona crítica ele deu outro, valor, um Y. Significa que durante esse meio tempo, houve a transição. 

![[Pasted image 20250428180746.png]]

---

-  O uso da palavra chave **~={cyan}volatile=~** em C/C++ é usada para informar ao compilador que a variável pode ser alterada por outro trecho de código.

Essa palavra chave é usada em situações de trechos de códigos concorrentes. Pois em programação "normal" o compilador otimiza o trecho de código para que não seja necessário obter os valores novamente da memória. 

Quando usamos o volatile ele informa ao compilador "sempre pegue o valor que está na memória porque ele pode ter sido alterado."


---

###### <span style="color:rgb(0, 255, 64)">Interrupções Concorrentes</span>

-  Quando duas interrupções ocorrem ao mesmo tempo

	-  ~={blue}A de maior prioridade é executada;=~

		As interrupções podem vir de várias fontes,  e com isso podemos setar uma prioridade diferente para cada fonte de interrupção.


	-  ~={blue}As vezes diferentes fontes "compartilham" a mesma ISR. =~

		Nesse caso, vai existir uma única função de tratamento de interrupções para vários tipos de interrupções. Quando isso ocorre, a verificação de quem gerou a interrupção ocorre internamente.  (normalmente usamos if e elses) 

	-  ~={blue}Outra coisa que pode acontecer é a aparição de interrupções aninhados.=~

		Isso quer dizer que eu posso estar no meio da execução de uma interrupção e eu chavear para uma outra interrupção de maior prioridade. Se a prioridade for menor ou igual, então a interrupção atual é tratada primeiro, ou seja, não ocorre a aninhada. (Normalmente pode ser habilitada manualmente, depende do microcontrolador).


<mark style="background: #D2B3FFA6;">Uso do static em tratamento de interrupções e sistemas embarcados</mark>

###### <span style="color:rgb(0, 255, 64)">Interrupções Desabilitadas</span>

O que ocorre se uma interrupção for gerada enquanto as interrupções estiverem desabilitadas?

-  No geral, a interrupção vai ser *postergada* (adiada);
-  As vezes as interrupções são desabilitadas por um tempo, mas os eventos não podem ser perdidos. 

###### Latência de Interrupção 

Alguns fatores que influenciam na latência de interrupções são

-  Período mais longo em que a interrupção fica desabilitada

É o tempo entre a desativação e reativação da interrupções no programa

-  Tempo de execução de todas as interrupções com prioridade superior

É o tempo que leva para que todas as execuções de interrupções de prioridade superiores sejam concluídas.

-  Tempo de chaveamento do processador;

É o tempo em que o processador troca de uma rotina para outra. 

-  Tempo para salvamento do contexto e execução da ISR, relação com IRQ (Interrupt Request)

É o tempo em que o ponto atual do programa é salvo na pilha de execução até que ele retorna após a execução da função de tratamento de exceção.

###### Resolução para diminuir a latência no contexto de interrupções

-  Avaliar o tempo de processos e tarefas

	O tempo pode ser determinado de duas formas
	-  Contando instruções;
	-  Realizando experimentos (principalmente em cenários não determinísticos).

-  Como lidar com gargalo em tempo de resposta

	Quando os fatores dependem de software, podemos;
	-  Escrever códigos eficientes;
	-  Escrever ISRs curtas;
	-  Desabilitar interrupções o mínimo possível;
	-  Determinar cuidadosamente as prioridades


























