#Program to send email using 'smtplib' library.
import smtplib
mail_details_file_name = "mail_details.txt"
"""mail_details.txt file contain mail ID and password"""
body_of_mail_file_name = "body_of_mail.txt"
"""body_of_mail.txt file contain Subject: and body of mail"""
file_not_found_error_message = "File not found or error in opening the file"
mail_details = []
try:
	with open(mail_details_file_name) as mail_details_file_object:
		information_of_mail = mail_details_file_object.readlines()
	mail_details_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

for line in information_of_mail:
	line = line.rstrip()
	mail_details.append(line)
try:
	with open(body_of_mail_file_name) as body_of_mail_file_object:
		message = body_of_mail_file_object.read()
	body_of_mail_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

smtp_server = "smtp.gmail.com"
port_number = 465
server = smtplib.SMTP_SSL(smtp_server, port_number)
sender_mail_id = mail_details[0]
password = mail_details[1]
server.login(sender_mail_id, password)
print("Login successful.")
receiver_mail_id = input("Enter recipient mail address: ")
server.sendmail(mail_details[0], receiver_mail_id, message)
print("Mail sending...")
print("Mail sent.")
server.quit()