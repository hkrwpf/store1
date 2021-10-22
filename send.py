import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

msg_from = "1158493671@qq.com"
pwd = "yjqlzmnfstyyjbda"
to = "2431320433@qq.com"

msg = MIMEMultipart()
msg["From"] = msg_from
msg["To"] = to

msg["Subject"] = Header('主题:测试报告 ', 'utf-8')
msg.attach(MIMEText('测试报告 ', 'plain', 'utf-8'))

att1 = MIMEText(open(r"D:\ruanjiandakai\day14\txt\工商银行开户.html",'rb').read(), 'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.html"'
msg.attach(att1)

att2 = MIMEText(open(r"D:\ruanjiandakai\day14\txt\工商银行取钱.html",'rb').read(), 'base64','utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test.html"'
msg.attach(att2)

att3 = MIMEText(open(r"D:\ruanjiandakai\day14\txt\工商银行存钱.html",'rb').read(), 'base64','utf-8')
att3["Content-Type"] = 'application/octet-stream'
att3["Content-Disposition"] = 'attachment; filename="test.html"'
msg.attach(att3)

att4 = MIMEText(open(r"D:\ruanjiandakai\day14\txt\工商银行转账.html",'rb').read(), 'base64','utf-8')
att4["Content-Type"] = 'application/octet-stream'
att4["Content-Disposition"] = 'attachment; filename="test.html"'
msg.attach(att4)

ss = smtplib.SMTP_SSL("smtp.qq.com")
ss.connect('smtp.qq.com')
ss.login(msg_from, pwd)
ss.sendmail(msg_from, to, msg.as_string())


