from sense_emu import SenseHat
import time


hat = SenseHat()
hat.clear()

temperature = hat.get_temperature()
temperature_from_humidity = hat.get_temperature_from_humidity()
temperature_from_pressure = hat.get_temperature_from_pressure()

print(f'Temperature je: {round(temperature, 1)} \u2103')
print(f'Temperature iz vlaznosti je: {round(temperature_from_humidity, 1)} \u2103')
print(f'Temperature iz tlaka je: {round(temperature_from_pressure, 1)} \u2103')


while True:
    temperature = hat.get_temperature()
    print(f'Temperature je: {round(temperature, 5)} \u2103')