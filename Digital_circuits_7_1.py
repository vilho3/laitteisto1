from machine import Pin
import time

class STATE_MACHINE:
    def __init__(self, delay, button, led):
        self.delay = delay
        self.button = Pin(button, Pin.IN, Pin.PULL_UP)
        self.led = Pin(led, Pin.OUT)
        self.state=self.off
        
    def off(self):
        self.led.off()
        time.sleep(self.delay)
        if self.button()==0:
            self.state=self.onw
        else:
            self.state=self.off
            
    def onw(self):
        self.led.on()
        time.sleep(self.delay)
        if self.button()==1:
            self.state=self.on
        else:
            self.state=self.onw
        
    def on(self):
        self.led.on()
        time.sleep(self.delay)
        if self.button()==0:
            self.state=self.offw
        else:
            self.state=self.on
    
    
    def offw(self):
        self.led.off()
        time.sleep(self.delay)
        if self.button()==1:
            self.state=self.off
        else:
            self.state=self.offw
            
        
asm = STATE_MACHINE(0.05, 7, 20)

while True:
    asm.state()
    