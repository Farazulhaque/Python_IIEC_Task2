
#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("commands")

q = cmd.lower()

if ((("launched" in q) or ("run" in q)) and (("before" in q) or ("past" in q) or ("previously" in q))):
	output = sp.getoutput("sudo docker ps -a")
	print(output)
elif (("running" in q) and ("currently" in q)):
	output = sp.getoutput("sudo docker ps")
	print(output)
elif (("show" in q) and ("docker" in q) and ("images" in q)):
	output = sp.getoutput("sudo docker images")
	print(output)
elif ((("remove" in q) or ("delete" in q) or ("clear" in q)) and ("docker" in q) and ("images" in q) and ("running" in q)):
	output = sp.getoutput("sudo docker rm -f $(docker ps -a -q)")
	print(output)
else:
	output = sp.getstatusoutput(q)
	status = output[0]
	out = output[1]
	if status == 0:
		print(out)
	else:
		print("Please enter basic docker commands")