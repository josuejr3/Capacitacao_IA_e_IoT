
#####                                                                <span style="color:rgb(0, 255, 64)">Bluetooth - Parte 2</span> 

###### <span style="color:rgb(0, 255, 64)">Conexão</span> 

Um sistema bluetooth pode ser composto por até 8 dispositivos, separados por uma distância de 10 metros entre si. Dentre esses dispositivos existem uma relação mestre escravo, com apenas um único mestre e até sete escravos ativos. 

Mesmo assim, ainda podem haver até 255 outros nós na rede, só que colocados em estado suspenso pelo mestre (hibernação), com objetivo de economizar energia. Um dispositivo que está suspenso, apenas responde a sinais de ativação ou sinalização (beacon) enviados pelo mestre.

![[Pasted image 20250429085627.png]]

-  Uma scatternet é um conjunto de piconets

![[Pasted image 20250429090209.png]]

###### <span style="color:rgb(0, 255, 64)">Introdução ao BLE</span>

-  Normalmente os dispositivos BLE consomem por volta de 10% da energia demandada por dispositivos baseados no Bluetooth clássico, embora esse valor possa variar um pouco para mais ou menos.

-  O BLE usa uma faixa de frequência de 2.4 GHz e 2.483 GHz om método de transmissão FHSS (Frequency hopping spread spectrum), igual o tipo clássico.

-  O que torna o BLE mais econômico é o conjunto de recursos e o sistema de modulação um pouco mais simples, um modo que mantém a tecnologia inativa até que seja "chamada" pelo mestre e uso de pacotes menores.

~={cyan}Topologia bluetooth=~

-  Ponto a ponto - celular e fone de ouvido;
-  Broadcast - um dispositivo se conecta com vários outros (ex: sistema que rastreia lotes de produtos em um estoque por meio de BLE beacons (dispositivos de localização));
-  Mesh - rede com muitos dispositivos que podem se comunicar uns contra os outros, topologia usada em sistemas de monitoramento. O bluetooth mesh possibilita milhares de dispositivos conectados. Além disso, essa topologia oferece suporte à comuniação device-to-device-to-device.

Em relação ao BLE ele possui alcance de até 100 metros, embora distâncias maiores sejam possíveis. No entanto, vale ressaltar que obstáculos podem atrapalhar o sinal. Esses obstáculos podem fazer o sinal ser reduzido a apenas 10 metros. Também pode ocorrer de vários dispositivos atuando na mesma faixa de frequência o que pode ocasionar o congestionamento.

-  BLE Beacons são dispositivos que usam BLE e permitem que dispositivos sejam ligados, identificados, rastreados ou monitorados.
-  Os beacons são semelhantes ao NFC, porém o NFC requer dispositivos afastados de poucos centimetros.
-  Anteriormente o rádio bluetooth e o rádio LTE não coexistiam, a partir da versão 4.1 do bluetooth eles passaram a coexistir.
-  BLE entrou oficialmente em IoT devido a eficiência energética.
-  Foi dado suporte a IPv6 para fornecer a capacidade de criar uma arquitetura Bluetooth Smart Internet Gateway (GATT)

###### <span style="color:rgb(0, 255, 64)">Arquitetura do BLE</span>

Pilha de protocolos do Bluetooth

![[Pasted image 20250429093030.png]]

-  Camada de aplicação

Depende do uso e refere-se a implementação sobre o perfil de acesso génerico e de atributo genérico. Essa camada vai ser como o aplicativo lida com os dados recebidos e enviados para outros dispositivos e a lógica por trás deles.

-  Camada de host

1. GAP;
2. GATT;
3. ATT;
4. SM;
5. L2CAP;
6. HCI.

-  Camada controller

1. HCI;
2. LL - Link Layer;
3. Direct Test Mode - DTM;
4. Camada física - PHY

HCI - Roda em duas camadas.

![[Pasted image 20250429093639.png]]

-  3 são canais (azul) são canais primários de anúncios, o restante (37) é usado para anúncios secundários e para transferência de dados (os dados que queremos transmitir) durante as conexões.
-  Os canais primários são responsáveis por fazer a conexão com outros dispositivos bluetooth (pareamento).

![[Pasted image 20250429094250.png]]
![[Pasted image 20250429094404.png]]
![[Pasted image 20250429094551.png]]

---

