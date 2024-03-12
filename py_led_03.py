from sense_emu import SenseHat
import time

hat = SenseHat()

hat.clear()
hat.set_pixel(0, 2, [0, 255, 0])
hat.set_pixel(0, 1, [255, 0, 0])
time.sleep(2)

hat.clear()
r = [255, 0, 0] # red
g = [0, 255, 0] # green
b = [0, 0, 255] # blue
w = [255, 255, 255] # white

time.sleep(1)
flag = [
    g, g, g, g, g, g, g, g,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    g, g, g, g, g, g, g, g,
]

hat.set_pixels(pixel_list=flag)