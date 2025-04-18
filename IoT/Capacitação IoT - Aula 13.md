
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

~={cyan}Hardware para Eng. de Software Embarcado=~

-  Escrever software de baixo nível requer conhecimento de hardware;
-  Necessidade de saber ler um esquemático (esquema eletrônicos e datasheets);
-  Saber estudar novos processadores.

~={blue}Conceitos=~

A parte digital em sistemas embarcados opera por meio de dois níveis de tensão, que são os números binários 1 e 0 que conhecemos. Essas tensões podem ser:

0V e 5V ou então 0V e 3.3V

-  Nível baixo - GROUND (GND) ou Vss
-  Nível alto - VCC ou Vdd ou 3V3 etc

![[Pasted image 20250417232625.png]]

A comunicação entre os componentes ocorre pela ativação de sinais que se propagam pelas trilhas de PCB.

	Os sinais podem ser de dados, endereçamento e controle e alguns deles podem ativar em nível baio como por exemplo: *RST, RST/ e (RST nivel baixo).

![[Pasted image 20250417233145.png]]

































