
####                                                 *~={cyan} Fundamentos de Sistemas Embarcados=~*

~={blue}Arquitetura do Dispositivo Final (Sistema Embarcado)=~

-  É o dispositivo que se conecta aos sensores e atuadores, além de se comunicar à uma rede de comunicação.

![[Pasted image 20250404091042.png]]

~={blue}Componentes Básicos de IoT=~

~={cyan}GATEWAY=~

Além do dispositivo final, temos um gateway. Em IoT alguns dispositivos conseguem se conectar diretamente à internet (device-to-cloud). Porém, outros não possui uma conexão nativa, por esse motivo é necessário usar algum mecanismo que auxilie (LoRa, ZigBee).

Para isso, o dispositivo final envia os dados para o dispositivo gateway e esse último que envia os dados para internet.

![[Pasted image 20250404091629.png]]

~={cyan}MIDDLEWARE=~

Middleware são componentes de softwares intermediários. É basicamente quando o dispositivo se conecta diretamente ao servidor da aplicação através de (rede wifi, rede móvel...) e envio os dados capaturados e esses dados são mostrados em uma interface. 

~={red}Obs: não é ideal ter essa ligação "direta". Por exemplo, um sensor que captura informações de temperatura, as informações não são exclusivas apenas para uma única aplicação, as podem funcionar para outras.=~

![[Pasted image 20250404092214.png]]

-  O middleware como software intermediário pode ser visto como a seguinte situação: o hardware deseja enviar uma informação e solicita ao middleware para verificar se o dispositivo que deve receber está conectado - o middleware recebe essa mensagem, identifica, e "avisa". 
-  O Middleware funciona como se fosse um "filtro" ou "comunicado";

![[Pasted image 20250404093302.png]]

Na imagem acima vemos uma plataforma de middleware que é chamada de dojot. Ela facilita a criação de soluções IoT.

~={blue}Mas o que o dojot faz?
=~
-  Gerenciamento de dispositivos (registro, autenticação, etc);
-  Recebimento e envio de dados para dispositivos IoT;
-  Armazenamento e visualização de dados;
-  Criação de fluxos de processamento (lógica de negócio) usando Node-RED;
-  APIs REST e MQTT para comunicação;
-  Multi-tenant (suporte a mútplos usuários/ambientes isolados);
-  Dojot pode ser executado na nuvem ou borda;


~={cyan}EDGE / FOG COMPUTING
=~
Essas duas se referem a qual local os dados vão ser processados.

![[Pasted image 20250404094910.png]]

-  Edge computing - basicamente é quando o processamento dos dados pode ser feito a partir dos dispositivos "mais próximos" fisicamente dos dispositivos finais. Não havendo a necessidade do dado chegar na nuvem, ser processado para depois retornar. Isso torna uma resposta mais rápido para os atuadores.

> ~={green}Exemplo em redes 5G=~

![[Pasted image 20250404095215.png]]

> ~={green}Exemplos=~

![[Pasted image 20250404100107.png]]

<mark style="background: #D2B3FFA6;">Dúvida</mark>

**Socket** TCP/UDP? 

---

~={cyan}Definição de Sistemas Embarcados=~

-  Sistema computacional embarcado **vs** sistema de **propósito geral**
-  Definição para leigos:
	-  Sistemas embarcados são coisas que executam software, mas **"não são computadores"**

> ~={green}Exemplos=~

-  Fechadura inteligente;
-  Lâmpada inteligente;
-  Brinquedo;
-  Alexa;

~={blue}Certo, mas o que diferencia um sistema embarcado de um sistema de propósito geral?
=~
-  Sistemas Embarcadsos são para aplicações específicas, não possuem nenhum mecanismo de customização, ou então muito poucos;

- Isso implica que o sistema pode ser projetado de forma que seja bem otimizado;

-  Implementação
	-  Hardware dedicado - desenvolver o próprio chip;
	-  Dispositivo programável - uso de microprocessadores e controladores que já existem;

	A escolha de como vai ser feita a implementação vai depender das seguintes características
	-  Custo;
	-  Tecnologia;
	-  Flexibilidade;
	-  Otimização de uso de recursos;

	-  Microcontrolador vs Microprocessador
		-  Custo;
		-  Tamanho;
		-  Poder computacional;
		-  Recursos de software;
		-  Consumo de Energia;
	
		Qual microcontrolador escolher?
			-  Requisitos de processamento e memória
				1. Ex1: TM4C - 80MHz, 32-bits, 32KB RAM;
				2. Ex2: PIC12F508 - 4MHz, 8-bits, 25B RAM;
			- Interfaces de I/O disponíveis.

-  Desafios
	-  Tentar executar tarefas críticas;
	-  Interagem como "mundo real" por meio de sensores e atuadores;
	-  Interface com mundo físico pode trazer desafios adicionais, como por exemplo:
		-  Segurança;
		-  Teste/debug;
		-  Operação autônoma.

	-  Restrição de recursos
		-  Processamento;
		-  Memória;
		-  Interfaces de I/O;

	-  Trade-offs (relação de compromisso / basicamente ganha em um atributo e perde em outro)
		-  O que pode implicar uma ~={red}redução de uso de memória?=~
		-  O que podemos implicar uma ~={red}redução no tempo de processamento?=~

	-  Consumo de Energia
		-  Alimentação por pilhas/baterias/colheita de energia
		![[Pasted image 20250404110802.png]]
				























































































































