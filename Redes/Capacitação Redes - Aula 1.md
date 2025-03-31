
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

![[Pasted image 20250331162252.png]]

Em resumo, o modelo OSI é só uma referência, enquanto que o TCP/IP é o utilizado.

----

~={cyan}Meios Físicos=~

-  Quando estamos estudando os meios físicos, podemos ter o formato guiado e o não guiado.
Se o envio do sinal é eletrico, podemos usar meios metálicos.

1.  Cabos de cobre (ex: cabos de rede)

	Fios de cobre, são mais simples de instalar, possuem baixa resistência de corrente elétrica. Possui possibilidade de ocorrer interferência eletromagnética
	
2.  Fibra óptica

	Transporte de luz, não tem interferência de choque elétrico, interferência elétrica e eletromagnética. Além disso, a uma maior quantidade de dados que podem ser passados, como por exemplo: 10 Gigabit/segundo 

3.  Redes Wireless (meio não guiado)

	Ondas eletromagnéticas são usadas como meio físico. Ela não é confinada num meio físico. Porém, há problemas quando ocorrem fenomenos físicos, cmo por exemplo quando chuvas ocorrem. Apesar disso, ela traz mais flexibilidade e maior mobilidade aos usuários que fazem esse tipo de conexão.

~={cyan}Observando a camada 2 de Data Link Addresses=~

![[Pasted image 20250331164433.png]]

Nesse exemplo, podemos ver a comunicação entre um usuário e um destino à direita. Além disso, tem-se dispositivos intermediários, cada um possuindo sua~={red} placa de rede=~,  R1  e R2 possuem duas placas cada.

-  Todos os dispositivos possuem endereço lógico e endereço físico;
-  Cada "NIC", placa de rede, possui endereço físico;
-  Quando estamos usando "ethernet" o endereço de físico (MAC), pode ser visto através das cores de NIC que se alteram quando eu mudo de uma camada L2 para uma L3

---

~={cyan}Endereçamento Físico - MAC
=~
Endereço físico quando falamos de ethernet é chamado de endereço MAC. 

-  É um endereço físico que já vem de fábrica na placa de rede;
-  Está na camada de "enlace";
-  É composto por 48 bits, com representação em hexadecimal;
-  Os 24 bits mais significativos representam o ~={green}fabricante=~ (OU- Organizationally Unique Identifier)
-  Os 24 bits menos significativos vão representar uma identificação para a interface específica

> ~={green}Exemplo=~

![[Pasted image 20250331170945.png]]

-  A representação de endereço físico pode ser feita de diversas formas, com separação por :, . e até -.

> ~={green}Exemplos=~

-  00-05-9A-3C-78-00
- 00:05:9A:3C:78:00
- 0005.9A3C.7800

Além disso, existem MACs específicos para determinados para modos de aplicações específicos (~={cyan}MAC Unicast=~).

![[Pasted image 20250331171420.png]]

-  Protocolo ARP - Protocolo que faz o mapeamento de um endereço MAC a partir de um IP específico.

No caso do MAC Unicast, ele utiliza como MAC de destino uma faixa de valores em que o MAC que vai receber as informações está localizado. No caso acima, ele está com o MAC de destino 00-07-E9-42-AC-28

Já no Broadcast o destino é para todos que estão no dominio o MAC de destino vai estar com dígitos hexadecimais em F.

![[Pasted image 20250331171911.png]]

O Multicast funciona cm














































































































