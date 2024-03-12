from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()

while True:
    air_humidity = round(hat.get_humidity(),2)
    print(f"Vlaznost zraka je: {air_humidity} %")
    time.sleep(0.1)