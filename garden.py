from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
fan_1 = 12
fan_2 = 16
# Soil sensor requires GPIO, ground, and 3.3v pins
soil_sensor = 5 # ground=9, 3.3v=1
water_pump = 24

GPIO.setup(fan_1, GPIO.OUT)
GPIO.setup(fan_2, GPIO.OUT)
GPIO.setup(soil_sensor, GPIO.IN)
GPIO.setup(water_pump, GPOI.OUT)

def pump_water():
    GPIO.output(water_pump, True)
    sleep(5)
    GPIO.output(water_pump, False)

def check_soil():
    is_moist = GPIO.input(soil_sensor)
    if not is_moist:
        pump_water()
