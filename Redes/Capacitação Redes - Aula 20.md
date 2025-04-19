
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

-  O ZigBee tem suas camadas base (física e de controle de acesso ao meio) com o IEEE 802.15.4. O gerenciamento de dispositivos da rede, a escolha do canal de comunicação com menor ruído, o melhor caminho para tráfego de dados e a distribuição de endereços dinÂmicos da rede são características do padrão ZigBee

-  A rede de trabalho dos dispositivos ZigBee é PAN, (ou seja, personal area network ?). Cada rede formada possui um endereço específico chamado PAN ID, que é o meio de diferenciar as redes formadas por diversos dispositivos coordenadores. Esse endereço deve ser armazenado em cada dispositivo ZigBee ao associar à rede especifica. 

-  Para que haja uma PAN, o coordenador realiza um conjunto de leituras com intenção inicial de procurar um endereço e um canal de frequência disponível para a comunicação. Para isso verifica-se o nível de energia de cada canal testado (Energy scan). Se o nível de um local for alto, esse canal entra na lista de memória de canal disponível no coordenador. 

-  Associação da PAN com o coordenador.

-  Cada rede ZigBee possui um coordenador.

~={cyan}Modos de Operação de Dispositivos ZigBee
=~
Basicamente os modos de operação se referem ao consumo de energia eleétrica que o dispositivo pode gastar em seus diferentes modos de trabalhos. 

O padrão ZigBee suporta os seguintes modos:

-  Modo Inativo

É quando o dispositivo não recebe e nem transmite dados. O dispositivo está em processo de verificação de dados válidos vindos da antena. Ele sai desse modo para um desses outros: Transmissão, Recepção, Sono ou Comando

-  Modo de Recepção

Quando os dados estão pronto para transmissão são coletados da antena do dispositivo. Nesse modo, se um dado é válido, é recebido e vai para o *buffer* de transmissão serial.

-  Modo de Comando;

Quando a sequência de dados de comando é iniciada. Nesse modo, para modificar ou ler os parâmetros do módulo de RF ele deve ficar em modo comando. Ao entrar nesse modo, os dados são recebidos e interpretados como linhas de comando.

-  Modo Sono;

Quando são dispositivos finais (basicamente o sensor que é um end device, precisa de uma validação muito rápida para fazer algo no ambiente). É quando o dispositivo possui menor consumo de energia, na classe de *redes de curto alcance*.

-  Modo de Transmissão

Quando dados seriais oriundos do *buffer* estão prontos a serem empacotados. O endereçamento do destino do pacote determina qual módulo na rede receberá o pacote. 

	Nesse caso, o dispositivo assegura-se que o 

-  Modo Ativo.

Não é um modo específico, é um conjunto de modos.

















































