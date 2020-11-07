#Frame work program using XML
import xml.etree.ElementTree as ET
menu_cfg_file_name = "menu.cfg"
data_file_name = "data.xml"
fields_cfg_file_name = "fields.cfg"
updatable_fields_cfg_file_name = "updatablefields.cfg"
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
		field_names = fields_file_object.read()
		field_names = eval(field_names)
	fields_file_object.close()
except FileNotFoundError:
	print(file_not_found_error_message)

try:
	tree = ET.parse(data_file_name)
	root = tree.getroot()
except Exception:
	print("ERROR")

def save_all_records():
	try:
		with open("data.xml", "wb") as data_file_object:
			tree.write(data_file_object)
		data_file_object.close()
	except FileNotFoundError:
		print(file_not_found_error_message)

def create_record():
	parent_node = ET.Element("Record")
	parent_node.set('status', 'A')
	for field_name in field_names:
		child_node = ET.SubElement(parent_node, field_name)
		print(field_name + ": " , end = "")
		field_value = input()
		child_node.text = field_value
	root.append(parent_node)
	save_all_records()
	print("Details are saved successfully.")

def print_record(record_info):
	for field_name in field_names:
		print(field_name + ": ", end = "")
		print(record_info.find(field_name).text)

def print_records():
	no_of_records = 0
	for record in root.findall('Record'):
		if record.attrib['status'] == 'A':
			no_of_records += 1
			print("Record " + str(no_of_records) + ": ")
			print_record(record)
	print("\nNumber of records present: " + str(no_of_records))

def get_key_value():
	return input("Enter " + field_names[0] + ": ")

def delete_record():
	key_value = get_key_value()
	delete_status = False
	for record in root.findall('Record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == key_value:
			record.set('status', 'D')
			delete_status = True
			break
	if delete_status == True:
		save_all_records()
		print("Delete successful")
	else:
		print(record_not_found_error_message) 

def search_record():
	key_value = get_key_value()
	for record in root.findall('Record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == key_value:
			print_record(record)
			break

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
	update_status = False
	key_value = get_key_value()
	index_number = 0
	for record in root.findall('Record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == key_value:
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
			record.find(field_names[updatable_fields[update_option - 1] - 1].rstrip()).text = new_field_value	
			break
	if update_status == True:
		save_all_records()
		print("Update successful")
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
