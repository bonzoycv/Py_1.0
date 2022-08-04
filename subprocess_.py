
#!/usr/bin/env python3

import subprocess

#se puede colocar el nombre de cualquier
#service para determinar si esta corriendo en el sistema o no.

svc = "bash"

check_cmd = ["ps", "-C", svc]


service_check = subprocess.call(check_cmd)

if service_check == 0:
	print ("The service is running")
else:
	print ("The service is not running.")
	print ("Starting it...")
	subprocess.call(["systemctl", "start", "bash"])
	subprocess.call(check_cmd)


