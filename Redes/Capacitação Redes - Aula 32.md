
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








