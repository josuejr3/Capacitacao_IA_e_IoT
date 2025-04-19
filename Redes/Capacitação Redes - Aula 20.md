
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

	Nesse caso, o dispositivo assegura-se que o módulo que recebera os dados já são conhecidos e se tiver tudo ok, os dados vão ser enviados.

	O dispositivo verifica o endereço de 16 bits, se não for conhecido ele vai entrar em estado de busca de endereço na rede.
	Se a rota não for conhecida ele entra em estado de busca de rota.
	Se nenhum dos dois for reconhecidos, a comunicação não é estabelecida e o pacote é descartado.

~={red}Ainda em relação a transmissão, uma mensagem é enviada ao transmissor pela mesma rota que o dado trafegou. A função é basicamente informar que o dado chegou com sucesso. Se a mensagem não chegar no transmissor, o pacote é retransmitido.
=~
-  Modo Ativo.

Não é um modo específico, é um conjunto de modos, ou seja, é quando o dispositivo está em modo Recepção, Comando ou Transmissão.

![[Pasted image 20250419124830.png]]

~={cyan}Formação de uma Rede ZigBee=~

Ao verificar a energia dos canais testados, o coordenador verifica se os canais habilitados na memória estão sendo usados por outro coordenador. Para essa verificação ele envia um quadro de broadcast, solicitando os canais e endereços que estão em uso em uma possível rede de trabalho.

Os coordenadores ou roteadores respondem a solicitação enviando um quadro com o canl e o endereço já usados na rede de trabalho e se há dispositivos para associar a rede de trabalho em formação.

A essas etapas, chamamos de PAN Scan. Após esses procedimentos, o coordenacor tenta se conectar a um canal de frequência e endereço não utilizados, formando assim uma rede de trabalho. O coordenador se apodera do mesmo canal e endereço.


- Existe apenas um dispositivo coordenador em uma rede formada. ~={red}NÃO EXISTEM DOIS DISPOSITIVOS COORDENADORES COM MESMA PAN ID.=~

- A rede ZigBee é formada quando o coordenador seleciona um canal de comunicação e a PAN ID. Possibilitando os roteadores e dispositivos finais se conectarem a rede.

- Todos os dispositivos recebem um endereço de 16 bits ao associar a PAN, o endereço do coordenador é o 00h.

- Fluxo de conexão: 

	-  Coordenador inicia uma PAN
	
	-  Roteadores ou dispositivos finais fazem uma leitura de PAN para encontrar as mais próximas disponíveis.
	
	-  Após a leitura, o dispositivo final ou roteador analisa uma lista de PANs disponíveis para associar.

~={red}Obs: os dispositivos finais só podem se associar apenas à um único módulo pai (FFD) ou coordenador.
=~
~={blue}Como é feito a conexão de outros dispositivos?=~

Coordenadores ou roteadores vão permitir o acesso de dispositivos à rede. O controle de acesso vai depender se o acesso é permitido e se o número de dispositivos filhos já chegou ao limite máximo.

~={blue}Segurança=~

Em relação a segurança o coordenador ZigBee pode iniciar a rede com uma chave **criptografada** de 128 bits. Somente dispositivos que possuem a mesma chave podem ter acesso à rede formada. A chave pode ser adquirida em ~={orange}pré-configuração=~.


![[Pasted image 20250419133042.png]]

~={cyan}Coexistência ZigBee=~

A coexistência é a capacidade de dispositivos sem fio de diferentes tecnologias poderem operar próximos uns dos outros sem interferências na mesma faixa de frequência. O padrão ZigBee pode trabalhar em banda de frequência de 2.4GHz, assim como Wi-Fi, Bluetooth e alguns telefones sem fio.

-  O protocolo ZigBee é destinado a operar em uma **faixa de frequência que não necessita de licenciamento.** 

-  Com isso, ele deveria sofrer interferência de dispositivos que operam na mesma faixa. Porém, com tecnicas e ~={orange}CSMA/CA=~ e ~={orange}Espalhamento Espectral=~ é possível aumentar as chances de coexistência.

~={cyan}Endereçamento=~

-  Endereço de 64 - é o endereço fixo de identificação do módulo, no momento da sua fabricação. Ele é único para cada dispositivo e não possuem o mesmo valor.

-  Endereço de 16 - é o endereço dinâmico que o módulo recebe ao ingressar em uma PAN. Ele é  endereço de rede, sendo fornecido pelo coordenador ou roteador.

![[Pasted image 20250419140116.png]]


~={cyan}Roteamento de Dados=~

-  Algumas transmissões unicast necessitam utilizar roteamento de mensagens, quando a distância de um dispositivo não for suficiente para se conectar com um coordenador;
-  Os dispositivos finais não utilizam os protocolos de roteamento por serem RFD. Eles enviam aos pais, em transmissão unicast e permitem que eles roteiem os pacotes de dados.

Tendo isso em vista, há três técnicas de roteamento.

![[Pasted image 20250419140813.png]]

![[Pasted image 20250419141748.png]]

![[Pasted image 20250419141941.png]]

![[Pasted image 20250419142238.png]]

![[Pasted image 20250419142559.png]]

![[Pasted image 20250419142822.png]]

![[Pasted image 20250419143204.png]]

![[Pasted image 20250419143223.png]]
![[Pasted image 20250419143309.png]]

![[Pasted image 20250419143504.png]]










































































































































