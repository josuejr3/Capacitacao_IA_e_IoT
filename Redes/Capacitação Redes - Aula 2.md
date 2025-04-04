
#### ~={cyan}                                         *Endereço privado e endereço público=~

| Endereço de rede e prefixo | RFC 1918 Intervalo de endereços privados |
| :------------------------: | :--------------------------------------: |
|         10.0.0.0/8         |        10.0.0.0 - 10.255.255.255         |
|        172.16.0.0/7        |       172.16.0.0 - 172.31.255.255        |
|       192.168.0.0.6        |      192.168.0.0 - 192.168.255.255       |
*Endereços usados privados que impedem que o host apareça na internet (isso não significa que é mais ou menos seguro que o público)*

Ambos os endereços, privado e público, são convenções. Essa convenção está na RFC 1918. 

IPv4 Privado - Os endereços não podem ser roteáveis na internet;
IPv4 Pública - Tem a capacidade de ser roteável na internet, ou seja, todo dispositivo de rede conectado a internet consegue interagir com aquele dispositivo.

~={red}Na prática não há uma característica que separe os dois tipos.=~

- A forma de "bloquear" o IP privado e deixar o acesso para o público é através de filtros.

![[Pasted image 20250403084716.png]]

-  NAT - Ferramenta para tradução de endereço privado para público (para comunicação com internet). 

O NAT não é exclusivo apenas do provedor, pode haver NAT na própria residência do usuário. O que não é viável, quanto mais tiver pior o desempenho da rede.

![[Pasted image 20250403085715.png]]

-  Residências atreladas ao mesmo provedor de internet possuem o mesmo endereço 192.168.0.0/24, por exemplo.
-  A maneira que a identificação específica é feita, ou seja, como é feita a diferenciação é através do IP que fica no link de WAN, normalmente um IP do protocolo PPoE. (~={red}Exemplo de NAT=~).
-  No provedor a um outro NAT que transforma modifica o tipo do IP.

---

~={blue}Maneiras de Atribuição de Endereçamento de IP=~

O endereçamento pode ser feito de maneira estática ou dinâmica. O que é comum em dispositivos finais é que o IP seja atribuído de maneira dinâmica, pois é mais simples para o usuário final (para isso usa-se o protocolo BHCP).

-  Endereços link local

	169.254.0.0/16 ou 169.254.0.1 a 169.254.255.254 são endereços locais de link e também são conhecidos como endereços de endereçamento IP privado automático (APIPA) ou endereços auto-atribuídos.

	~={red}(Gateway padrão)=~
	
	![[Pasted image 20250403090915.png]]

![[Pasted image 20250403093524.png]]

-  Switch (une todos os dispositivos conectados na rede local)
-  <mark style="background: #FF5582A6;">NAT de origem e de destino</mark>

---

-  SWITCHES CAMADA 2
-  VLAN (LAN VIRTUAL)

	-  Cada VLAN deve ter seu próprio endereçamento ou subrede de IP;
	
		![[Pasted image 20250403100549.png]]
	
	-  A VLAN separa o domínio de broadcast;

		![[Pasted image 20250403100937.png]]

- Os computadores ou dispositivos estão conectados a um switch (paralelepípedo) que por sua vez se conectam a um roteador.

<mark style="background: #D2B3FFA6;">Dúvida</mark>

		O que é um SWITCH?

		A VLAN subdivide o broadcast (todos os hosts) em grupos e ai os grupos só vão poder se comunicar entre si. Como por exemplo, acima PC1 só pode se comunicar com PC4, pois eles fazem parte da mesma VLAN. Porém, não pode se comunicar com PC6, mesmo que seja a mesma rede?

	Se a VLAN não faz parte do projeto, por exemplo, e o PC1 faz uma solicitação, significa que o PC1 iria "solicitar" ou fazer uma requisição em todos os dispositivos?

-  Normalmente as VLANs são configuradas nos Switchs (camada 2)
-  Quando há dispositivos finais conectados aos switchs dizemos que a configuração feita no switch é uma configuração de <mark style="background: #BBFABBA6;">PORTA DE ACESSO</mark>.
-  A transição "de volta" ou seja dos switchs mais abaixo (que se conectam com os PCs) para o switch que está conectado ao roteador tem uma interface de transporte (com tags para cada uma das VLANs).

![[Pasted image 20250403103015.png]]

---
####                                                              *~={cyan}IPv6=~*

No IPv6 não temos mais apenas 32 bits para representar o endereço, mas sim 128 bits no total.

![[Pasted image 20250403103736.png]]

-  Nem todos os dispositivos de IoT conseguem "abarcar" endereços IPv6;
-  Representação em formato hexadecimal;

> ~={green}Exemplo=~

![[Pasted image 20250403104107.png]]

~={cyan}Regras de Abreviações do IPv6=~

-  Omitir zeros à esquerda de qualquer seção de 16 bits;

> ~={green}Exemplo=~

	01AB - 1AB
	09f0 - 9f0
	0a00- a00
	00ab - ab

-  Dois pontos duplos pode substituir uma única sequênia contígua de um ou mais segmentos de 16 bits compostos exclusivamente por 0s.

	Só podem ser usados os "::" uma única vez no endereço. 

>  ~={green}Exemplo=~

![[Pasted image 20250403105504.png]]

-  Diferente do IPv4 o IPv6 não tem broadcast;
-  Tipo AnyCast - que é de um para o mais próximo. (Ex: usando o servidor DNS do Google);
	- Vários DNS do Google separados no mundo, porém ele usa o mais próximo.


~={cyan}Composição=~

![[Pasted image 20250403110011.png]]

A grosso modo

-  A identificação de Rede (Prefixo)
-  Identificação do Host (ID de interface)

~={blue}Unicast=~

![[Pasted image 20250403110211.png]]

-  Unicast global funciona como se fosse o IPv4 público (IP voltado para documentação de rede);
	- (Ex: corte de internet de um usuário);

-  Local exclusivo seria equivalente a um endereço IPv6 privado.

Esquema do endereço IPv6 - Unicast Global

![[Pasted image 20250403111055.png]]

-  Atribuição Dinâmica para endereçamento IPv6

![[Pasted image 20250403111303.png]]

---
