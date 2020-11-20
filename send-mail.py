import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sub = input("[+] subject > ")
msg = input("[?] message > ")
to = "cybersecurty922@gmail.com"
#The mail addresses and password
sender_address = 'rehmanazhar922@gmail.com'
sender_pass = 'passwrd'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = to
message['Subject'] = sub   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(msg, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, to, text)
session.quit()
print('Mail Sent')
