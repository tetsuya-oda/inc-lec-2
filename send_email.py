from smtplib import SMTP

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

import os
import ssl

load_dotenv()

gmail_addr = os.getenv('GMAIL_ADDRESS')
app_passwd = os.getenv('APP_PASSWD')
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')


def send_email(from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    context=ssl.create_default_context()

    with SMTP(smtp_server, smtp_port) as smtp:
        try:
            print("メール送信中...")
            smtp.starttls(context=context)
            smtp.login(gmail_addr, app_passwd)
            smtp.send_message(msg)
            print("メール送信完了")
        except Exception as e:
            print(e)
            print("メール送信失敗")


if __name__ == '__main__':
    from_addr = 'hogehoge@hoge.jp'
    to_addr = 'hogehoge@hoge.jp'
    subject = 'テスト'
    body = 'テストメール'

    send_email(from_addr, to_addr, subject, body)