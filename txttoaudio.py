import os
import gtts

tts = gtts.gTTS(text='''Type any text''', lang='en')

tts.save('holllik.wav')
os.startfile('holllik.wav')