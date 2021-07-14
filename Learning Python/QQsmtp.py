import smtplib

smtpObj = smtplib.SMTP('smtp.qq.com')
print(type(smtpObj))
print(smtpObj.ehlo())
print(smtpObj.starttls())
print(smtpObj.login('xxxxx@qq.com', 'My_password'))
smtpObj.sendmail('xxxxx@qq.com', '334230789@qq.com', 'Subject: Test SMTP service message.\nHello World.')
print(smtpObj.quit())
