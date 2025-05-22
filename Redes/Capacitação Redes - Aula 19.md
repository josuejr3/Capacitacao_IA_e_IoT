
####                                                        *~={cyan}ZigBee - Parte 1=~*

~={blue}REVISÃO=~

-  O comprimento de onda é inversamente proporcional à frequência.

Isso quer dizer que conforme a frequência aumenta o alcance do sinal irá diminuir na mesma proporção.

-  Teorema de Shannon: C = B * log2 (1 + S/N)

O teorema de Shannon nos informa que a capacidade máxima de transmissão de um canal de comunicação é dado pelo produto da largura de banda multiplicado pelo log na base dois de um somado razão de sinal ruído (S/N).

-  A razão sinal-ruído é a medida de qualidade para transmissão em um canal de comunicações, normalmente ela é dada em dB, quanto maior o valor, melhor é o canal e também maior é a capacidade de transmissão (bit/s).

-  Sinais transportados pelo ar devem ser modulados/modularizados ex: sinais AM, FM (Para portas analógicas).

-  Diagrama de modulação digital

![[Pasted image 20250418163244.png]]


~={blue}Bluetooth=~

-  O Bluetooth faz parte de uma PAN - Personal Area Network;
-  Comunicação digital, então será necessário modularização;
-  Possui baixo alcance;
-  O alcance de 10cm a 10m e a taxa de transmissão de 1 Mbps
-  O aumento da potência de transmissão pode ajudar a transmissão entre dois locais mais distantes, como por exemplo 100m.
 

~={blue}Wi-Fi=~
-  Protocolo que permite dispositivos se conectarem por meio de uma rede local (WLAN);
-  Pode ser usado com 2.4GHz, 5GHz e até frequências maiores. (Quanto maior a banda, maior a quantidade de bits/s)
-  O Wi-Fi é uma tecnologia WAN;


~={blue}ZigBee=~
-  É um protocolo de comunicação sem fio que consome baixa potência.


~={blue}Z Wave=~
-  Tecnologia sem fio baseada em RF (rádio frequência);
-  Possui boa confiabilidade;
-  Possui consumo de baixa potência.

> ~={green}Exemplo com algumas outras características dos protocolos de rede de comunicação sem fio com baixo alcance.=~

![[Pasted image 20250418164432.png]]

~={blue}SIGFOX=~
-  Utiliza uma banda de dados bastant estreita (UNB);
-  Conexão estável com os dados.


~={blue}LORA ALLIANCE =~
-  Trabalha na camada física;
-  Suporta transmissão bidirecional;


~={blue}NB-IOT=~
-  Baseada em comunicação narrowband (UNB);
-  Pode ser implementada em GSM, UMTS e LTE;
-  Largura de banda de 180 kHz.


~={blue}eMTC=~
-  Caracterísiticas baseadas em LTE;
-  Baixa potência.

 >~={green}Exemplo com algumas outras características dos protocolos de rede de comunicação sem fio com longo alcance.

![[Pasted image 20250418170036.png]]

~={cyan}IEEE 802.15.4=~

Diferente das pilhas que vimos antes, TCP/IP e OSI o ZigBee possui sua pilha própria, que pode ser encontrada a partir do IEEE 802.15.4

-  IEEE 802.15.4 é uma tecnologia de acesso sem fio para dispositivos de baixo custo e baixa taxa de dados que são alimentados ou funcionam por meio de baterias;

-  Várias pilhas de comunicação de rede utilizam essa tecnologia;

-  Essa tecnologia é encontrada em: automação residencial e predial, redes automotivas, redes de sensores sem fio industriais, brinquedos interativos e controles remotos.

-  O IEEE 802.15.4 tem pontos negativos em torn da confiabiliade e latência devido o algoritmo CSMA/CA. 

-  O CSMA/CA é um método de acesso em que o dispositivo "escuta" para garantir que nenum outro dispositivo seja transmitido antes de iniciar sua própria transmissão. 

~={cyan}IEEE 802.15.4 - PHY (câmada física)=~

<mark style="background: #D2B3FFA6;">Canais?</mark>

-  Taxa de transmissão de dados de 250 kbps, 100 kbps, 40 kbps e 20 kbps;
-  Define 27 canais
	-  16 canais de banda de 2450 MHz;
	-  30 canais de banda de 915 MHz;
	-  3 canais de banda de 868 MHz
-  Pode usar DSSS quando está operando em baixa frequência 868/91 MHz com uma modulação de BPSK ou O-QPSK;
-  Pode usar PSSS (Parallel Sequence Spread Spectrum) quando opera em baias frequências com a modulação BPSK ou ASK;
- Utiliza DSSS quando opera em frequencia de 2450 MHz com modulação de O-QPSK.

> ~={green}Exemplos: rede de sensores usam poucos bits para fazer um acionamento de sensor por exemplo=~

O IEEE 802.15.4 da base para operação de diversas tecnologias de comunicação

-  ZigBee;
-  6LoWPAN;
-  ZigBee IP;
-  ISA100.11A;
-  WirelessHART;
-  Thread.

---

~={cyan}ZigBee=~

-  O nome é basicamente uma referência a movimentação de abelhas;
-  Não foi lançado com um padrão típico como uma RFC;
-  A ZigBee Alliance é um grupo de indústrias responsável por certificar a interoperabilidade entre fornecedores e é basicamente quem desenvolve o ZigBee para ser uma forma de solução de IoT.
	- A ZigBee Alliance tem como objetivo definir camadas de software de rede, segurança e aplicação;
	- Fornecer testes de interoperabilidade e conformidade;
	- Promover a marca ZigBee globalmente para aumentar a difusão no mercado;
	- Gerenciar a evolução da tecnologia.

- Soluções ZigBee são voltadas para objetos e sensores inteligentes que possuem baixa largura de banda e baixa necessidade de energia. 
- O ZigBee deve funcionar, interoperar, mesmo que fornecedores diferentes possam fabricá-los.

	Pilha ZigBee

![[Pasted image 20250418173846.png]]

Lembrando que MAC Layer é a camda de transporte de acesso ao meio.

~={orange}Redes ZigBee=~

-  Coordenador (ZC) - inicia e controla a rede, é a entidade mais importante
-  Roteador (ZR) - dispositivos que estendem a cobertura da rede, contornam obstacúlos e podem se conectar ao coordenador ou outros roteadores.
-  Dispositivos Finais (ZED) - recebem ou enviam mensagens, porém não conseguem executar alguma operação de roteamento. Eles devem estar conectados ao coordenador ou roteador.

![[Pasted image 20250418175131.png]]

![[Pasted image 20250418175342.png]]

![[Pasted image 20250418175534.png]]

![[Pasted image 20250418175654.png]]














































