import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

send_email = '2017253020@yonsei.ac.kr'
send_pwd = os.environ['GMAILPW']

recv_email = 'one2ol@daum.net'

smtp_name = 'smtp.gmail.com'
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = 'html로 보내는 메일 입니다'
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #ff0000;">글자의 색깔을 지정하거나</span></p>
<h1><strong>크기를 조정할 수 있습니다</strong></h1>
<p>표도 만들 수 있습니다.</p>
<table style="height: 76px;" width="352">
<tbody>
<tr>
<td style="width: 81px;">1</td>
<td style="width: 81px;">2</td>
<td style="width: 81px;">3</td>
<td style="width: 81px;">4</td>
</tr>
<tr>
<td style="width: 81px;">표</td>
<td style="width: 81px;">도</td>
<td style="width: 81px;">만</td>
<td style="width: 81px;">들</td>
</tr>
<tr>
<td style="width: 81px;">수</td>
<td style="width: 81px;">있</td>
<td style="width: 81px;">습</td>
<td style="width: 81px;">니다</td>
</tr>
</tbody>
</table>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)

s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()