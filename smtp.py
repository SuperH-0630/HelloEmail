from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from time import strftime, localtime


class Email:
    def __init__(self, user, passwd, server, port=465, ssl=True):
        self.user = user
        self.passwd = passwd
        self.server = server
        self.port = port
        self.is_ssl = ssl

        if self.is_ssl:
            self.smtp = smtplib.SMTP_SSL(self.server, self.port)
        else:
            self.smtp = smtplib.SMTP(self.server, self.port)
        self.smtp.login(self.user, self.passwd)

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_email(self, name, to, to_email, subject, text):
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = self._format_addr(f'{name} <{self.user}>')
        msg['To'] = self._format_addr(f'{to} <{to_email}>')
        msg['Subject'] = Header(subject, 'utf-8').encode()
        msg["Date"] = Header(strftime('%a, %d %b %Y %H:%M:%S %z', localtime())).encode()
        self.smtp.sendmail(self.user, [to_email], msg.as_string())

    def quit(self):
        if self.smtp:
            self.smtp.quit()
            self.smtp = None
