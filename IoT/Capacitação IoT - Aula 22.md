
##### <span style="color:rgb(0, 255, 64)">Relembrando GPIO no ESP32</span>

Entendendo como os periféricos são configurados no microncontrolador ESP32

Os códigos abaixo são usados para acesso de memória e GPIOs

```C++
#define GPIO_PIN0_INT_TYPE 0x00000007U
#define GPIO_PIN0_INT_TYPE_M (GPIO_PIN0_INT_TYPE_V << GPIO_PIN0_INT_TYPE_S)
#define GPIO_PIN0_INT_TYPE_V 0x00000007U
#define GPIO_PIN0_INT_TYPE_S 7

/** GPIO_PIN0_WAKEUP_ENABLE : R/W; bitpos: [10]: default: 0;
* set this bit to enable GPIO wakeup. (can only wakeup CPU from light-sleep Mode)
*/

#define GPIO_PIN0_WAKEUP_ENABLE (BIT(10))
#define GPIO_PIN0_WAKEUP_ENABLE_M (GPIO_PIN0_WAKEUP_ENABLE_V << GPIO_PIN0_WAKEUP_ENABLE_S)
#define GPIO_PIN0_WAKEUP_ENABLE_V 0x00000001U
#define GPIO_PIN0_WAKEUP_ENABLE_S 10

/** GPIO_PIN0_CONFIG : R/W; bitpos: [12:11]; default: 0;
* reserved
*/

#define GPIO_PIN0_CONFIG 0x00000003U
#define GPIO_PIN0_CONFIG_M (GPIO_PIN0_CONFIG_V << GPIO_PIN0_CONFIG_S)
#define GPIO_PIN0_CONFIG_V 0x00000003U
#define GPIO_PIN0_CONFIG_S 11
```

Entretanto, não há tanta necessidade desses códigos do jeito que estão escritos, pois há bibliotecas disponibilizadas pelo fabricante que facilitam o uso desses códigos. 

![[Pasted image 20250426132655.png]]

![[Pasted image 20250426133008.png]]

-  O gpio_config é uma função que faz a configuração do GPIO;
-  gpio_config_t é uma struct que contem todos os membros necessários que definem um GPIO, como resistores PULLUP E PULLDOWN, mascaras e interrupções. 
-  Passamos o gpio_config_t por referência para a função de configuração para poupar memória na pilha de execução e para ter acesso ao registrador.

```C
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"

// Definindo as variáveis dos leds e dos botões
#define BUTTON_0 GPIO_NUM_4
#define BUTTON_1 GPIO_NUM_15
#define LED_0 GPIO_NUM_21
#define LED_1 GPIO_NUM_19
#define LED_2 GPIO_NUM_18
#define LED_3 GPIO_NUM_5

// Setando os bits que vão ser configurados como saida (usando mascara) 1ULL - Unsigned long long 64 bits

#define GPIO_OUTPUT_PIN_SEL ((1ULL << LED_0) | (1ULL << LED_1) | (1ULL << LED_2) | (1ULL << LED_3))

// EX: Deslocando um 1 do LED_3 5 Vezes já que GPIO_NUM_5
// 000000000000000000000000000000000000001
// 000000000000000000000000000000000100000

// Cada LED terá de passar por uma opração dessa e após isso, preciso juntar tudo, por isso uso o operador |

// Setando os bits que vaão ser configurados como entrada (usando mascara) - (Botões)

#define GPIO_INPUT_PIN_SEL ((1ULL << BUTTON_0) | (1ULL << BUTTON_1))
// Função de configuração de todos os pinos e componentes

void setup(){

  // Configuração de LEDS
  gpio_config_t led_conf = {};
  led_conf.intr_type = GPIO_INTR_DISABLE;
  led_conf.mode = GPIO_MODE_OUTPUT;
  led_conf.pin_bit_mask = GPIO_OUTPUT_PIN_SEL;
  led_conf.pull_down_en = GPIO_PULLDOWN_DISABLE;
  led_conf.pull_up_en = GPIO_PULLUP_DISABLE;
  gpio_config(&led_conf);

  // Configuração de Botões
  gpio_config_t button_conf = {};
  button_conf.intr_type = GPIO_INTR_DISABLE;
  button_conf.mode = GPIO_MODE_INPUT;
  button_conf.pin_bit_mask = GPIO_INPUT_PIN_SEL;
  button_conf.pull_down_en = GPIO_PULLDOWN_DISABLE;
  button_conf.pull_up_en = GPIO_PULLUP_DISABLE;
  gpio_config(&button_conf);

}

void app_main() {
  setup();
  while (true) {
    gpio_set_level(LED_3, 1);
  }
}
```

