
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

