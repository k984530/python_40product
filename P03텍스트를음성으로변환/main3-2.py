from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = "테스트용 음성입니다"

tts = gTTS(text = text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")