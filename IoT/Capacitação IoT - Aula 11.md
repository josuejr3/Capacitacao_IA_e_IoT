
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


~={cyan}EDGE / FOG COMPUTING
=~























































