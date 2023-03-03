import random
from gtts import gTTS
from time import sleep
from pygame import mixer
import pvporcupine
from pvrecorder import PvRecorder
from sense_hat import SenseHat

sns = SenseHat()

def audio_detection():
    # -1 is the default input audio device.
    porcupine = pvporcupine.create(
        access_key='K9TMWltm8F/ePLVUN+m83XmxBPSPWGLSUWbVxG+Bih1ETIm8mRM17A==',
        keyword_paths=[
            './Next-Spin_en_raspberry-pi_v2_1_0/Next-Spin_en_raspberry-pi_v2_1_0.ppn']
    )
    recorder = PvRecorder(device_index=-1, frame_length=512)
    try:
        recorder.start()
        while True:
            pcm = recorder.read()
            keyword_index = porcupine.process(pcm)
            if keyword_index == 0:
                return True
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        recorder.delete()
        porcupine.delete()
    return False

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

def get_players():
    sns.show_message("Enter Number Players")
    players = 2
    sns.show_letter("2")
    while True:
        for event in sns.stick.get_events():
            if event.direction == "left":
                players = 2
                sns.show_letter(str(players))
            elif event.direction == "up":
                players = 3
                sns.show_letter(str(players))
            elif event.direction == "right" :
                players = 4
                sns.show_letter(str(players))
            elif event.direction == "middle":
                return players
            
def AudioOutput(output):
    #gTTS Creation of Output
    tts = gTTS(output)
    tts.save('hello.mp3')
    #pygame Audio Output (using mixer)
    mixer.init()
    mixer.music.load("hello.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        sleep(1)
    mixer.quit()

def run(source):
    
    while True:
        color_count = {'Red': 0, 'Blue': 0, 'Green': 0, 'Yellow': 0}
        body_on = {'Left Hand': '', 'Right Hand': '',
                   'Left Foot': '', 'Right Foot': ''}
        x = True
        y = input('Players: ') if source == 0 else get_players()
        if y == '2':
            y = 3
        elif y == 'quit':
            break
        else:
            y = 2

        while x:
            if x == True:
                part = random.choice(list(body_on.keys()))
                color = random.choice(list(color_count.keys()))
                if body_on[part] == color:
                    continue
                if color_count[color] == y:
                    continue
                output = part + ' ' + color
                twister_command(part.replace(' ', '_').lower(), color.lower())
                print(output)
                #gTTS Creation/Audio Output
                AudioOutput(output)
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
            x = audio_detection() if source == 0 else input() == ""

        if x == 'quit':
            break

        # audio = gTTS(output, slow = False)
        # audio.save("call_out.mp3")
        # os.system("start call_out.mp3")
        # sleep(5)
        # os.system("taskkill /F /IM wmplayer.exe")
        # os.system("del call_out.mp3")


if __name__ == '__main__':
    run(-1)

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
