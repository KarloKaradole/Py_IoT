#Napraviti aplikaciju koja prikazuje strelicu na led matrici, ovisno o tome 
# da li se temperatura povecava ili snizava

from sense_emu import SenseHat 
import time 

hat = SenseHat()
hat.clear()

r=[255,0,0] # red
b=[0,0,255] # blue

temp_up = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r        
]
temp_down = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
]

while True:
    temperature = round(hat.get_temperature(), 2)
    time.sleep(1) # pauza izmedu mjerenja
    current_temperature = round(hat.get_temperature(), 2)
    
    temp_diff = current_temperature - temperature


    if temp_diff >= 1:
        hat.set_pixels(pixel_list=temp_up)
    elif temp_diff <= -1:
        hat.set_pixels(pixel_list=temp_down)