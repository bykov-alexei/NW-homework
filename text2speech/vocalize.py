import requests
import os
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

from config import key, region

def get_dictors():
    auth_url = "https://francecentral.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    lang_url = "https://francecentral.tts.speech.microsoft.com/cognitiveservices/voices/list"
    headers = { "Ocp-Apim-Subscription-Key": key, "Content-Length": "0", "Content-type": "application/x-www-form-urlencoded" }
    response = requests.post(auth_url, headers=headers)
    token = response.text

    headers= { "Authorization": "Bearer " + token }
    response = requests.get(lang_url, headers=headers)
    json_langs = response.json()
    return json_langs

filename = input('Enter file to vocalize: ')
if not os.path.isfile(filename):
    print("No such file")
    exit(-1)

with open(filename, 'r') as f:
    text = f.read()

filelang = input('Enter lang of file (en, ru etc.): ')
langs = get_dictors()
available_dictors = []
for lang in langs:
    if lang['Locale'][:2] == filelang:
        available_dictors.append(lang)

if len(available_dictors) == 0:
    print('No dictors found')
    exit(0)

for i, dictor in enumerate(available_dictors):
    print("%i. Name: %s. Gender: %s" % (i + 1, dictor['DisplayName'], dictor['Gender']))

dictor = input("Choose dictor. Enter his number: ")
try:
    dictor = int(dictor) - 1
except ValueError:
    print("Wrong number")
    exit(-1)
if not (0 <= dictor < len(available_dictors)):
    print("Wrong number")
    exit(-1)

output = input('Enter output file name (default: file.wav): ') 
output = output if output else 'file.wav'

dictor = available_dictors[dictor]

speech_config = SpeechConfig(subscription=key, region=region)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)

ssml_string = """<speak version='1.0' xml:lang='{LANG}'><voice xml:lang='{LANG}' xml:gender='{GENDER}'
    name='{NAME}'>
        {TEXT}
</voice></speak>""".format(LANG=dictor['Locale'], GENDER=dictor['Gender'], NAME=dictor['ShortName'], TEXT=text)
result = synthesizer.speak_ssml_async(ssml_string).get()

stream = AudioDataStream(result)
stream.save_to_wav_file(output)
print('Done')