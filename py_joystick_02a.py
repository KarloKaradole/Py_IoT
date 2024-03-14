from sense_emu import SenseHat
import random

hat = SenseHat()
hat.clear()

b = [0, 0, 0]
g = [0, 255, 0]
r = [255, 0, 0]

game_board = [b]*64 

location = 0

def display_board():
    hat.set_pixels(game_board)

def set_fruits_start_loc():
    global game_board, location
    rnd_index = list(range(64))
    random.shuffle(rnd_index)

    fruit_locations = rnd_index[:3] 

    for fruit_location in fruit_locations:
        game_board[fruit_location] = r

    while True:
        location = random.randint(0, 63)
        if location not in fruit_locations:
            game_board[location] = g
            break

def move_dot(event_direction):
    global game_board, location

    if event_direction == "up" and location >= 8:
        new_location = location - 8
    elif event_direction == "down" and location < 56:
        new_location = location + 8
    elif event_direction == "right" and (location + 1) % 8 != 0:
        new_location = location + 1
    elif event_direction == "left" and location % 8 != 0:
        new_location = location - 1
    else:
        return 

    if game_board[new_location] != r:
        game_board[location] = b  
        location = new_location
        game_board[location] = g  
        display_board()

set_fruits_start_loc()
display_board()

while True:
    joystick_events = hat.stick.get_events()
    for event in joystick_events:
        if event.action == "released":
            move_dot(event.direction)
