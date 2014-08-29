import smtplib
import sys, os, string
import email.mime.text

def sendMail(content, to_addr=-1, title="This is a MekBlog's email"):
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
	# email-user-name
	try:
		email_user_name = settings["email-user-name"]
	except Exception, e:
		raise ValueError("lack email-user-name")
	try:
		email_user_name + ""
	except Exception, e:
		raise TypeError("email-user-name not a %s, but a %s", str, type(email_user_name))
	# email-user-password
	try:
		email_user_password = settings["email-user-password"]
	except Exception, e:
		raise ValueError("lack email-user-password")
	try:
		email_user_password + ""
	except Exception, e:
		raise TypeError("email-user-password not a %s, but a %s", str, type(email_user_password))
	# email-server-host
	try:
		email_server_host = settings["email-server-host"]
	except Exception, e:
		raise ValueError("lack email-server-host")
	try:
		email_server_host + ""
	except Exception, e:
		raise TypeError("email-server-host not a %s, but a %s", str, type(email_server_host))
	# email-server-port
	try:
		email_server_port = settings["email-server-port"]
	except Exception, e:
		raise ValueError("lack email-server-port")
	try:
		email_server_port + ""
	except Exception, e:
		raise TypeError("email-server-port not a %s, but a %s", str, type(email_server_port))
	# check type
	if (type(to_addr) != list) and (type(to_addr) != tuple):
		if __name__ != "__main__":
			raise TypeError
	try:
		content+""
	except Exception, e:
		raise TypeError("Email content not a %s but a %s"% type(str), type(content))
	try:
		title+""
	except Exception, e:
		raise TypeError("Email title not a %s but a %s"% type(str), type(title))
	# if to_addr == -1, send to myself
	if to_addr == -1:
		to_addr = (settings["email-user-name"])
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
	sendMail(content = "hello world!")
