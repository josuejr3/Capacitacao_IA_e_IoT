
#####                                                                   ~={cyan}*LoRa=~

###### <span style="color:rgb(0, 255, 64)">Características</span> 

- Baixa potência (fornecimento de energia);
- Longo alcance (baixa taxa de dados);
- Baixo custo financeiro;

O LoRa é uma técnica de modulação sem fio derivada da tecnologia "Chirp Spread Spectrum" ou CSS. Ele codifica as infomações em ondas de rádio usando pulsos chirp, bastante semelhante à forma como golfinhos e morcegos se comunicam.

A transmissão modulada LoRa é robusta contra distúrbios e pode ser recebida em grandes distâncias. Ela é ideal para aplicações que transmitem pequenos blocos de dados com baixa taxa de bits, sendo adequado paa sensores e atuadores que operam com baixa potência.

-  Uma característica do LoRa é que ele pode ser operado em bandas de sub-gigahertz livres de licença por exemplo 915 MHz, 868 MHz e 433 MHz. Entretanto, o LoRa pode operar em 2.4 GHz para taxas mais altas, porém, com diminuição do alcance. Esse tipo de operação é vista mais em estudos científicos, aplicações médicas e industriais (ISM).

###### <span style="color:rgb(0, 255, 64)">Pilha de comunicação - Lora</span>

![[Pasted image 20250424083427.png]]

De baixo para cima, temos

Camada Física

-  Bandas que podem ser utilizadas, muitas vezes separadas por ISM;
-  Utilização em ISM;
-  Funções de modulação do LoRa

Camada de MAC

-  Classes de dispositivos que podem se comunicar;
-  Opções de controle de acesso ao meio;
-  O LoRaWAN;
-  Aplicações que podem rodar em cima do LoRa.

---

-  O LoRa utiliza o *~={blue}espalhamento espectral=~*
-  Ganho de processamento em técnicas de espalhamento espectral

	![[Pasted image 20250424085607.png]]

-  O ganho de processamento espectral no LoRa.

	![[Pasted image 20250424085643.png]]
	-  SF sendo um fator de espalhamento (pode ter de 7 até 12);
	-  BW sendo a largura de banda de modulação.

###### <span style="color:rgb(0, 255, 64)">Modulação LoRa</span>

Em dispositivos LoRa um sistema final possui um módulo de rádio responsável pela codificação/decodificação das informações em um sinal. O sinal é transmitido ou recebido por um *~={blue}gateway=~* que também possui o mesmo módulo que é capaz de modular/demodular o sinal. Dessa forma, a comunicação entre sistema final e gateway é bidirecional e estes dispositivos que se comunicam são chamados de ~={blue}*Transceivers*=~.

![[Pasted image 20250424090322.png]]

![[Pasted image 20250424090725.png]]

-  Se a frequência aumenta temos um UP-CHIRP
-  Se a frequência diminui temos um DOWN-CHIRP

Em relação aos saltos, um salto decodificado representa um símbolo e esse pode representar um ou mais bits de dados e apresenta um total de 2^SF valores possíveis.

![[Pasted image 20250424091120.png]]

O ~={blue}fator de espalhamento SF=~ representa o número de bits da modulação. Na prática, ele representa a duração de um chirp. Sendo assim, quanto maior o SF, mais longo é o chirp e mais bits vão ser transmitidos por um chirp. A cada incremento no SF, o tempo no ar de um chirp dobra, como mostra a tabela acima. 

-  Maior sensibilidade -137 dBm
-  O SF7 consegue identificar até -123. Já se estivermos operando em SF12 conseguiremos identificar sinais que chegam mais fracos (se estivermos em um receptor).
- <mark style="background: #FF5582A6;">O valor acompanhado do SF, ex: SF7 significa que a formação do simbolo é feita com 7 bits e o simbolo é a onda que vai ser transmitida de maneira física pelo ar, ou seja o chirp.</mark>

	Os tipos de onda em um SF são dados por 2^(valor) = X
	Ex: para SF7

	2^(7) = 128 símbolos, também chamados de formatos de onda. Isso possibilita o envio de mais bits.

-  Modulações como maior fator de espalhamento conseguem identificar sinais mais fracos.
-  Time on air é o "tempo de viagem" e a medida que eu aumento a quantidade de dados eu aumento a latência.

![[Pasted image 20250424092340.png]]

![[Pasted image 20250424092450.png]]

