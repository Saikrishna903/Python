#Oxford Dictionary 
import requests
from playsound import playsound

app_id = "bab7f31f"
app_key = "aee173cf53475e437c44ddc98e1bb41b"
dictionary_word = input("Enter a word to get definition and pronunciation: ")
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/" + dictionary_word.lower()
response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
if response.status_code == 200:
	dictionary_info = response.json()
	audio_url = dictionary_info['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
	definition_of_word = dictionary_info['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
	print("Definition: ")
	print(definition_of_word)
	playsound(audio_url)
else: 
	print("RESPONSE NOT FOUND")