#Frame work program
import validate_OTP
validate_OTP.generate_OTP()
menu_cfg_file_name = "menu.cfg"
fields_cfg_file_name = "fields.cfg"
updatable_fields_cfg_file_name = "updatablefields.cfg"
data_file_name = "data.dat"
record_not_found_error_message = "NO RECORD FOUND"
file_not_found_error_message = "File not found or error in opening the file"

try:
	with open(menu_cfg_file_name) as menu_file_object:
		menu = menu_file_object.read()
	menu_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

try:
	with open(fields_cfg_file_name) as fields_file_object:
		field_names = fields_file_object.readlines()
	fields_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

try:
	with open(data_file_name) as data_file_object:
		field_values = data_file_object.read()
		records = eval(field_values)
	data_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)


def save_all_records():
	try:
		with open(data_file_name, 'w') as data_file_object:
			data_file_object.write(str(records))
		data_file_object.close()
	except FileNotFoundError:
		print(file_not_found_error_message)

def create_record():
	list_of_field_values = []
	record_status = True
	list_of_field_values.append(record_status)
	for field_name in field_names:
		print(field_name.rstrip() + ": " , end = " ")
		field_value = input()
		list_of_field_values.append(field_value)
	records.append(list_of_field_values)
	save_all_records()
	print("Details are saved successfully.")

def print_field_values(field_value):
	index_number = 1
	for field_name in field_names:
		print(field_name.rstrip() + ": " , end = " ")
		print(field_value[index_number])
		index_number += 1

def print_records():
	no_of_records = 0
	for record in records:
		if record[0] == True:
			no_of_records += 1
			print("\nRecord " + str(no_of_records) + ": ")
			print_field_values(record)
	print("\nNo of records present: " + str(no_of_records))

def search_record():
	key_to_search_record = get_key_value()
	for record in records:
		if record[0] == True and record[1] == key_to_search_record:
			print("Record info: ")
			print_field_values(field_value)
			break

def get_key_value():
	return input("Enter " + field_names[0].rstrip() + ": ")


def update_record():
	try:
		updatable_fields_object = open(updatable_fields_cfg_file_name)
		updatable_fields = []
		for update_field in updatable_fields_object.read():
			update_field = int(update_field)
			updatable_fields.append(update_field)
		updatable_fields_object.close()
	except FileNotFoundError:
		print(file_not_found_error_message)
	index_number = 0
	update_status = False
	key_to_update_record = get_key_value()
	
	for record in records:
		if record[0] == True and record[1] == key_to_update_record:
			update_status = True
			
			print("Do you want to update: ")
			while index_number < len(updatable_fields):
				print(str((index_number + 1)) + "." + field_names[updatable_fields[index_number] - 1].rstrip())
				index_number += 1
			try:
				update_option = input("Enter your option: ")
				update_option = int(update_option)
			except Exception: 
				print("INVALID OPTION")
			new_field_value = input("Enter new " + field_names[updatable_fields[update_option - 1] - 1].rstrip() + ": ")
			record[update_option + 1] = new_field_value
			break
	save_all_records()
	if update_status == True:
		print("\nUpdate successful!")
	else:
		print(record_not_found_error_message)

def delete_record():
	key_to_delete_record = get_key_value()
	delete_status = False
	index_number = 0
	for record in records:
		if record[0] == True and record[1] == key_to_delete_record:
			delete_status = True
			record[0] = False
			break
	save_all_records()
	if delete_status == True:
		print("\nDelete successful!")
	else:
		print(record_not_found_error_message)

functions_list = [create_record, print_records, search_record, update_record, delete_record, exit]
while(True):
	print(menu)
	try:
		user_choice = input("Enter your choice to perform: ")
		user_choice = int(user_choice)
		if user_choice == 6:
			print("Do you really want to exit or cancel?")
			print("1. Exit\n2. Cancel\n")
			exit_option = int(input("Enter your exit choice: "))
			if exit_option == 1:
				print("Entered exit as your choice")
				exit()
			else: 
				continue
		elif user_choice > 0 and user_choice < 6:
			functions_list[user_choice - 1]()
	except Exception:
		print("INVALID CHOICE")
