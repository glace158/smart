import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
class Motor:
    def __init__(self, EN, INA, INB = None):
        self.ina = INA
        self.inb = INB
        if (self.inb != None):
            GPIO.setup(INB, GPIO.OUT)
        
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        
        
        self.pwm = GPIO.PWM(EN, 100)
        self.pwm.start(0)
        
        print("----------Motor----------")
        print("PWM: ", self.pwm)
        print("INA: ", self.ina)
        print("INB: ", self.inb)
        

    def motor_speed(self, speed):
        self.pwm.ChangeDutyCycle(abs(speed))  
        
        if speed == 0:
            GPIO.output(self.ina, 0)
            
            if(self.inb != None):
                GPIO.output(self.inb, 0)

        elif speed < 0:
            GPIO.output(self.ina, 0)

            if(self.inb != None):
                GPIO.output(self.inb, 1)
                
        elif speed > 0:
            GPIO.output(self.ina, 1)
            
            if(self.inb != None):
                GPIO.output(self.inb, 0)

#obj = Motor(21, 20, 16)
#obj.motor_speed(33)
#time.sleep(2)
#obj.motor_speed(0)
GPIO.cleanup()