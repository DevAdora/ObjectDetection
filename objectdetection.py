from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=5, threshold_distance=1)

    
def in_range_5():
    print("Object in 5 meters")
    #Sound and LED input

def in_range_1():
    print("Object in 1 meter")
    #Sound and LED input

def check_distance():
    distance = ultrasonic.distance * 5
    if distance <=1:
        in_range_1()
        elif distance <=5:
            in_range_5()

while True():
    check_distance()
    sleep(0.1)