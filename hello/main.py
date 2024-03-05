import utime
from machine import Pin, I2C
import ssd1306

red = Pin(16, Pin.OUT)


# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(4), sda=Pin(5))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, Wokwi!', 10, 10)      
oled.show()


while True:
  red.value(0)
  utime.sleep(1)
  red.value(1)
  utime.sleep(1)
  