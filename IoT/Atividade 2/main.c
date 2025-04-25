#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"


#define BUTTON GPIO_NUM_34
#define LED1 GPIO_NUM_21
#define LED2 GPIO_NUM_19
#define LED3 GPIO_NUM_18
#define LED4 GPIO_NUM_17

void app_main() {


// Configuração de LED como saída e BOTÃO como entrada
gpio_config_t io_conf_led = {
  .pin_bit_mask = (1ULL << LED1) | (1ULL << LED2) | (1ULL << LED3) | (1ULL << LED4),
  .mode = GPIO_MODE_OUTPUT,
  .pull_up_en = 0,
  .pull_down_en= 0,
  .intr_type = GPIO_INTR_DISABLE
};
gpio_config(&io_conf_led);

gpio_config_t io_conf_button = {
  .pin_bit_mask = (1ULL << BUTTON),
  .mode = GPIO_MODE_INPUT,
  .pull_up_en = 0,
  .pull_down_en = 0,
  .intr_type = GPIO_INTR_DISABLE
};
gpio_config(&io_conf_button);

// Setando valor da contagem
uint8_t cont = 0;
  
  while (true) {

    uint8_t state_buttom = gpio_get_level(BUTTON);

    if (state_buttom == 0){

      gpio_set_level(LED1, 0);
      gpio_set_level(LED2, 0);
      gpio_set_level(LED3, 0);
      gpio_set_level(LED4, 0);

      cont++;
      if (cont > 15){
        cont = 0;
      }

    } else{
        gpio_set_level(LED1, (cont >> 0) & 1);
        gpio_set_level(LED2, (cont >> 1) & 1);
        gpio_set_level(LED3, (cont >> 2) & 1);
        gpio_set_level(LED4, (cont >> 3) & 1);
      }
    
    }

  }

