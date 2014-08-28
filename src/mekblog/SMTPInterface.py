import smtplib
import sys, os, string
import email.mime.text


settings = {}

# test mode
if __name__ == "__main__":
	import json
	fp = open("test.json")
	settings = json.load(fp)
	fp.close()
# normal mode
else:
	import mekblog.config
	settings = mekblog.config.settings

# check message
try:
	email_user_name = settings["email-user-name"]
	email_user_password = settings["email-user-password"]
	email_server_host = settings["email-server-host"]
	email_server_port = settings["email-server-port"]
except Exception, e:
	raise e

def sendMail(to_addr, content, title="This is a MekBlog's email"):
	# check type
	if (type(to_addr) != list) and (type(to_addr) != tuple):
		if __name__ != "__main__":
			raise TypeError
	try:
		content+""
	except Exception, e:
		raise e
	try:
		title+""
	except Exception, e:
		raise e
	#create a SMTP object
	smtp = smtplib.SMTP()
	#set debug level
	if __name__ == "__main__":
		smtp.set_debuglevel(1)
	else:
		smtp.set_debuglevel(0)
	# connecti to SMTP server
	try:
		smtp.connect(email_server_host, email_server_port)
	except Exception, e:
		raise e
	# use ssl
	smtp.starttls()
	# log in
	try:
		smtp.login(email_user_name, email_user_password)
	except Exception, e:
		raise e

	msg = email.mime.text.MIMEText(content)
	msg["From"] = email_user_name
	msg["To"] = ";".join(to_addr)
	msg["Subject"] = title
	smtp.sendmail(email_user_name, to_addr, msg.as_string())
	smtp.quit()

if __name__ == "__main__":
	sendMail( to_addr = (email_user_name,), content = "hello world!")