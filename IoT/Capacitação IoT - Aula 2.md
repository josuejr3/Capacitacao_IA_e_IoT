
#### ~={cyan}Relembrado...=~

Apesar de IoT estar bastante present no nosso dia a dia, ainda há barreiras muito importantes em relação a adoção de IoT Industrial, como mostra a imagem abaixo.

![[Pasted image 20250330153042.png]]

Pela imagem, vemos que a maior preocupação da industria é a cibersegurança. Além disso, integralização com sitemas legados, falta de padronização e entre outros.

Alguns outros desafios são:

-  Segurança (confiabilidade e disponibilidade);
-  Privacidade (coleta e processamento de dados privados do usuário);
-  Interoperabilidade e Padrões (nível de interoperabilidade entre diferentes dispositivos de diferentes fabricantes);
-  Questões regulatórias (como os dados podem ser usados e responsabilização);
-  Economias Emergentes e Desenvolvimento (como lidar com as limitações de economias emergentes para permitir acesso global às oportunidades e benefícios da IoT).

#### ~={cyan}Arquitetura de IoT=~

Mas o que é arquitetura?

	Define a organização de um sistema

	1 - Quais as entidades?
	2 - Quais as responsabilidades?
	3 - Como as entidades se relacionam?

	Deve levar em conta requisitos e restrições

Trazendo para a área da computação, basicamente é termos a organização de um sistema computacional, como por exemplo um dispositivo IoT, aplicação que executa na nuvem, dispositivo intermediário e entre outras. Todas as entidades nesse sistema tendo responsabilidades definidas e como elas se relacionam.

~={blue}Fatores Importantes para Arquitetura de IoT=~

-  Escala (grande quantidade de dispositivos)
-  Segurança (maior exposição de dispositivos)
-  Restrições de Recursos (limitações de processamento, memória e comunicação)
-  Volume de Dados (geração massiva de dados por dispositivos IoT)
-  Suporte a Dispositivos Legados (equipamentos antigos que precisam ser integrados à IoT)
-  Tempo (suporte a operações de tempo real)

<mark style="background: #ABF7F7A6;">Escala</mark>

Esse tópico é visto em cidades inteligentes, as quais possuem milhares de *endpoints* para milhões de *endpoints* em uma determinada área. 

Desafios: endereçamento e identificação, conectividade (rede de acesso) e como o armazenamento e o transporte de dados é feito.

<mark style="background: #ABF7F7A6;">Segurança</mark>

A segurança é importante de ser estudada, pois podem ocorrer: ameaças relacionadas a comunicação dos dispositivos, ameaças ao ciclo de vida dos aparelhos IoT, ameaças ao acesso físico e também as relacionadas ao firmware dos dispositivos.

Para resolver parte de problemas de acesso e deixar os sistemas mais seguros, são utilizados diversos mecanismos que melhoram a segurança, sendo eles os seguintes:

-  **Autenticação** de todas as entidades envolvidas (ex: gateway = roteador, endpoint = celular, plataformas de serviços etc);
-  **Criptografia** de dados sensíveis; 
-  **Adequação a legislação** para proteção de dados;
-  **Monitoramento e detecção de anomalias** em dispositivos.

<mark style="background: #ABF7F7A6;">Restrições de Recursos</mark>

Como na maioria das vezes os dispositivos usam componentes de baixo custo, o poder de processamento também não é tão alto. 

-  **Processamento** (microprocessadores e microcontroladores de **baixo custo**);
-  **Armazenamento** (em alguns casos "poucos" KB de memória estão disponíveis);
-  Limitações de **rede** (taxa de bits, alcance, duty-cycle, disponibilidade);
-  Consumo de **energia** (dispositivos alimentados por **baterias**)

<mark style="background: #ABF7F7A6;">Volume de Dados</mark>

![[Pasted image 20250330161228.png]]

O volume de dados de dispositivos IoT crescem ao longo do tempo

Além disso, quando estamos falando de arquitetura é importante que os dados passem por filtragem e sumarização e essas etapas podem ser feitas ao longo da arquitetura.

Ademais, o processamento e resposta na ~={yellow}borda da rede=~ com objetivo de reduzir a latência. Por exemplo, eu não preciso de uma resposta imediata de um servidor, eu posso utilizar a resposta de um gateway como forma de ativar um atuador.

<mark style="background: #ABF7F7A6;">Suporte à Dispositivos Legado</mark>

<mark style="background: #ABF7F7A6;">Tempo</mark>


















































