# 1. korak - import SenseHAT emulator modula
from sense_emu import SenseHat

# 2. korak - kreiranje SenseHAT emulator objekta
sense_hat = SenseHat()

# Boja se definira kao RGB (Red, Green, Blue) od 0 do 255
#             R   G   B
text_color = [76, 139, 245]
# background = [255, 255, 255] # bijela
background = [0, 0, 0] # crna

while True:
    sense_hat.show_message('Hello, World!', 
                            scroll_speed=.2,
                            text_colour=text_color,
                            back_colour=background)