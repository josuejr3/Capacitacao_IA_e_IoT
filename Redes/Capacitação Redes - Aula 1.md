
####                                                   *Introdução*

-  Connecting Things 
	-  Visão Geral
	-  Modelos OSI e TCP/IP
	-  Camada Física: Meios físicos, dispositivos sensores, atuadores, controladores, atividade interativa.

-  Slide 
	-  Camada de Enlace: Endereçamento Físico, Domínio de Colisão, Domínio de Broadcast;
	-  Camada de Rede: Endereçamento Lógico IPv4, NAT, ICMP e Ping, Atribuições de endereçamento de IP.

~={cyan}Computação na borda / neblina =~

Normalmente está mais próxima do usuário do que na nuvem (exemplos de usuário: torradeira inteligente, liquidificador inteligente, lâmpada inteligente e entre outros).

![[Pasted image 20250331153848.png]]

Os roteadores são considerados <mark style="background: #ABF7F7A6;">gateways</mark>. E esses roteadores fazem a conexão de uma rede controlada, para uma rede externa ou mais de uma rede externa.

-  Conexões na borda possuem baixa latência.

~={cyan}Modelo OSI=~

![[Pasted image 20250331160153.png]]

Caracterizado por uma pilha de protocolos. Esse modelo é utilizado para projeto, implantação e suporte de rede.

~={blue}Vantagens=~

	- Uma das vantagens é ter um projeto/planejamento estruturado
	- Estimulo da concorrência entre fabricantes

~={red}Obs: nem todos os projetos de IoT utilizam o projeto OSI, porém, ele serve de base=~

O modelo OSI está relacionado com o TCP/IP que é qual usamos de fato nas redes do dia a dia

![[Pasted image 20250331160821.png]]

A divisão em camadas, auxilia na detecção de problemas, pois a partir de um erro encontrado conseguimos classifica-lo em um dos níveis do TCP/IP ou OSI e com isso encontrar uma melhor solução para o problema.

-  Uma forma de detecar problemas na rede é utilizar ferramentas de teste de conectividade, que nesse caso, é o ~={cyan}Ping=~.

-  Camadas inferiores encapsulam camadas superiores de conexão, ou seja, a camada mais inferior encapsula todas as outras. (Além disso, as camadas acrescentam ~={red}cabeçalho=~ como por exemplo IP de origem e de destino).

<mark style="background: #FF5582A6;">Trouble shooting - pesquisar</mark>








































