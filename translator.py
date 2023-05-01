# Using python version 3.10.7
import json
import azure.cognitiveservices.speech as speech


API_KEY = "2a66aa050dec476e9ede880f7e09e932"

end_point = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

media_file_path = './recording2.wav'

# config speech

speech_config = speech.SpeechConfig(subscription="2a66aa050dec476e9ede880f7e09e932", endpoint=end_point)
audio_config = speech.audio.AudioConfig(filename=media_file_path)
speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
result = speech_recognizer.recognize_once_async().get()
print(result)
# print(result.cancellation_details.error_details)
# source_language_text = result.text
# translation = result.translations['en']
# print(translation)
translation_config = speech.translation.SpeechTranslationConfig(subscription=API_KEY, endpoint=end_point)
translation_config.speech_recognition_language = 'en-US'
translation_config.add_target_language('zh-Hans')
translator = speech.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
result_translated = translator.recognize_once_async().get()
print(result_translated.translations)

# translation config
'''
translation_config = speech.translation.SpeechTranslationConfig(subscription=API_KEY, endpoint=end_point)
translation_config.speech_recognition_language = 'zh-Hans'
translation_config.add_target_language('en-US')
audio_config = speech.audio.AudioConfig(filename=media_file_path) #if nothing in the parentheses, defalut using microphone
recognizer = speech.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)
result = recognizer.recognize_once_async().get()
print(vars(result))
'''
#
# translation status
# result.reason
#
# source_language_text = result.text
# print(result.text)
# duration = result.duration // pow(60, 4)
# print(duration)
# # result.translations['en']