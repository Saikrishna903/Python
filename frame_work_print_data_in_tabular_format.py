#Frame work program print the data in tabular format
menu_cfg_file_name = "menu.cfg"
fields_cfg_file_name = "fields.cfg"
updatable_fields_cfg_file_name = "updatablefields.cfg"
data_file_name = "data.dat"
field_value_not_found_error_message = "NO field_value FOUND"
file_not_found_error_message = "File not found or error in opening the file"

try:
	with open(menu_cfg_file_name) as menu_file_object:
		menu = menu_file_object.read()
	menu_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)
try:
	with open(fields_cfg_file_name) as fields_file_object:
		field_names = fields_file_object.read()
		field_names = eval(field_names)
	fields_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)
try:
	with open(data_file_name) as data_file_object:
		field_values = data_file_object.read()
		field_values = eval(field_values)
	data_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

def save_all_field_values():
	try:
		with open(data_file_name, 'w') as data_file_object:
			data_file_object.write(str(field_values))
		data_file_object.close()
	except FileNotFoundError:
		print(file_not_found_error_message)

def create_record():
	list_of_field_values = []
	field_value_status = True
	list_of_field_values.append(field_value_status)
	for field_name in field_names:
		print(field_name + ": " , end = "")
		field_value = input()
		list_of_field_values.append(field_value)
	field_values.append(list_of_field_values)
	save_all_field_values()
	print("Details are saved successfully.")


def find_columns_length():
	columns_length = []
	for fields_index in range(len(field_names)):
		field_name_length = len(field_names[fields_index])
		for values_index in range(len(field_values)):
			if field_values[values_index][0] == True:
				field_value_length = len(field_values[values_index][fields_index + 1])
				if field_name_length < field_value_length:
					field_name_length = field_value_length
			elif fields_index == len(field_names):
				break
		columns_length.append(field_name_length)
	return columns_length

def print_border(max_length_of_column):
	for counter in range(0, len(field_names)):
		print('+', end = "")
		print('-' * (max_length_of_column[counter] + 2), end = "")
	print('+')

def print_column_headings(max_length_of_column):
	for counter in range(0, len(field_names)):
		print('|', end = " ")
		print(field_names[counter], end = " ")
		print(' ' * (max_length_of_column[counter] - len(field_names[counter])), end = "")
	print('|')

def print_column_values(max_length_of_column):
	for values_index in range(len(field_values)):
		if field_values[values_index][0] == True:
			for fields_index in range(1, len(field_names) + 1):
				field_value = field_values[values_index][fields_index]
				print('|', end = " ")
				print(field_value, end = " ")
				print(' ' * (max_length_of_column[fields_index - 1] - len(field_value)), end = "")
			print('|')			

def print_column_values_in_tabular_format():
	max_length_of_column = find_columns_length()
	print_border(max_length_of_column)
	print_column_headings(max_length_of_column)
	print_border(max_length_of_column)
	print_column_values(max_length_of_column)
	print_border(max_length_of_column)

def print_records():
	print_column_values_in_tabular_format()


def get_key_value():
	return input("Enter " + field_names[0].rstrip() + ": ")

def search_record():
	key_to_search_record = get_key_value()
	for field_value in field_values:
		if field_value[0] == True and field_value[1] == key_to_search_record:
			print("Record info: ")
			print_record(field_value)
			break

def print_record(field_value):
	index_number = 1
	for field_name in field_names:
		print(field_name + ": " , end = "")
		print(field_value[index_number])
		index_number += 1

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
	
	for field_value in field_values:
		if field_value[0] == True and field_value[1] == key_to_update_record:
			update_status = True
			
			print("Do you want to update: ")
			while index_number < len(updatable_fields):
				print(str((index_number + 1)) + "." + field_names[updatable_fields[index_number] - 1])
				index_number += 1
			try:
				update_option = input("Enter your option: ")
				update_option = int(update_option)
			except Exception: 
				print("INVALID OPTION")
			new_field_value = input("Enter new " + field_names[updatable_fields[update_option - 1] - 1] + ": ")
			field_value[updatable_fields[update_option - 1]] = new_field_value
			break
	save_all_field_values()
	if update_status == True:
		print("\nUpdate successful!")
	else:
		print(field_value_not_found_error_message)

def delete_record():
	key_to_delete_record = get_key_value()
	delete_status = False
	index_number = 0
	for field_value in field_values:
		if field_value[0] == True and field_value[1] == key_to_delete_record:
			delete_status = True
			field_value[0] = False
			break
	save_all_field_values()
	if delete_status == True:
		print("\nDelete successful!")
	else:
		print(field_value_not_found_error_message)

functions_list = [create_record, print_records, search_record, update_record, delete_record, exit]
while(True):
	print(menu)
	try:
		user_choice = input("Enter your choice to perform: ")
		user_choice = int(user_choice)
		if user_choice == 6:
			print("Do you really want to exit y or n?")
			exit_choice = input("Enter your exit choice: ")
			if exit_choice == 'Y' or exit_choice == 'y':
				print("Entered exit as your choice")
				exit()
			else: 
				continue
		elif user_choice > 0 and user_choice < 6:
			functions_list[user_choice - 1]()
	except Exception:
		print("INVALID CHOICE")