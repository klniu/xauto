import base64
import email
import imaplib
import socks
import socket

from xauto.web.parse_email import print_info


class MailUtil:
    def __init__(self, email: str, password: str, server: str, port: int,
                 socks5_proxy_address: str = None, socks5_proxy_port: int = None):
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, socks5_proxy_address, socks5_proxy_port,
                              True)
        socket.socket = socks.socksocket

        self.m = imaplib.IMAP4_SSL(server, port)
        self.m.login(email, password)
        self.m.select()

    def read_all(self):
        typ, message_numbers = self.m.search(None,
                                        'ALL')  # change variable name, and use new name in for loop
        for num in message_numbers[0].split():
            typ, data = self.m.fetch(num, '(RFC822)')
            # num1 = base64.b64decode(num)          # unnecessary, I think
            # print(data)  # check what you've actually got. That will help with the next line
            print_info(email.message_from_bytes(data[0][1]))
            break
        self.m.close()
        self.m.logout()


if __name__ == '__main__':
    mail = MailUtil('ym369@klniu.com', 'a12345678', 'imap.gmail.com', 993, '127.0.0.1', 1080)
    mail.read_all()
