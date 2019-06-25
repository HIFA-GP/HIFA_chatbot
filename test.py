import speech_recognition as sr
import pyttsx3
import time

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
	#while True:

		r = sr.Recognizer()

		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			#audio = r.listen(source, timeout= None)
			#audio = r.listen_in_background(source, callback, phrase_time_limit=None)
			WIT_API_KEY = "GMC25PJVMSZX4PU3LUKVTZP22DV7WBX6"
			#IBM_API_KEY = "3DHgpA3qYTJ66304DrOH5Ljs5FsVrLVGpYKOiUCMctAc"
			#try:
			#	google = r.recognize_google(audio).lower()
			#	wit_ai = r.recognize_wit(audio, key=WIT_API_KEY).lower()
				#order = r.recognize_ibm(audio, key=IBM_API_KEY).lower()


			#	print("Google: ", google)
			#	print("Wit.ai: ", wit_ai)
			#except sr.UnknownValueError:
			#	print("Listening to the magic words: 'Wake up ' or 'Shut down'")

			#except sr.RequestError:
				#eng.say("I'm sorry, I couldn't reach google")
				#eng.runAndWait()
			#	print("I'm sorry, I couldn't reach google")
		stop_listening = r.listen_in_background(source, callback)
		# do some unrelated computations for 5 seconds
		for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

		# calling this function requests that the background listener stop listening
		stop_listening(wait_for_stop=False)
		while True:
		# do some unrelated computations for 5 seconds
			for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

		
