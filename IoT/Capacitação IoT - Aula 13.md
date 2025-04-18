
####                                            *~={cyan}Continuação Sistemas Embarcados=~*

Ainda sobre trade-offs, é importante se atentar ao uso de interrupções. Elas são necessárias para evitar que a aplicação consuma mais energia e o programa só seja "utilizado" quando for necessário tratar uma interrupção.

~={cyan}Outros desafios em Sistemas Embarcados
=~
-  Aspectos temporais
	-  Execução de múltiplas tarefas;
	-  Responder a eventos com prazos estritos;
	-  Uso de RTOS pode ajudar.
	-  Tempo de resposta (delay) - tempo para responser a um evento, ex: um botão pressionado

![[Pasted image 20250417224115.png]]


-  Testabilidade (debug)
	-  Interface homem-máquina limitada ou inexistente;
	-  Uso de cross-debugger - limitação na quantidade de breakpoints;
	-  Uso de interface de comunicação (ex: Serial/USB).
	Normalmente em sistemas embarcados normalmente utilizamos leds para indicar se algo está correndo bem ou se aconteceu algum erro.

	![[Pasted image 20250417225204.png]]

	-  JTAG é pinos específicos do microprocessador que eu conecto e informo onde será os breakpoints
	-  Porta USB serial serve para debugar como se fosse os "prints" que usamos para "debugar" códigos isso possibilita visualizar os dados no computador.

	O problema de debugar é que causa sobrecarga no sistema.
	-  Os erros podem aparecer somente no modo debug;
	-  Pode ser dificil reproduzir todo tipo de cenário de uso;
	-  Dificuldade de identificar se o bug é de hardware ou software.

	![[Pasted image 20250417230202.png]]

