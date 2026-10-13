from machine import Pin
import time

class State_machine:
    def __init__(self, delay, button, alarm, red, siren):
        self.delay = delay
        self.button = Pin(button, Pin.IN, Pin.PULL_UP)
        self.alarm = Pin(alarm, Pin.IN, Pin.PULL_UP)
        self.red = Pin(red, Pin.OUT)
        self.siren = Pin(siren, Pin.OUT)
        self.state=self.s1
        
    def s1(self):
        self.red.off()
        self.siren.off()
        time.sleep(self.delay)
        if self.alarm()==0:
            self.state=self.s2
        else:
            self.state=self.s1
            
    def s2(self):
        self.red.on()
        self.siren.on()
        time.sleep(self.delay)
        if self.alarm()==1:
            self.state=self.s3
        else:
            if self.button()==0:
                self.state=self.s4
            else:
                self.state=self.s2
                
    def s3(self):
        self.red.on()
        self.siren.off()
        time.sleep(self.delay)
        if self.button()==0:
            self.state=self.s1
        else:
            self.state=self.s3
            
    def s4(self):
        self.red.off()
        self.siren.off()
        time.sleep(self.delay)
        self.state=self.s5
        
    def s5(self):
        self.red.on()
        self.siren.off()
        time.sleep(self.delay)
        if self.alarm()==0:
            self.state=self.s4
        else:
            self.state=self.s1
            
            
asm = State_machine(0.5, 7, 9, 22, 20)

while True:
    asm.state()
            
        