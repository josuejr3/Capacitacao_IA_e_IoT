
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

























