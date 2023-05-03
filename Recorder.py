# Using python version 3.10.7
import json
import azure.cognitiveservices.speech as speech
import sounddevice as sd
import wavio as wv

freq = 44100
duration = 5
API_KEY = "2a66aa050dec476e9ede880f7e09e932"
end_point = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

while True:
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    media_file_path = './recording1.wav'

    # config speech
    speech_config = speech.SpeechConfig(subscription="2a66aa050dec476e9ede880f7e09e932", endpoint=end_point)
    audio_config = speech.audio.AudioConfig(filename=media_file_path)
    speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once_async().get()
    # print(result)
    print(result.text)
    file = open("output.txt","a")
    file.write(result.text+"\n")
    file.close()
