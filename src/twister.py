import random
from gtts import gTTS
import os
from time import sleep
import TwisterCommands
import pvporcupine
from pvrecorder import PvRecorder

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

def run():
    while True:
        color_count = {'Red': 0, 'Blue': 0, 'Green': 0, 'Yellow': 0}
        body_on = {'Left Hand': '', 'Right Hand': '',
                   'Left Foot': '', 'Right Foot': ''}
        x = True
        y = input('Players: ')
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
                TwisterCommands.twister_command(
                    part.replace(' ', '_'), color.lower())
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
            x = audio_detection()

        if x == 'quit':
            break

        # audio = gTTS(output, slow = False)
        # audio.save("call_out.mp3")
        # os.system("start call_out.mp3")
        # sleep(5)
        # os.system("taskkill /F /IM wmplayer.exe")
        # os.system("del call_out.mp3")


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
