# Using python version 3.10.7
import azure.cognitiveservices.speech as speech # version 1.28.0


API_KEY = "2a66aa050dec476e9ede880f7e09e932"

end_point = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

media_file_path = './recording1.wav'

# config speech

speech_config = speech.SpeechConfig(subscription="2a66aa050dec476e9ede880f7e09e932", endpoint=end_point)
audio_config = speech.audio.AudioConfig(filename=media_file_path)
speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
result = speech_recognizer.recognize_once_async().get()
print(result)

translation_config = speech.translation.SpeechTranslationConfig(subscription=API_KEY, endpoint=end_point)
translation_config.speech_recognition_language = 'en-US'
translation_config.add_target_language('zh-Hans')
translator = speech.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
result_translated = translator.recognize_once_async().get()
print(result_translated.translations['zh-Hans'])

# translation config
'''
translation_config = speech.translation.SpeechTranslationConfig(subscription=API_KEY, endpoint=end_point)
translation_config.speech_recognition_language = 'en-US'
translation_config.add_target_language('zh-Hans')
audio_config = speech.audio.AudioConfig(filename=media_file_path) #if nothing in the parentheses, defalut using microphone
recognizer = speech.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
result = recognizer.recognize_once()
print(result)
'''