#Image processing using PIL library
from PIL import Image

def save_image(image_object, file_name):
	image_object.save(file_name)
	print("Image saved successfully.")

def rotate_image(rotate_value):
	image_after_rotate = image.rotate(rotate_value)
	return image_after_rotate

def convert_image_to_gray_scale():
	return image.convert(mode = 'L')

def show_image(file_name):
	image_after_modify = Image.open(file_name)
	image_after_modify.show()

try:
	image_file_name = input("Enter image file name: ")
	image = Image.open(image_file_name)
	print("Do you want?\n1. Rotate\n2. Convert to grayscale")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		rotation_value = int(input("Enter rotate value (0 to 360): "))
		rotated_image = rotate_image(rotation_value)
		global_image_obj = rotated_image
		print("Image Rotated.")
	elif choice == 2:
		print("Image processing...")
		converted_image = convert_image_to_gray_scale()
		global_image_obj = converted_image
		print("Image is converted to grayscale.")
	else:
		print("INVALID CHOICE")
except FileNotFoundError:
	print("FILE NOT FOUND OR ERROR IN OPENING FILE")
	exit()

print("Provide a file name to save: ", end = "")
file_name_to_save = input()
save_image(global_image_obj, file_name_to_save)
print("Do you want to see saved image or exit?\n1. Show image\n2. Exit")
option = int(input("Enter your choice: "))
if choice == 1:
	show_image(file_name_to_save)
elif choice == 2:
	print("Entered exit as your choice.")
	exit()
else:
	print("INVALID CHOICE")