##### <span style="color:rgb(0, 255, 64)">Software Embarcado - Interrupções</span>

###### ~={cyan}Conceitos Iniciais=~

O que é uma interrupção?

São semelhantes as funções, ou seja, fazem um desvio no fluxo do programa, porém a chamada não é explícita como nas funções. 

-  Permitem oferecer respostas a eventos assíncronos mesmo estando no meio da execução de alguma tarefa.
-  Dispositivos internos do micro-controlador também podem gerar interrupções
-  <mark style="background: #FF5582A6;">O tratamento de exceções é diferente do tratamento de interrupções
</mark>

		

Interrupções ocorrem quando algum evento assíncrono de hardware externo altera o fluxo do programa.

![[Pasted image 20250426150413.png]]

> ~={green}Exemplo=~

Um clássico exemplo são as transmissões de pacotes entre um microcontrolador e um transceptor. Sempre que o transceptor recebe um pacote ele cria uma interrupção para "avisar" que recebeu um pacote que deve ser lido.

Quando a interrupção é gerada, o programa principal para, a interrupção é trata e após isso o programa continua o fluxo.

---

Assim como em funções, antes da rotina de tratamento de interrupções ser finalizada há condições que precisam ser satisfeitas

-  O PC (program counter) deve conter o endereço da próxima instrução do bloco interrompido;
-  Os registradores precisam ter seus valores restaurados;

Chamamos essas duas técnicas de ~={blue}salvamento e recuperação de contexto=~. E essa técnica também é bastante usada quando estamos fazendo uso de múltiplos threads e processos.

---
###### <span style="color:rgb(0, 255, 64)">Configuração de GPIO na ESP32</span>

Toda função/rotina que trata interrupções deve seguir um formato específico. Como por exemplo um ponteiro void, um retorno também void.

-  O ponteiro pra void * void significa basicamente que eu posso receber o ponteiro para qualquer coisa. É um ponteiro genérico
-  IRAM_ATTR força os códigos a ficarem salvos na memória RAM, deixando o acesso mais rápido.
-  Qual o motivo do static?
-  Mesmo o parâmetro sendo ponteiro para void, é necessário fazer o casting para a variável que pretende-se receber.

```C
static void IRAM_ATTR gpio0_isr_handler(void *arg){
	uint8_t *v = (uint8_t*) arg;
	*v = 1;
}
static void IRAM_ATTR gpio1_isr_handler(void* arg){
	uint8_t *v = (uint8_t*) arg;
	*v = 0;
}
```

###### Configurando as Interrupções no ESP32

Por padrão os botões ficam em nível alto. Dessa forma, a interrupção será acionada sempre que ocorrer o nivel baixo nos botões, ou seja, quando forem pressionados.

```C
void setup(){
	...
	button_conf_intr_type = GPIO_INTR_LOW_LEVEL;
	...
}
void app_main(){
	...
	// install gpio isr service
	gpio_install_isr_service(ESP_INTR_FLAG_LOWMED);
	// hook isr handler for specific gpio pin
	gpio_isr_handler_add(BUTTON_0, gpio0_isr_handler, (void*) &valor);
	// hook isr handler for specific gpio pin
	gpio_isr_handler_add(BUTTON_1, gpio_isr_handler, (void*), &valor);
	...
}
```

###### <span style="color:rgb(0, 255, 64)">Problemas com códigos de execução concorrente</span>

Execução concorrente são trechos diferentes de código que vão intercalar o uso de um mesmo processador e podem compartilhar conteúdo. 

Esse fenômeno ocorre bastante em situações que usa-se multithread.

-  Dados compartilhados
	-  A comunicação entre as ISRs e o código da tarefa é feita por meio de ~={red}variáveis compartilhadas=~. (Em alguns casos pode ocorrer ~={red}condição de corrida=~)
	
	![[Pasted image 20250426161721.png]]

	O código apresenta problemas, um deles sendo a interrupção sendo gerada durante a verificação das temperaturas e a outra durante a atribuição. Nesse caso os novos valores seriam atribuidos na função de interrupção, porém, no programa principal eles estariam desatualizados.

<mark style="background: #D2B3FFA6;">Ao invés de usar variáveis comuns, poderiamos usar ponteiros e atribuir o valor para qual o ponteiro aponta? </mark>

-  Uma possível solução para resolver esse problema seria desabilitar as interrupções na ~={red}região crítica=~. (Porém pode causar problemas de temporização).

	-  Região crítica é o trecho de código em que estou acessando as variáveis que são compartilhadas
 ![[Pasted image 20250426163827.png]]



































































































