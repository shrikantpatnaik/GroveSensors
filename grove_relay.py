import time
import Adafruit_BBIO.GPIO as GPIO

RELAY_PIN = "P9_22"

class Relay():
    def __init__(self, pin):
        self.__pin = pin
        self.__isOn = False
        GPIO.setup(self.__pin, GPIO.OUT)
        self.turnOff()
         
    def turnOn(self):
        self.__isOn = True
        GPIO.output(self.__pin, GPIO.HIGH)
        
    def turnOff(self):
        self.__isOn = False
        GPIO.output(self.__pin, GPIO.LOW)
    
    def isOn(self):
        return self.__isOn
        
    
if __name__ == "__main__":
    relay = Relay(RELAY_PIN)
    
    while True:
        if relay.isOn():
            relay.turnOff()
        else:
            relay.turnOn()
        time.sleep(2)
        
    