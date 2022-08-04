
#!/usr/bin/env python

import os

print ("Tu directorio actual es: " + os.getcwd() + "\n\n")


print ("El contenido de este directorio es: ")
os.system('ls')


update = input("Deseas actualizar el sistema?")


if str(update) == 'Si':
	os.system('update')
	print ("El sistema se ha actualizado")

else:

 	print ("de acuerdo, hasta luego.")

