
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
		
---





























































































