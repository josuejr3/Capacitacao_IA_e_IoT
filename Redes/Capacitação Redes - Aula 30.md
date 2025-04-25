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

-  Em redes LoRaWAN o ADR é um mecanismo de taxa de dados adaptável, o objetivo dele é economizar a energia da bateria dos nós finais LoRaWAN.

###### <span style="color:rgb(0, 255, 64)">Segurança em dispositivos LoRaWAN</span>

Em dispositivos LoRaWAN existem dos elementos principais em relação à segurança: o procedimento de associação e autenticação de mensagens. O procedimento de associação estabelece autenticação mútua entre um dispsitivo final e a rede LoRaWAN à qual ele está conectado. 

Somente dispositivos autorizados têm permissão para se conectar à rede. LoRaWAN MAC e mensagens de aplicações são autenticadas por origem, protegidas por integridade e criptografadas de ponta a ponta (ou seja, do dispositivo final para o servidor de aplicações e vice-versa).

Os recursos de segurança garantem que:

-  O tráfego de rede não foi alterado;
-  Apenas dispositivos legítims estão conectados à rede LoRaWAN;
-  O tráfego de rede não pode ser ouvido (sem escutas);
-  O tráfego de rede não pode ser capturado ou reproduzido.

![[Pasted image 20250424231507.png]]

![[Pasted image 20250424231945.png]]

![[Pasted image 20250424232044.png]]

###### <span style="color:rgb(0, 255, 64)">Formato do pacote físico</span>

O pacote físico é a unidade que é transportada de um ponto a outro, é basicamente o dado. Esse pacote é definido como uma sequência de bits que é modulada e transmitida.

O pacote é formado pelas seguintes partes

-  Preâmbulo
	Sequência de simbolos identicos que servem para a detecção e sincronização do receptor.

-  CR de cabeçalho
	-  Cabeçalho
		É um campo opcional, porém possui seu próprio campo corretor de erro
	-  CRC
		Esse campo serve para identificar erros no cabeçalho
-  CR da carga
	-  Carga
		Payload em si que são os bits de carga, ou seja dado propriamente dito.
	-  CRC
		Outro campo que serve para fazer identificação de erro do payload.

Com a definição desses conceitos podemos verificar a *Taxa de Codificação* (CR) que é a razação de bits entre o tamanho do campo e o tamanho total do campo mais o CRC.

-  Para o cabeçalho o valor é sempre de 4/8
-  Para a carga vai ser sempre 4/(4+x) com x estando entre 1 e 4.

![[Pasted image 20250424233702.png]]

###### <span style="color:rgb(0, 255, 64)">Classes de Dispositivos</span>

Os dispositivos finais baseados em LoRa podem operar em três modos diferentes, dependendo de sua classe.

-  Todos os dispositivos devem suportar classe A;
-  Dispositivos classe B, suportam B e A;
-  Dispositivos classe C suportam os três modos.

Os modos de operação se relacionam a maneira de como os dispositivos se comunicam com a rede.

O primeiro modo ou classe é fundamental, os outros fazem apenas modificaão na forma de recepção de pacotes do dispositivo final, junto com a adição de alguns comandos de controle da camada MAC. 

---

-  Classe A
Tem janelas de recepção de pacotes abertas apenas após o envio de mensagens, o que torna ela mais eficiente energeticamente, pois o demodulador não é passivo e consome energia quando espera por um sinal. Essas janelas de recepção da classe Acontinuam sendo abertas em outros modos de operação. ~={red}Só pode receber dados após enviar uma mensagem (uplink.). Fora os momentos de recepção o dispositivo permanece dormindo e economizando bateria.=~

	- Transmissão half-duplex

![[Pasted image 20250424235643.png]]
![[Pasted image 20250425000232.png]]
![[Pasted image 20250425000346.png]]
![[Pasted image 20250425000755.png]]
 
- Classe B
Semelhante a classe A com a diferença apenas da quantidade de janelas de recepçãoo que possibilita a recepção de mais pacotes, porém com um consumo de energia um pouco maior que a de A.

![[Pasted image 20250425001632.png]]

![[Pasted image 20250425002016.png]]



























-  Classe C 
Uma janela de recepção é aberta continuamente quando a janela padrão da classe A não está aberta. Fazendo a classe C ser a que apresenta maior consumo de energia e maior capacidade de recepção de dados.









































































































































































Site que fala sobre redes para IoT: https://www.thethingsnetwork.org