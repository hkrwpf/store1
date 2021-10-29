import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

msg_from = "1158493671@qq.com"
pwd = "yjqlzmnfstyyjbda"
to = "1544606475@qq.com"
# 2431320433
msg = MIMEMultipart()
msg["From"] = msg_from
msg["To"] = to

msg["Subject"] = Header('主题：HKR登录测试报告', 'utf-8')
msg.attach(MIMEText('测试报告', 'plain', 'utf-8'))

att1 = MIMEText(open(r"D:\ruanjiandakai\自动化测试\autoweb03\test\正常登陆.html", 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename = "test.html"'
msg.attach(att1)

att2 = MIMEText(open(r"D:\ruanjiandakai\自动化测试\autoweb03\test\账号或密码有一个错误.html", 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename = "test.html"'
msg.attach(att2)

ss = smtplib.SMTP_SSL("smtp.qq.com")
ss.connect('smtp.qq.com')
ss.login(msg_from, pwd)
ss.sendmail(msg_from, to, msg.as_string())
















