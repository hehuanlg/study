import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
smtpserver = input('smtpserver:')
user = input('user:')
password = input('password:')
# sender = user
receiver = input('to:')
# subject = 'python email 2'
# msg = MIMEText('<html><h1>第二次发送<h1><html>','html','utf-8')
# msg['subject'] = Header(subject,'utf-8')
# msg['From'] = sender
# msg['To'] = receiver
#
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()
# print('发送成功')

subject = 'python send emiall'
msgroot = MIMEMultipart('related')
sender = user
msgroot['subject'] = subject
msgroot['From'] = sender
msgroot['To'] = receiver
#构造附件
att = MIMEText(open('test.bmp','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application/octet-strem'
att['Content-Disposition'] = 'attachment;filename="test.bmp"'
msgroot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgroot.as_string())
smtp.quit()
