########################################################
'''
A Python program to stop the leak of flammable gases using esp8266


Authors - Rajith Ashok
          Kraleti V S Siddhartha Bharadwaj
'''
########################################################


from machine import Pin
import time 


# initializing the pin configuration for each component
led = Pin(16, Pin.OUT)         #connect positive to pin 16
buzzer = Pin(5, Pin.OUT)       #connect 'signal' to pin 5, Vcc to 3.3v and Gnd to Gnd
gasSensor = Pin(4, Pin.IN)     #connect 'DO' - Digital output to pin 4, Vcc to 3.3v and Gnd to Gnd
motor = Pin(12, Pin.OUT)       #connect positive to pin 12


while True:
    if gasSensor.value()==0:
        # Runs if the sensor detects a flammable gas in its surroundings
        # Motor is run to shut the gas source
        motor. on()
        for i in range(10):
            # Warning system involving LEDs and buzzers
            led.on()
            buzzer.off()
            time.sleep(0.5)
            
            led.off()
            buzzer.on()
            time.sleep(0.5)
            
    else:
        # Components are turned off when there is no gas leak
        led.off()
        buzzer.off()
        motor.off()
