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
    # print(result.cancellation_details.error_details)
    # source_language_text = result.text
    # translation = result.translations['en']
    # print(translation)
    translation_config = speech.translation.SpeechTranslationConfig(subscription=API_KEY, endpoint=end_point)
    translation_config.speech_recognition_language = 'en-US'
    translation_config.add_target_language('en')
    translator = speech.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
    result_translated = translator.recognize_once()
    print(result_translated.translations['en'])
    file = open("output.txt","a")
    file.write(result_translated.translations['en']+"\n")
    file.close()

# translation config
#
# translation status
# result.reason
#
# source_language_text = result.text
# print(result.text)
# duration = result.duration // pow(60, 4)
# print(duration)
# # result.translations['en']