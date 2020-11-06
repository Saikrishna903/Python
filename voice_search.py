#Calling an api using requests library.
import requests
import json
import speech_recognition as sr

print("1. Search by voice\n2. Search by text")
choice = int(input("Enter your choice: "))
if choice == 1:
	try:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say your pincode to get location")
			audio = r.record(source, duration = 3)
			Pincode = r.recognize_google(audio)
	except Exception:
		print("I DID NOT GET YOUR VOICE TRY AGAIN!")
		exit()
elif choice == 2:
	Pincode = input("Enter your Pincode to find location: ")
else:
	print("INVALID CHOICE")
	exit()
url = "https://api.postalpincode.in/pincode/" + Pincode
response = requests.get(url)
try:
	if response.status_code == 200:
		postal_pincode_info = response.json()
		for post_office_info in postal_pincode_info:
			village_name = post_office_info['PostOffice'][0]['Name']
			district_name = post_office_info['PostOffice'][0]['District']
			state_name = post_office_info['PostOffice'][0]['State']
			break
		print("Postal information of " + Pincode + ": ")
		print("Village: ", village_name)
		print("District: ", district_name)
		print("State: ", state_name)
	else:
		print("RESPONSE NOT FOUND")
except Exception:
	print("TRY AGAIN!")
	exit()