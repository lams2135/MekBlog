import smtplib
import sys, os, string
import email.mime.text
if __name__ == "__main__":
	import config
else:
	import mekblog

def sendEventHandler(obj):
	try:
		obj['content']
		obj['to_addr']
		obj['title']
	except Exception, e:
		raise TypeError('Unavaliable event object received.')
		return
	sendMail(obj['content'], obj['to_addr'], obj['title'])

# set up SMTP service listening
subscriber_obj = {'name':'email.sendmail', 'response-method':sendEventHandler}
mekblog.notification.register_subscriber('email.sendmail', subscriber_obj)

def sendMail(content, to_addr=-1, title="This is a MekBlog's email"):
	settings = {}
	# test mode
	if __name__ == "__main__":
		settings = config.settings_object()
		settings.load("test.json")
	# normal mode
	else:
		settings = mekblog.config.settings
	# check message
	# email-user-name
	email_user_name = settings.email.user.name.get()
	# email-user-password
	email_user_password = settings.email.user.password.get()
	# email-server-host
	email_server_host = settings.email.host.get()
	# email-server-port
	email_server_port = settings.email.port.get()
	# check type
	# if to_addr == -1, send to myself
	if to_addr == -1:
		to_addr = (settings.email.user.name.get())
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
