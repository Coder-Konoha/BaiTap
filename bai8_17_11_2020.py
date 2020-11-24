import sys
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
SMTP_Host = "smtp.gmail.com"
sender = #tendangnhap
receivers = input("Nhập địa chỉ email muốn gửi thư: ")
username = #tendangnhap
password = #matkhau
text_subtype = "plain"
content = input("Thông điệp muốn gửi:")
subject = "Test"
n= int(input("Số lần muốn gửi: "))
try:
    for i in range(n):
        msg = MIMEText(content, text_subtype)
        msg["Subject"] = subject
        msg["From"] = sender
        conn = SMTP(SMTP_Host)
        conn.set_debuglevel(False)
        conn.login(username, password)
        try:
            conn.sendmail(sender, receivers, msg.as_string())
        finally:
            conn.quit()
except Exception as error:
    print(error)