-  ~={blue}Camada de Link Layer=~

É a camada de enlace e é a camada que faz a interface com a camada física (rádio) e fornece a camadas de nível superior uma abstração e uma forma de interagir com o rádio (através de um nível intermediário chamado camada HCI). 

Essa camada
-  Gerencia estado do rádio e requisitos de tempo para atisfazer a especificação BLE;
-  Gerencia operações aceleradas por hardware como: CRC, geração de números aleatórios e criptografia.

~={blue}Estados de operação de dispositivos BLE=~
-  Advertising state (anúncio) - ele se mostra pra rede;
-  Scanning state (busca) - é feita uma busca por outro dispositivo bluetooth;
-  Connected state (conexão estabelecida) - o dispositivo que inicia a conexão é o mestre, o que estava anunciado é o escravo;
-  Standby - (não transmite dados);
-  Initiating -(estado em que um dispositivo de digitalização decide estabelecer uma conexão com um dispositivo que é anunciado);

![[Pasted image 20250429095617.png]]

~={cyan}Endereçamento Bluetooth=~

-  O endereçamento em dispositivos bluetooth é semelhante ao MAC e tem um total de 48 bits. Existem dois endereços principais, o público e o aleatório.

		Público - esse não muda, é fixo e vem programado de fábrica. Deve ser registrado no IEEE (igual ao endereço MAC de um dispositivo wi-fi ou ethernet).

		Aleatório - os fabricantes podem escolher se usam aleatório, ou público. Os aleatórios não exigem registro no IEEE. O endereço é programado no dispositivo ou gerado em tempo de execução e pode ser de dois subtipos diferentes.

		1. Static address
			- Gerado na inicialização OU permanece o mesmo durante a vida útil;
			- Não é possível alterar até desligar e ligar a energia;
			- Usado como substituto do endereço público.
		2. Private address
			- Endereço privado não resolvível:
				- Aleatório, temporário por um certo tempo;
				- Não é comumente usado.
			- Endereço privado resolvível:
				-  Gerao para privacidade;
				-  Gerado usando Identit Resolving Key (IRK) e um número aleatório
				-  Muda periodicamente (mesmo durante a vida útil da conexão).
				-  Usado para evitar ser rastreado por scanners desconhecidos.

~={cyan}Direct Test Mode (DTM)=~

Esse modo é o de teste direto, só é necessário para realizar testes de RF e é usado durante a fabricação e para testes de certificação. 

~={cyan}Host Controller Interface (HCI) Layer=~

-  Realiza uma interface entre a camada inferior (controller) e a superior (host);
-  As camadas podiam existir em chipsets diferentes.

![[Pasted image 20250429102044.png]]

-  A tarefa da camada HCI é retransmitir comandos do host para o controlador e enviar eventos de volta do controlador para o host.

> ~={green}Exemplos de mensagens:=~

Pacotes de comandos, configuração do controlador, solicitações de ações, controle de conexão e parâmetros de conexão.

~={cyan}Logical Link Control and Adaptation Protocol (L2CAP) Layer=~

Atua como uma camada de multiplexação de protocolo. Ele é emprestado do Bluetooth Classic e faz as seguintes tarefas.

-  Recebe vários protocolos das camadas superiores e os coloca em pacotes BLE padrão que são transmitidos às camadas inferiores abaixo dele.
-  Lida com a fragmentação e recombinação. Ele recebe os pacotes maiores da parte de camadas superiores e as divide em pedaos que cabem no tamaho máximo de carga útil do BLE suportado para transmissão. No receptor, ele recebe vários pacotes e combina em um pacote que pode ser manipulado pelas camadas superiores.

No BLE, essa camada lida com dois protocolos prinicpais: ATT e SMP (attribute protocol e security manager protocol).

![[Pasted image 20250429102952.png]]
![[Pasted image 20250429103044.png]]
![[Pasted image 20250429103248.png]]
![[Pasted image 20250429103446.png]]
![[Pasted image 20250429103808.png]]
![[Pasted image 20250429104115.png]]

~={cyan}Camada de Perfil de Acesso Genérico=~

![[Pasted image 20250429104342.png]]
![[Pasted image 20250429104512.png]]
![[Pasted image 20250429104847.png]]
![[Pasted image 20250429105112.png]]
![[Pasted image 20250429105342.png]]





























































































































































































