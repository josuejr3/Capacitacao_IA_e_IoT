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

-  ~={cyan}Absorção=~

É basicamente a capacidade que elemtos do ambientes, (sólidos ou líquidos), como paredes de concreto, tijolos e tanques de água tem de interromper a propagação da onda, fazendo com que ela perca energia e potência.

> ~={green}Exemplo: um sinal de 2.4 GHz tem 1/6 da potência original após se propagar através de uma parede de concreto. Esse mesmo sinal, perde apenas metade da potência original depois de passar pelo material Drywall=~

Tabela com exemplos de perda e atenuação de sinais

![[Pasted image 20250410091740.png]]

<mark style="background: #ABF7F7A6;">Lembrando que dB se refere ao ganho ou perda de potência de um sinal. (+10 dB ou -10 dB)</mark>

- ~={cyan}Espalhamento=~

O espalhamento ocorre quando o comprimento de onda do sinal eletromagnético é maior do que as dimensões do meio envolvido. 

O sinal eletromagnético vai sofrer um espalhamento e isso faz com que ocorra uma degradação substancial do sinal e até mesmo causar a perda do sinal recebido.

![[Pasted image 20250410092816.png]]

-  ~={cyan}Reflexão=~

Modificação da direção da onda, quando ela retorna ao meio original após atingir um meio com caracterísitcas diferentes.

As refleões de onda podem ocorrer em situações como:

-  Camadas atmosféricas (temporárias) - enlaces ponto a ponto e ponto multiponto;
-  Obstruções - paredes, pisos e objetos - propagação indor;
-  Solo (permanentes) - enlaces ponto a ponto e ponto multiponto.

![[Pasted image 20250410093850.png]]

-  ~={cyan}Multipercurso=~

É o fenômeno de propagação que resulta em dois ou mais caminhos de um sinal chegando a uma antena receptora ao mesmo tempo.

Em locais internos temos por exemplo: **corredores**, mesas, pisos, armários entre objetos sólidos e superficies metálicas. 

Já em ambientes externos o multipercurso pode ser causado por uma estrada plana um grande copro de água, um edifício ou condições atmosféricas.

<mark style="background: #ADCCFFA6;">Em resumo, várias componentes do sinal do RF chegam ao receptor através de vários caminhos.</mark>

![[Pasted image 20250410094007.png]]

O problema é que essas componentes chegam em tempos distintos e também com fases diferentes.

~={cyan}Refração=~

A refração é basicamente a curvatura de um sinal de RF ao passar por um meio com uma densidade diferente, fazendo com que a direção da onda mude. Esse fenômeno ocorre na maioria das vezes como resultado das condições atmosféricas.

As três causas mais comuns de refração são:
-  Vapor d'água;
-  Mudanças na temperatura do ar;
-  Mudanças na pressão do ar.

![[Pasted image 20250410094847.png]]

~={cyan}Difração=~

A difração é a curvatura de um sinal de RF em torno de um objeto (enquanto a refração é a curvatura de um sinal ao passar por um meio). A difração é a curva e a propagaão de um sinal de RF quando ele encontra uma obstrução.

As condições para que o fenômeno ocorra vão depender inteiramente da forma, tamanho e material obstrutivo, assim como as caracterísitcas do sinal de RF, como polarização, fase e amplitude.

Normalmente a difração ocorre quando há um bloqueio parcial do sinal de RF.

![[Pasted image 20250410095243.png]]

---

Meios Guiados Metálicos

-  Cabo de par trançado não blindado (UTP)
![[Pasted image 20250410095902.png]]
-  Cabo de pares Trançados blindados (STP)
![[Pasted image 20250410095916.png]]
-  Cabo coaxial
![[Pasted image 20250410095932.png]]
Esse último usado em antenas.


![[Pasted image 20250410100038.png]]

~={blue}Conectores e Pinagem=~

Conectores RJ45

![[Pasted image 20250410100154.png]]























































































































   










































































































































































































