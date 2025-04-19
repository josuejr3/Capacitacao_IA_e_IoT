
####                                                         *~={cyan}ZigBee - Parte 2*=~


~={cyan}Tipos de Dispositivos ZigBee=~

No padrão ZigBee o tipo de dispositivo está relacionado com a quantidade de tarefas que uma pilha de instruções armazenadas na memória do microcontrolador pode executar.

-  FFD - Full Feature Device;
-  RFD - Reduced Feature Device

O ~={blue}FFD=~ é um dispositivo que possui a pilha de instruções completa em sua memória e a característica de incorporar qualquer papel da rede. Além disso, ele é considerado o dispositivo pai por poder se comunicar com qualquer outro dispositivo..

O ~={blue}RFD=~ por sua vez possui um conjunto reduzido de instruções carregadas em sua memória e está limitado a pequenas tarefas. Ele se comunica apenas com o FFD e é considerado um dispositivo filho, pois precisa do dispositivo pai para associar à rede. (dispositivos finais seriam RFD).

![[Pasted image 20250419114138.png]]

~={cyan}Topologia de Redes ZigBee=~

-  Topologia estrela

Nesse caso, os dispositivos finais se comunicam apenas com o coordenador, não havendo a possibilidade de dados serem retransmitidos pelos roteadores.

![[Pasted image 20250419114358.png]]

-  Topologia *peer-to-peer*

Cada módulo FFD ZigBee pode se comunicar com outro módulo FFD mais próximo, havendo assim, a possibilidae de roteamento de dados. Nessa topologia a rede é formada pelos módulos dotados de todos os papéis previstos pelo padrão.

Dependendo de como é feita a inclusão de novos dispositivos na rede esse tipo de topologia pode assumir duas ~={blue}subdivisões=~.

	-  Mesh

	Ocorre quando novos membros FFD se comunicam com módulos FFD da rede na mesma região de cobertura. E os dispositivos finais podem usar os roteadores para se comunicar com o roteador. 

![[Pasted image 20250419115114.png]]


<mark style="background: #D2B3FFA6;">Os dispositivos finais ainda vão poder se conectar diretamente com o coordenador?</mark>

	-  Árvore.

	Nessa topologia de árvore os membros podem crescer de forma metódica e organizada. Aqui, os roteadores funcinam como galhos e os dispositivos finais como folhas.

	Quando novos dispositivos finais precisam se associar a rede, eles precisam verificar se o módulo pai (FFD) disponivel mais próximo, que pode recebê-los. A rede pode se expandir com a inclusão de novos dispositivos roteadores.

![[Pasted image 20250419115951.png]]

~={cyan}Formação de uma Rede ZigBee=~























































