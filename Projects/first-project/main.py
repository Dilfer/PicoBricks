from machine import I2C, Pin, PWM
from picobricks import SSD1306_I2C
import time
import utime

OLD_PIXEL_WIDTH = 128  # oled display width
OLD_PIXEL_HEIGHT = 64  # oled display height

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = SSD1306_I2C(OLD_PIXEL_WIDTH, OLD_PIXEL_HEIGHT, i2c, addr=0x3c)

oled.fill(0)
oled.text("Initial main.py loading.", 0, 0)
oled.show()
time.sleep(3)

button = Pin(10, Pin.IN)
#buzzer=Pin(20, Pin.OUT)
buzzer = PWM(Pin(20, Pin.OUT))#initialize digital pin 20 as an OUTPUT for buzzer
buzzer.freq(1000)


def buttonInterruptHandler(event):  # Interrupt event, that will work when button is pressed
    if button.value() == 1:
        for i in range(1, 4):
            oled.fill(0)
            oled.text(str(i), 0, 0)
            oled.show()
            time.sleep(1)

        buzzer.duty_u16(6000)
        utime.sleep(1)
        # wait for one second
        buzzer.duty_u16(0)

        oled.fill(0)
        oled.text("...             ", 0, 0)
        oled.text("Nothing happened?", 0, 10)

        oled.show()
        time.sleep(3)


button.irq(trigger=Pin.IRQ_RISING, handler=buttonInterruptHandler)

while True:
    oled.fill(0)
    oled.text("Press the button", 0, 0)
    oled.text("if you DARE!", 0, 10)
    oled.show()
    time.sleep(3)
