from machine import Pin, Timer
led = Pin(21, Pin.OUT)
led2 = Pin(20, Pin.OUT)
timer = Timer()
timer2 = Timer()

def blink(timer):
    led.toggle()
def blink1(timer2):
    led2.toggle()
timer.init(freq=5, mode=Timer.PERIODIC, callback=blink)
timer2.init(freq=2, mode=Timer.PERIODIC, callback=blink1)