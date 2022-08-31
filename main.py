import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os



class chatboy():

	def __init__(self, name):
		print("[jvis] starting...",name)
		self.name = name


	def stt(self):
		recog = sr.Recognizer()
		recog.pause_threshold=0.7
		with sr.Microphone() as mic:
			print("[jvis] : listening...")
			recog.adjust_for_ambient_noise(mic)
			audio = recog.listen(mic)
		try:
			self.text = recog.recognize_google(audio)
			print("[you] :",self.text)
		except:
			print("I didn't hear anything :(")
	@staticmethod
	def tts(text):
		print("[jvis] : ",text)
		speaker = gTTS(text=text, lang="en", slow=False)
		speaker.save("temp.mp3")
		os.system("afplay temp.mp3")
		os.system("rm temp.mp3")

	#def wake(self,text):
		#return True if self.name in text.lower() else False




if __name__ == "__main__":
	ai = chatboy(name="Dev")

	while True:
		ai.stt()
		res=ai.text
		print("[jarvis] :",res)
		#if ai.wake(ai.text) is True:
			#res = "Hey"
		ai.tts(res)




