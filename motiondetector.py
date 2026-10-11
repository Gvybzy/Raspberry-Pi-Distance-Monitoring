from machine import Pin, I2C
import utime
from pico_i2c_lcd import I2cLcd

# ---------------- PINS ----------------
red_led1 = Pin(15, Pin.OUT)
red_led2 = Pin(17, Pin.OUT)
yellow_led1 = Pin(14, Pin.OUT)
yellow_led2 = Pin(16, Pin.OUT)
green_led1 = Pin(12, Pin.OUT)
green_led2 = Pin(13, Pin.OUT)
buzzer = Pin(18, Pin.OUT)

# HC-SR04
trig = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)

# ---------------- LCD ----------------
i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.backlight_on()
lcd.clear()
lcd.putstr("System Ready")
utime.sleep(1)

# ---------------- FUNCTION ----------------
def get_distance():
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(10)
    trig.low()

    while echo.value() == 0:
        pass
    start = utime.ticks_us()

    while echo.value() == 1:
        pass
    end = utime.ticks_us()

    # distance in cm
    distance = (utime.ticks_diff(end, start) * 0.0343) / 2
    return round(distance, 1)  # Round to 1 decimal to reduce sensor fluctuation

# ---------------- MAIN LOOP ----------------
while True:
    d = get_distance()

    # ---------------- RESET ALL ----------------
    red_led1.off(); red_led2.off()
    yellow_led1.off(); yellow_led2.off()
    green_led1.off(); green_led2.off()
    buzzer.off()

    # ---------------- CONDITIONS ----------------
    if d <= 24.0:
        # RED + BUZZER
        
        yellow_led1.on()
        yellow_led2.on()
        lcd.clear()
        lcd.putstr("Dist: {:.1f}cm".format(d))
        lcd.move_to(0, 1)
        lcd.putstr("DANGER")
        buzzer.on()
        utime.sleep(0.2)
        buzzer.off()
        utime.sleep(0.2)

    elif 25.0 <= d <= 40.0:
        # YELLOW, NO BUZZER
        red_led1.on()
        red_led2.on()
        lcd.clear()
        lcd.putstr("Dist: {:.1f}cm".format(d))
        lcd.move_to(0, 1)
        lcd.putstr("WARNING")
        utime.sleep(0.2)

    elif d > 40.0:
        # GREEN, NO BUZZER
        green_led1.on()
        green_led2.on()
        lcd.clear()
        lcd.putstr("Dist: {:.1f}cm".format(d))
        lcd.move_to(0, 1)
        lcd.putstr("SAFE")
        utime.sleep(0.2)
