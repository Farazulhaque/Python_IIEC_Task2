
#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("commands")

q = cmd.lower()

if ("date" in q):
	output = sp.getoutput("sudo date")
	print(output)
elif ("calender" in q):
	output = sp.getoutput("sudo cal")
	print(output)
elif ("list" in q):
	output = sp.getoutput("sudo ls")
	print(output)
elif ("ip" in q):
	output = sp.getoutput("sudo ifconfig")
	print(output)
else:
	output = sp.getstatusoutput(q)
	status = output[0]
	out = output[1]
	if status == 0:
		print(out)
	else:
		print("Please enter basic linux commands")