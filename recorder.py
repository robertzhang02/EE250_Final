import azure.cognitiveservices.speech as speech
import sounddevice as sd
import wavio as wv

# Sampling frequency
freq = 44100
# Set the Duration of each speech
duration = 5
#API Setting
API_KEY = "2a66aa050dec476e9ede880f7e09e932"
end_point = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

user_input = ""
while user_input != "q":
    user_input = input("Recording right now, press q to quit or press other key to continue:")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)   # record the aduio
    sd.wait()
    wv.write("recording1.wav", recording, freq, sampwidth=2)    # save the aduio file as wav
    media_file_path = './recording1.wav'

    # config speech
    speech_config = speech.SpeechConfig(subscription="2a66aa050dec476e9ede880f7e09e932", endpoint=end_point)    # set up the speech config
    audio_config = speech.audio.AudioConfig(filename=media_file_path)   # set up the audio config
    speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config) # reconize the speech
    result = speech_recognizer.recognize_once_async().get()
    # print(result)
    print(result.text)
    file = open("speech.txt", "a")
    file.write(result.text+"\n")
    file.close()
