from Tkinter import *
import sys
import os
import tkMessageBox
import error_mes
import subprocess
main = Tk()
#Variables that are globally needed
file_input = "" #whats put into the text box
_FILE_= "" #File the user wants to open; readapt to be synonymous with save?
open_a_file = "" #will be the entry field for opening a file
target = ""
new_file_ = ""
new_file_name = ""
isnewfile = "no"
def get_from_text():
	global file_input
	try:
		file_input = my_text_box.get("1.0", END)
		print file_input
	except:
		file_input = 'UHOH'
		print file_input

def save(): #This function can definitely be improved
	global file_input, target, _FILE_, my_text_box, new_file_name
	try:
		file_input = my_text_box.get("1.0", END)
		target = open(_FILE_, "r+w")
		target.truncate()
		target.write(file_input)
	except:
		file_input = my_text_box.get("1.0", END)
		target = open(new_file_name, "r+w")
		target.truncate()
		target.write(file_input)

def exit_application():
	sys.exit(0)

def menu_open_file():
	global _FILE_, open_a_file, save, my_text_box
	try:
		open_a_file = Entry()
		open_a_file.grid(row = 3, column = 0)
		open_a_file.insert(0, "Path to File to Open")
		#save.grid_forget()
		Button(main, text = "Click to Open", command = get_file).grid(row = 4, 
																column = 0)
	except:
		error_mes.error()

def get_file():
	global _FILE_, open_a_file, my_text_box
	try:	
		_FILE_ = open_a_file.get()
		target = open(_FILE_, "r+w")
		opened_file = target.read()
		try:
			my_text_box.insert(INSERT, opened_file)
		except:
			error_mes.error()
	except:
		error_mes.error()

def new_file():
	global new_file_, my_text_box
	my_text_box.delete("1.0", END)
	try:
		new_file_ = Entry()
		new_file_.grid(row = 3, column = 0)
		save_button = Button(main, text = "Click to Save", command = save_new_file)
		save_button.grid(row = 4, column = 0)
	except:
		error_mes.error()

def save_new_file():
	global new_file_, new_file_name, my_text_box, target
	new_file_name = new_file_.get()
	target = open(new_file_name, "w")
	target.write(my_text_box.get("1.0", END))


def add_date():
	global my_text_box
	date  = subprocess.check_output('date', shell = True)
	my_text_box.insert(INSERT, date)


def diary_preset():
	error_mes.error()

def c_preset():
	global my_text_box, target
	c_preset_text = open("/home/vhx/Documents/code/python/tkinter/text_editor/c_preset.txt").read()
	my_text_box.insert(INSERT, c_preset_text)
	Button(main, text = "Compile", command = compile_c).grid(row = 0, column = 0)

def compile_c():
	global open_a_file
	os.system("cc " + open_a_file + "; ./a.out")

my_text_box = Text(main, bg = "black", fg = "white", insertbackground = "white",
																tabs = ("1c"))
my_text_box.grid(row = 0, column = 0)
#The Menu
menu = Menu(main)
menu2 = Menu(main)
main.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New...", command = new_file)
filemenu.add_command(label = "Open...", command = menu_open_file)
filemenu.add_command(label = "Save", command = save)
filemenu.add_command(label = "Add Date", command = add_date)
filemenu.add_command(label = "C Preset", command = c_preset)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_application)

main.mainloop()