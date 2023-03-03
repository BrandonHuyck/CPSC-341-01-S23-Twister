from sense_hat import SenseHat
sns = SenseHat()

def twister_command(command, color):
    #color = 'blue'
    #command = 'left_foot'

    if(color == 'red'):
        x = (255,0,0)
    elif(color == 'green'):
        x = (0,255,0)
    elif(color == 'blue'):
        x = (0,0,255)
    elif(color == 'yellow'):
        x = (255,255,0)

    b = (1, 1, 1) #Black

    left_hand = [
        x, x, x, x, x, x, x, x,
        x, b, x, x, x, b, x, b,
        x, b, x, x, x, b, x, b,
        x, b, x, x, x, b, b, b,
        x, b, x, x, x, b, x, b,
        x, b, x, x, x, b, x, b,
        x, b, b, b, x, b, x, b,
        x, x, x, x, x, x, x, x,
    ]

    left_foot = [
        x, x, x, x, x, x, x, x,
        x, b, x, x, x, b, b, b,
        x, b, x, x, x, b, x, x,
        x, b, x, x, x, b, b, x,
        x, b, x, x, x, b, x, x,
        x, b, x, x, x, b, x, x,
        x, b, b, b, x, b, x, x,
        x, x, x, x, x, x, x, x,
    ]

    right_hand = [
        x, x, x, x, x, x, x, x,
        x, b, b, b, x, b, x, b,
        x, b, x, b, x, b, x, b,
        x, b, b, x, x, b, b, b,
        x, b, x, b, x, b, x, b,
        x, b, x, b, x, b, x, b,
        x, b, x, b, x, b, x, b,
        x, x, x, x, x, x, x, x,
    ]

    right_foot = [
        x, x, x, x, x, x, x, x,
        x, b, b, b, x, b, b, b,
        x, b, x, b, x, b, x, x,
        x, b, b, x, x, b, b, x,
        x, b, x, b, x, b, x, x,
        x, b, x, b, x, b, x, x,
        x, b, x, b, x, b, x, x,
        x, x, x, x, x, x, x, x,
    ]

    if(command == 'left_foot'):
        sns.set_pixels(left_foot)
    elif(command == 'right_foot'):
        sns.set_pixels(right_foot)
    elif(command == 'right_hand'):
        sns.set_pixels(right_hand)
    elif(command == 'left_hand'):
        sns.set_pixels(left_hand)