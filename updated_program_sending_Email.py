#Program to send email using 'smtplib' library.
import smtplib
import stdiomask
body_of_mail_file_name = "body_of_mail.txt"
"""body_of_mail.txt file contain Subject: and body of mail"""
file_not_found_error_message = "File not found or error in opening the file"
try:
	with open(body_of_mail_file_name) as body_of_mail_file_object:
		message = body_of_mail_file_object.read()
	body_of_mail_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)
smtp_server = "smtp.gmail.com"
port_number = 465
server = smtplib.SMTP_SSL(smtp_server, port_number)
sender_mail_id = input("Enter your mail ID: ")
password = stdiomask.getpass(prompt = 'Password: ')
server.login(sender_mail_id, str(password))
print("Login successful.")
receiver_mail_id = input("Enter recipient mail address: ")
server.sendmail(sender_mail_id, receiver_mail_id, message)
print("Mail sending...")
print("Mail sent.")
server.quit()