
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

###### Interrupções Concorrentes

-  Quando duas interrupções ocorrem ao mesmo tempo

	-  A de maior prioridade é executada;
	-  As vezes diferentes fontes "compartilham" a mesma ISR (Instruction Routine)
		-  Deve-se verificar todas as possíveis fontes dentro da ISR 





























