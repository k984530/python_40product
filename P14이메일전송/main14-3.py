import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

send_email = '2017253020@yonsei.ac.kr'
send_pwd = os.environ['GMAILPW']

recv_email = 'one2ol@daum.net'

smtp_name = 'smtp.gmail.com'
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "첨부파일 테스트 입니다."
msg['From'] = send_email
msg['To'] = recv_email

text = """
테스트용 메세지 입니다.
감사합니다.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'P14이메일전송\첨부파일.txt'
with open(etc_file_path, 'rb') as f :
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition', 'attachment', filename = '첨부파일.txt')
    msg.attach(etc_part)
    
s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()