![[Pasted image 20250408135742.png]]

- Muitos equipamentos utilizam TCP/IP.
- IPv6 não tem máscara de sub-rede ele tem cumprimento de prefixo.
-  Endereço ULA (Privado do IPv6) roteável em uma rede local;
-  Unicast global do IPv6 é similar ao IPv4 público por ser roteável.

![[Pasted image 20250408140109.png]]

-  O endereço de IPv6 link local, como o próprio nome já diz, é local. Com isso, ele não consegue atravessar pacotes por um roteador.
-  Não conseguimos rotear mesmo que localmente um endereço link local.

---
![[Pasted image 20250408140446.png]]

Acima é possível identificar na imagem a atribuição estática de um IPv6 com o endereço, o comprimento do prefixo (64 ou /64) e o gateway padrão.

~={cyan}Atribuição dinâmica
=~
*Processo de EUI-64*

-  Esse processo se baseia nos 48 bits do endereço MAC para fazer a atribuição dinâmica e automática para identificar uma interface;

-  O como o endereço MAC tem 48 bits e o endereço de IP deve ter 64 bits, o endereço MAC é "aberto" no meio e são inseridos 4 dígitos hexadecimais, ffff

-  Um dos bits é "iniciais" é alterado por questões de segurança.

![[Pasted image 20250410073850.png]]

~={cyan}Camada de Transporte=~

-  Os protocolos mais clássicos da camada de transporte são: TCP e UDP;

Comparação entre TCP e UDP

![[Pasted image 20250410074545.png]]

-  O TCP é orientado à conexão;
-  UDP é mais leve que o TCP;

~={cyan}Sobre as portas comuns em relação aos protocolos UDP e TCP
=~
-  Aqui, ao invés de endereço MAC de destino e endereço MAC de origem, chamamos de porta lógica de destino e de origem.
-  A porta lógica junto com endereço de IP é chamada de **socket**.

![[Pasted image 20250410074830.png]]

-  Para aumentar a segurança de um serviço, é comum alterarmos o valor da porta desse serviço 

> ~={green}Exemplo: um dispositivo SSH configurado rodando na porta 22.50 ao invés da porta 22 padrão.=~

![[Pasted image 20250410080335.png]]


~={cyan}Camada de Aplicação=~

![[Pasted image 20250410080407.png]]

---

~={cyan}Camada Física=~

-  O Espectro eletromagnético

![[Pasted image 20250410084106.png]]

A medida que aumentamos a frequência, nós diminuimos o comprimento de ondas.

![[Pasted image 20250410085740.png]]

-  Propagação no Espaço Livre de Ondas Eletromagnéticas

Em uma situação que estamos transmitindo uma determinada informação de uma antena para outra, podemos calcular o poder de recebimento da antena receptora.

$$
Pr = (PtGtGr(λ)^2) / (4πR)^2
$$

-  Pr - potência de recebimento da antena 2;
-  Pt - potência de transmissão da antena 1;
-  Gt - ganho de transmissão da antena 1;
-  Gr - ganho de recepção da antena 2;
-  λ - Comprimento de onda;
-  R - distância entre as antenas.

As ondas são difundidas em "linha reta" sem a ocorrência de fenômenos como refração e reflexão.

~={cyan}Fenômenos de ondas de RF=~

-  Absorção

É basicamente a capacidade que elemtos do ambientes, (sólidos ou líquidos), como paredes de concreto, tijolos e tanques de água tem de interromper a propagação da onda, fazendo com que ela perca energia e potência.

> ~={green}Exemplo: um sinal de 2.4 GHz tem 1/6 da potência original após se propagar através de uma parede de concreto. Esse mesmo sinal, perde apenas metade da potência original depois de passar pelo material Drywall=~

Tabela com exemplos de perda e atenuação de sinais

![[Pasted image 20250410091740.png]]

<mark style="background: #ABF7F7A6;">Lembrando que dB se refere ao ganho ou perda de potência de um sinal. (+10 dB ou -10 dB)</mark>

Espalhamento







































   










































































































































































































