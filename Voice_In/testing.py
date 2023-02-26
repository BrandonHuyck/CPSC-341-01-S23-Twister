import pvporcupine
from pvrecorder import PvRecorder


porcupine = pvporcupine.create(
    access_key='K9TMWltm8F/ePLVUN+m83XmxBPSPWGLSUWbVxG+Bih1ETIm8mRM17A==',
    keyword_paths=['./Next-Spin_en_raspberry-pi_v2_1_0/Next-Spin_en_raspberry-pi_v2_1_0.ppn']
)


def get_next_audio_frame():
    recorder = PvRecorder(device_index=-1, frame_length=2000) # -1 is the default input audio device.
    recorder.start()
    pcm = recorder.read()
    recorder.delete()
    return pcm


flag = True

while flag:
    audio_frame = get_next_audio_frame()
    keyword_index = porcupine.process(audio_frame)
    if keyword_index == 0:
        # detected `next spin`
        pass
    elif keyword_index == 1:
        flag = False
    print("bottom of while loop")

porcupine.delete()
