import RPi.GPIO as gpio
import pigpio
from time import sleep

frequency = 200
#pi = pigpio.pi()
#pi.set_mode(18, pigpio.OUTPUT)

#print("MODE: ",pi.get_mode(18))

#pi.set_PWM_frequency(18, frequency)
#print("Frequency: ", pi.get_PWM_frequency(18))
#pi.set_PWM_dutycycle(18, 64)
gpio.setmode(gpio.BCM)

#gpio.setup(4, gpio.OUT)
gpio.setup(18, gpio.OUT)



p = gpio.PWM(18, frequency)
p.start(20)

while(1):
    for x in range(500,2500):
        #print(x)
        #p.ChangeDutyCycle(x)
        #pi.set_servo_pulsewidth(18, x)
        sleep(0.01)
