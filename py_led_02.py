from sense_emu import SenseHat
import time

hat = SenseHat()


text_red = [255, 0, 0]
background = [0, 0, 0]

message = 'Pozdrav'

while True:
    for letter in message:
        hat.show_letter(letter,
                        text_colour=text_red,
                        back_colour=background)
        time.sleep(0.5)