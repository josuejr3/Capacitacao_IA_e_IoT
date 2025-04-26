
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

###### <span style="color:rgb(0, 255, 64)">Conceitos Iniciais</span>

O que é uma interrupção?




































