from sense_emu import SenseHat

hat = SenseHat()
hat.clear()


x = 0
y = 0
hat.set_pixel(x, y, 0, 255, 0)

def move_dot(direction):
    global x, y
    if direction == 'up':
        y = (y - 1) % 8
    elif direction == 'down':
        y = (y + 1) % 8
    elif direction == 'left':
        x = (x - 1) % 8
    elif direction == 'right':
        x = (x + 1) % 8
    hat.clear()
    hat.set_pixel(x, y, 0, 255, 0)

while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == "released":
            move_dot(event.direction)

    #Obje verzije rade, ali ova koja se koristi trenutno je puno zgodnija!
    """for event in joystick_events:
        if event.action == 'released' and event.direction == 'up':
            # print('Pokreni funkciju koja pomice OBJEKT prema gore')
            move_dot("up")
        elif event.action == 'released' and event.direction == 'down':
            # print('Pokreni funkciju koja pomice OBJEKT prema dolje')
            move_dot("down")
        elif event.action == 'released' and event.direction == 'left':
            # print('Pokreni funkciju koja pomice OBJEKT prema lijevo')
            move_dot("left")
        elif event.action == 'released' and event.direction == 'right':
            # print('Pokreni funkciju koja pomice OBJEKT prema desno')
            move_dot("right")
        elif event.action == 'released' and event.direction == 'middle':
            # print('Pokreni funkciju koja reagira na tipku ENTER')
            move_dot()"""