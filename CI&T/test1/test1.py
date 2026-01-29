def calcula_total_leds(altura,largura):
    if altura <= 0 or largura <= 0:
      return 0
      
    # calculated actual quantity
    led_height = altura + 1
    led_width = largura + 1
    
    return led_height * led_width