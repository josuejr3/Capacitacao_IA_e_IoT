#####                                                                   ~={cyan}*LoRa - 2=~

###### <span style="color:rgb(0, 255, 64)">Propriedades de modulação LoRa</span>

-  O ganho de processamento LoRa é introduzido no canal RF, multipplicando o sinal de dados com um código de dispersão ou sequência de chip. Ao aumentar a taxa do chip aumentamos os componentes de frequência do espectro total do sinal.

-  A energia do sinal total agora está espalhada por uma faixa mais ampla de frequências, permitindo que o receptor diferencie um sinal com uma relação sinal-ruído (SNR) mais baixa (ou seja, pior).

-  A quantidade de código de propagação aplicada ao sinal de dados originais é chamada de fator de propagação SF, a modulação LoRa tem seis fatores de propagação SF7 até SF12, quanto maior o fator mais longe o sinal vai.

	![[Pasted image 20250424222440.png]]

- Os fatores de propagaão da modulação LoRa inerentes ortogonais, isto é, significa que os sinais modulados com diferentes fatores de espalhamento e transmitidos em um mesmo canal de frequência ao mesmo tempo não interferem entre si, ~={red}eles são considerados ruidos uns para os outros=~.

-  Os sinais LoRa são robustos e resistentes a mecanismos de interferência dentro e fora da banda.  A modulação LoRa também oferece imunidade a multipercurso (espalhamento e reflexão é vários obstáculos) e desvanecimento, tornando-se ideal para ambientes urbanos e suburbanos onde ambos os mecanismos dominam.

-  Deslocamentos Doppler causam uma pequena mudança de frequência no eixo de tempo do sinal de banda base.

	<mark style="background: #D2B3FFA6;">canais de uplink e downlink?</mark>

![[Pasted image 20250424224930.png]]





































































































Site que fala sobre redes para IoT: https://www.thethingsnetwork.org