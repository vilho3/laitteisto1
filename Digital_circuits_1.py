from machine import Pin, ADC
import time


pot = ADC(Pin(27))
conversion_factor=3.3/65535

while True:
    pot_voltage = pot.read_u16()*conversion_factor
    
    
    led = Pin("LED",Pin.OUT)
    led.on()
    time.sleep(pot_voltage)
    led.off()
    print(pot_voltage)
    time.sleep(pot_voltage)
  
