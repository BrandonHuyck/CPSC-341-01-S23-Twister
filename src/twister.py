import random
from gtts import gTTS
import os
from time import sleep


def run():
    while True:
        color_count = {'Red': 0, 'Blue': 0, 'Green': 0, 'Yellow': 0}
        body_on = {'Left Hand': '', 'Right Hand': '',
                   'Left Foot': '', 'Right Foot': ''}
        x = ''
        y = input('Players: ')
        if y == '2':
            y = 3
        elif y == 'quit':
            break
        else:
            y = 2

        while x != 'quit':
            if x == '':
                part = random.choice(list(body_on.keys()))
                color = random.choice(list(color_count.keys()))
                if body_on[part] == color:
                    continue
                if color_count[color] == y:
                    continue
                output = part + ' ' + color
                print(output)
                if body_on[part] in color_count.keys():
                    color_count[body_on[part]] -= 1
                body_on[part] = color
                color_count[body_on[part]] += 1
            elif x == '2':
                y = 3
                x = ''
                continue
            elif x == 'on':
                print(body_on)
            elif x == 'restart':
                break
            # print(color_count, body_on, x, y) #debugging line
            x = input()

        if x == 'quit':
            break

        # audio = gTTS(output, slow = False)
        # audio.save("call_out.mp3")
        # os.system("start call_out.mp3")
        # sleep(5)
        # os.system("taskkill /F /IM wmplayer.exe")
        #os.system("del call_out.mp3")


if __name__ == '__main__':
    run()

# working on adding functionality for both voice inputs and outputs
'''
    audio = gTTS(output, slow = False)
    audio.save("call_out.mp3")
    os.system("start call_out.mp3")
    sleep(2)
    os.system("del call_out.mp3")
'''
'''
color_count = {'Red': 0,'Blue': 0,'Green': 0,'Yellow': 0}
body_on = {'Left Hand': '','Right Hand': '','Left Foot': '','Right Foot': ''}
if input('Players: ') == '2':
    y = 3
else:
    y = 2

while True:
    part = random.choice(list(body_on.keys()))
    color = random.choice(list(color_count.keys()))
    if body_on[part] == color:
        continue
    if color_count[color] == y:
       continue
    output = part + ' ' + color
    print(output)
    audio = gTTS(output, slow = False)
    audio.save("call_out.mp3")
    os.system("start call_out.mp3")
    sleep(5)
    os.system("taskkill /F /IM wmplayer.exe")
    #os.system("del call_out.mp3")
    #sleep(8)
    #input()
    if body_on[part] in color_count.keys():
        color_count[body_on[part]] -= 1
    body_on[part] = color
    color_count[body_on[part]] += 1
    '''
