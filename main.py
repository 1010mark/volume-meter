import pyaudio
import numpy as np
import winsound
import datetime



audio = pyaudio.PyAudio()
stream = audio.open( format = pyaudio.paInt16,
                     rate = 44100,
                     channels = 1, 
                     input_device_index = 1,
                    input = True, 
                    frames_per_buffer = 1024)
while True:
    dt = datetime.datetime.now()
    if(dt.hour >= 20) or (dt.hour <= 7):
        pre_threshold = 0.06
        threshold = 0.09
    else:
        pre_threshold = 0.12
        threshold = 0.15
    data = stream.read(1024)
    x = np.frombuffer(data, dtype="int16") / 32768.0
    #print(x.max())
    if(x.max()>pre_threshold):
        print(x.max())
    if(x.max()>threshold): 
        winsound.Beep(1000, 100)
