
#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("commands")

dimage =  "sudo docker pull {}".format(cmd)
output = sp.getoutput(dimage)
print(output)