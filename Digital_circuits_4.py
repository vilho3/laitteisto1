from machine import Pin
import time

button = Pin(12, mode =Pin.IN, pull=Pin.PULL_UP)
led1=Pin(20, Pin.OUT)
led2=Pin(21, Pin.OUT)
led3=Pin(22, Pin.OUT)
pressed=0

def leds(button_value):
    if button_value & 1:
        led1.on()
    else:
        led1.off()
    
    if button_value & 2:
        led2.on()
    else:
        led2.off()
            
    if button_value & 4:
        led3.on()
    else:
        led3.off()
     
while True:
    if button.value()==0:
        time.sleep(0.150)
        pressed+=1
        print(pressed)
        if pressed>7:
            pressed=0
        leds(pressed)
        
   