import random
import requests
def get_random_number():
	random_integer = random.randint(1000, 9999)
	return random_integer

def send_OTP():
	try:
		mobile_number = input("Enter your mobile number to send otp: ")
	except Exception:
		print("VALUE ERROR")
		exit()
	url = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=" + mobile_number + "&msg=" + str(get_random_number()) + " is your verification code.&type=1&dnd_check=0%22"
	response = requests.get(url)


def generate_OTP():
	send_OTP()
	if verify_OTP() == True:
		print("OTP matched successfully.")

def get_OTP():
	return input("Enter OTP: ")
	
def verify_OTP():
	random_number = get_random_number()
	print(random_number)
	try:
		verification_code = get_OTP()
		verification_code = int (verification_code)
	except Exception:
		print("VALUE ERROR")
		exit()
	if random_number == verification_code:
		return True
	else:
		print("ENTERED INVALID OTP")
		exit()
