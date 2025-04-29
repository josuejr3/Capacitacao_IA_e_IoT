
#####                                                             <span style="color:rgb(0, 255, 64)">Bluetooth - Parte 1</span> 

###### <span style="color:rgb(0, 255, 64)">Histórico e Versões</span>

-  Inicialmente foi criado para substituir cabos de curta distância, como cabos de mouse e fones.
-  Existem dois tipos de dispositivos Bluetooth
	-  Bluetooth Classic (~={cyan}BR/EDR=~) - usado em alto falantes sem fio, sistemas de entretenimento automotivo e fones de ouvido.
	-  Bluetooth de baixa energia (~={cyan}BLE=~) - foi introduzido na versão 4.0, é usado em aplicações que costumam ter a energia como um fator crucial, ou seja, dispositivos alimentados por bateria em que pequenas quantidades de dado são transferidas e com pouca frequência.

<mark style="background: #FF5582A6;">Obs:</mark>

Os dois tipos de dispositivos bluetooth são incompatíveis entre si, embora compartilhem a mesma marca e até o mesmo documento de especificação.  

Um dispositivo bluetooth classic não pode se comunicar (diretamente) com um dispositivo BLE. É por esse motivo que alguns smartphones e aparelhos, optam por implementar os dois tipos. Esses dispositivos são conhecidos como dispositivos bluetooth de ~={blue}Modo Duplo=~. 

![[Pasted image 20250428230012.png]]

*Exemplos de dispositivos com BLE e Bluetooth Classic*

---

O BLE as vezes é chamado de Bluetooth Smart ou BTLE e confundido com o Bluetooth 4.0, já que ele incluia os dois tipos de bluetooth.

-  Ambos os dispositivos operam no mesmo espectro de frequência, (a banda industrial, Científica e Médica (ISM) de 2.4 GHz)

-  Em IoT o bluetooth mais popular, foi o BLE justamente por ele trabalhar com baixa energia, que é o que acontece em IoT quando usamos sensores e atuadores.

-  A partir da versão 5 (5.0) do Bluetooth a maioria dos recursos e melhorias foi levada para o tipo BLE.

-  ~={blue}Bluetooth Mesh=~ - é uma implementação de bluetooth em redes e arquiteturas com malha. Ele é baseado no BLE e requer a pilha BLE completa. (Um software que atua como uma interface para outro softwrae ou hardware) para funcionar, mas não faz parte da especificação principal do bluetooth. (Voltado para camadas superiores)

	![[Pasted image 20250428231728.png]]

###### <span style="color:rgb(0, 255, 64)">Características Gerais sobre o BLE</span>

-  Espectro de frequência ocupado é: 2,400 ~ 2,4835 GHz.
-  O espectro de frequência é segmentado em 40 canais de "2 MHz" de largura;
-  A taxa de dados máxima suportada pelo rádio (introduzida na versão 5 do Bluetooth) é 2 Mbps;
-  O consumo de energia pode variar a depender da implementação e aplicação e dos parâmetros BLE. Entretanto, normalmente o pico de corrente em um chipset BLE durante transmissão não ultrapassa 15mA;
-  Em relação a segurança, ela é opcional e cabe ao desenvolvedor do dispositivo implementar;
-  Para operações de criptografia, o BLE usa AES CCM com uma chave de 128 bits;
-  O BLE foi projetado para uma baixa taxa de transferência de dados. Se submetido a aplicações que requerem alta taxa,  a promessa de ser de baixo consumo de energia será comprometida;
-  Quando falamos em BLE, dizemos que são compatíveis entre si, entretanto, a comunicação pode ser limitada devido as características da versão mais antiga.

> ~={green}Exemplo=~

Um dispositivo bluetooth 5 pode se comunicar com um 4.1 BLE, mas os recursos específicos do 5 não vão ser suportados. 

![[Pasted image 20250428233715.png]]

###### <span style="color:rgb(0, 255, 64)">Aplicações</span>

![[Pasted image 20250428233901.png]]

###### <span style="color:rgb(0, 255, 64)">Limitações do BLE</span>

![[Pasted image 20250428234620.png]]

![[Pasted image 20250428234758.png]]

<mark style="background: #D2B3FFA6;">Então no final das contas não é uma transmissão menor?</mark>


































































































































