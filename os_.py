
#!/usr/bin/env python3

# como crear archivos en python con el modulo os

import os

file = input ("Enter a file name: ")

if os.path.isfile(file):
	print ("The file exist.")
else:
	print ("The file does not exist.")
	print ("Creating it...")
	os.system('touch {}'.format(file))
	print ("Done")
