import random
from sense_emu import SenseHat


hat = SenseHat()
hat.clear()


b = [0, 0, 0] # black
g = [0, 255, 0] # green
r = [255, 0, 0] # red
game_board = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]
location = 0

def display_board():
    global game_board
    hat.clear()
    hat.set_pixels(game_board)


def set_fruits_start_loc():
    global game_board
    global location
    rnd_index = list(range(64))
    random.shuffle(rnd_index)

    fruit_locations = rnd_index[ : : 22]

    for fruit_location in fruit_locations:
        game_board[fruit_location] = r

    location = random.randint(0, 63)
    if location not in fruit_locations:
        game_board[location] = g


def move_dot(event_direction: str):
    global game_board
    global location

    if event_direction == 'up':
        game_board[location] = b
        game_board[location - 8] = g
        display_board()
    elif event_direction == 'down':
        game_board[location] = b
        game_board[location + 8] = g
        display_board()
    elif event_direction == 'left':
        game_board[location] = b
        game_board[location - 1] = g
        display_board()
    elif event_direction == 'right':
        game_board[location] = b
        game_board[location + 1] = g
        display_board()
    elif event_direction == 'middle':
        pass


set_fruits_start_loc()
display_board()

while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == 'released':
            move_dot(str(event.direction))