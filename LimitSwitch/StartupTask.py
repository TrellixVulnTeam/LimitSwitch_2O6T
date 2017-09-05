# Add your code here to run in your startup task
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(24,IN)   # Limit Switch
gpio.setup(7,OUT)   # MotorA1
gpio.setup(8,OUT)   # MotorA2


while True:
    if not(gpio.input(24)):
        gpio.output(7,True)
        gpio.output(8,False)
        time.sleep(2)
    elif gpio.input(24):
        gpio.output(7,False)
        gpio.output(8,True)
        time.sleep(2)
    else:
        gpio.output(7,False)
        gpio.output(8,False)