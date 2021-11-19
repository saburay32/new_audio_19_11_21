import pyaudio
import wave
'''
    Lessons tube:
    https://youtu.be/UQFkU9Abzt8
    https://www.youtube.com/watch?v=ergRggVCNK8
    
    Doc:
    http://people.csail.mit.edu/hubert/pyaudio/docs/#pyaudio.PyAudio.open
    http://people.csail.mit.edu/hubert/pyaudio/
'''


    #  p = pyaudio.PyAudio()#detected audio device
    #  for i in range(p.get_device_count()):
    #      print(i,p.get_device_info_by_index(i)['name'])
    # Результат на рабочем компе:
    #
    # 0 Microsoft Sound Mapper - Input

    # 1 Microphone (Magic Sound)<<<<--------с этого пишет,беру для дальнейшей индекс 1(stream--->input_device_index = 1)

    # 2 Микрофон (Realtek High Definiti
    # 3 Microsoft Sound Mapper - Output
    # 4 Динамики (Realtek High Definiti
    # 5 Первичный драйвер записи звука
    # 6 Microphone (Magic Sound)
    # 7 Микрофон (Realtek High Definition Audio)
    # 8 Первичный звуковой драйвер
    # 9 Динамики (Realtek High Definition Audio)
    # 10 Динамики (Realtek High Definition Audio)
    # 11 Microphone (Magic Sound)
    # 12 Микрофон (Realtek High Definition Audio)
    # 13 Микрофон (Realtek HD Audio Mic input)
    # 14 Лин. вход (Realtek HD Audio Line input)
    # 15 Стерео микшер (Realtek HD Audio Stereo input)
    # 16 Speakers (Realtek HD Audio output)
    # 17 Микрофон (Magic Sound)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 1,#index mic after cycle for
                frames_per_buffer=CHUNK)

print("* запись")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* запись окончена ")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()