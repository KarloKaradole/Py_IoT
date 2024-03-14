from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()

while True:
    pressure = round(hat.get_pressure(), 2)
    print(f"Tlak zraka je: {pressure} hPa.")

    time.sleep(1)

