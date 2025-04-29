
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

Topologia bluetooth

-  Ponto a ponto - celular e fone de ouvido;
-  Broadcast - um dispositivo se conecta com vários outros (ex: sistema que rastreia lotes de produtos em um estoque por meio de BLE beacons (dispositivos de localização));
-  Mesh - rede com muitos dispositivos que podem se comunicar uns contra os outros, topologia usada em sistemas de monitoramento. O bluetooth mesh possibilita milhares de dispositivos conectados. Além disso, essa topologia oferece suporte à comuniação device-to-device-to-device.



























































