
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

##### <span style="color:rgb(0, 255, 64)">Software Embarcado - Interrupções</span>

