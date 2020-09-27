
#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

name = form.getvalue("osname")
image = form.getvalue("osimage")

cmd =  "sudo docker run -d -it --name {0} {1}".format(name,image)

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
	print("{} OS Launched with name {}...".format(image,name))
else:
	print("{0} \nError in launching OS with name {1}".format(out,name))