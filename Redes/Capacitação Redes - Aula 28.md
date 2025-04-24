
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

Em relação aos saltos, um salto decodificado representa um símolo e esse pode representar um ou mais bits de dados e apresenta um total de 2^SF valores possíveis.

![[Pasted image 20250424091120.png]]

O ~={blue}fator de espalhamento SF=~ representa o número de bits da modulação. Na prática, ele representa a duração de um chirp. Sendo assim, quanto maior o SF, mais longo é o chirp e mais bits vão ser transmitidos por um chirp. A cada incremento no SF, o tempo no ar de um chirp dobra, como mostra a tabela acima. 

-  Maior sensibilidade -137 dBm
-  O SF7 consegue identificar até -123. Já se estivermos operando em SF12 conseguiremos identificar sinais que chegam mais fracos (se estivermos em um receptor).
-  Modulações como maior fator de espalhamento conseguem identificar sinais mais fracos.
























































































