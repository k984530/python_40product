import smtplib
from email.mime.text import MIMEText
import os 

send_email = '2017253020@yonsei.ac.kr'
send_pwd = os.environ['GMAILPW']

recv_email = 'one2ol@daum.net'

smtp_name = 'smtp.gmail.com'
smtp_port = 587

text = """
테스트용 메세지
한 번에 성공할까요
"""
msg = MIMEText(text)

msg['Subject'] = '제목입니다'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit