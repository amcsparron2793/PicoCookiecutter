"""
Joystick.py

controls a basic Analog joystick

based on https://diyprojectslab.com/joystick-with-raspberry-pi-pico/
"""


from machine import Pin, ADC


class Joystick:
    def __init__(self, xAxisPin: int = 28, yAxisPin: int = 27, ButtonPin: int = 18):
        self.xAxis = ADC(Pin(xAxisPin))
        self.yAxis = ADC(Pin(yAxisPin))
        self.Button = Pin(ButtonPin, Pin.IN, Pin.PULL_UP)

    def get_position(self):
        xValue = self.xAxis.read_u16()
        yValue = self.yAxis.read_u16()
        return xValue, yValue

    def get_button(self):
        return self.Button.value()

    def read_all_values(self):
        buttonStatus = "not pressed"
        if self.get_button() == 0:
            buttonStatus = "pressed"

        xVal, yVal = self.get_position()
        print("X: " + str(xVal) + ", Y: " + str(yVal) + " button status: " + buttonStatus)


"""while True:
    buttonValue = button.value()
    buttonStatus = "not pressed"

    if buttonValue == 0:
        buttonStatus = "pressed"

    print("X: " + str(xValue) + ", Y: " + str(yValue) + " -- button value: " + str(
        buttonValue) + " button status: " + buttonStatus)
    utime.sleep(0.2)"""