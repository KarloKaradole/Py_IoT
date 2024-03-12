#Napraviti aplikaciju koja ovisno o postotku vlaznosti zraka,
#LED matricu puni pixel po pixel, bojom po izboru.
#Kada je vlaznost zraka 0% matrica je prazna(crna),
#a kada je 100% onda je puna(boja po izboru).abs

from sense_emu import SenseHat
import time

def get_led_matrix_picture(color_up, color_down, air_humidity):
    led_matrix = []

    for i in range(64):
        if i < round(64/100, 2) * air_humidity:
            led_matrix.append(color_down)
        else:
            led_matrix.append(color_up)

    return led_matrix
    
hat = SenseHat()
hat.clear()

black = [255, 0, 0]
white = [255, 255, 255]

while True:
    air_humidity = round(hat.get_humidity(),2)
    led_matrix = get_led_matrix_picture(white, black, air_humidity)

    hat.set_pixels(led_matrix)
    time.sleep(1)