###### <span style="color:rgb(0, 255, 64)">Fatores de Espalhamento - Taxa de Dados</span> 

-  Fatores de propagação mais baixos fornecem uma taxa de bits mais alta do que fatores de propagação mais altos para uma largura de banda fixa e taxa de codificação. Ex: o SF7 tem uma taxa de bits mais alta que SF12.
-  Dobrar a largura de banda também dobra a taxa de bits para um fator de propagação fixo e taxa de codificação.
-  Na tabela a baixo há as taxas de bits calculadas com SF7, a taxa de codificação CR = 1 para larguras de banda 125, 250 e 500 kHz.

	![[Pasted image 20250424094034.png]]

-  A duração da bateria está ligada diretamente ao fator de propagação. Pois, fatores de propagação mais altos resultam em tempos ativos mais longos para transceptores de rádio, fazendo com que a bateria diminua sua duração.
-  O fator de espalhamento também está relacionado com o tempo no ar
-  Quanto maior o fator de espalhamento, maior será a distância que o sinal irá percorrer. Ex:um sinal modulado com SF12 percorre uma distância maior que SF7. Porém, a taxa de transmissão será diminuida.

~={blue}RSSI E SNR=~

-  RSSI é um indicador de intensidade do sinal recebido. É uma medição relativa que ajuda a determinar se o sinal recebido é forte o suficiente para obter uma boa comunicação sem fio com o transmissor. É medido em -dBm e é importante para dispositivos finais e gateways, já que LoRa é uma conexão bidirecional. Quanto mais próximo de zero, mais forte é o sinal.

	Fatores que influenciam o RSSI

	-  Perda de caminho;
	-  Ganho de antena;
	-  Perda de cabo/conector

-  SNR é a relação sinal-ruído, ou seja, é a relação entre a potência do sinal recebido e o piso de ruído. A SNR é comumente usada para determinar a qualidade do sinal recebido. 
-  A SNR pode ser calculada usando a seguinte fórmula e geralmente é expressa em decibéis (dB)

	SNR (db) = Preceived_signal (dBm) - Pnois(dBm)

-  Se a SNR for positiva significa que a potência do sinal é maior do que a potência do ruído.
-  Se a SNR for negativa significa que a potência do sinal é menor do que a potência do ruído.
-  Se a RSSI estiver acima do piso do ruído, o receptor pode facilmente demodular o sinal.
-  Se a RSSI estiver abaixo do piso do ruído, teoricamente não é possível fazer a demodulação. Entretanto, devido ao espalhamento no LoRa, conseguimos demodular.

##### <span style="color:rgb(0, 255, 64)">LoRaWAN (Long Range WAN)</span>

O LoRaWAN é um protocolo de camada de acesso ao meio MAC que é construído sobre a modulação LoRa. É uma camada de software que define como os dispositivos usam o hardware LoRa.

-  O LoRaWAN é adequado para transmitir *payloads* de tamanho pequeno (como dados de um sensor) em longas distâncias. 

![[Pasted image 20250424101409.png]]
###### <span style="color:rgb(0, 255, 64)">Características</span>

-  Ultra baixo consumo de energia - os dispositivos finais LoRaWAN são otimizados para operar no modo de baixo consumo de energia e podem durar até 10 anos com uma única bateria de célula tipo moeda.

- Longo alcance - os gateways podem transmitir e receber sinais a uma distância de mais de 10km em áreas rurais e até 3km em áreas urbanas densas.

-  Penetração interna profunda - as redes LoRaWAN podem fornecer cobertura interna profunda e cobrir facilmente edifícios de vários andares.

-  Espectro livre de licença - não é necessário pagar taxas caras de liença de espectro de frequência para implementar uma rede LoRaWAN.

-  Geolocalização - uma rede LoRaWAN pode determinar a localização de dispositivos finais usando triangulação sem a necessidade de GPS. Um dispositivo final LoRa pode ser localizado, se pelo menos três gateways captarem seu sinal.

-  Alta capacidade - os servidores de uma rede LoRaWAN lidam com milhões de mensagens de milhares de gateways.

![[Pasted image 20250424102159.png]]

![[Pasted image 20250424102505.png]]

-  Na comunicação dos nós finais e o gateway usamos basicamente o que estudamos na camada física.
-  A partir do gateway, podemos usar TCP/IP

![[Pasted image 20250424103033.png]]

































































































































