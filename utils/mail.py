
import mimetypes
import os
import smtplib
from email.header import Header
from email.message import EmailMessage


def send_email(server, email, password, to_list: str, subject, content, attach_path):
    """
    发送邮件
    :param server:邮件服务器
    :param email: 发送者邮件地址
    :param password: 不是邮箱密码，登录邮箱开通 POP3/SMTP服务 会获取一个code
    :param to_list: 发送地址列表,多个用逗号隔开
    :param subject: 主题
    :param content: 发送邮件内容
    :param attach_path: 发送邮件附件
    :param debug_level: 发送邮件debug级别,默认为0
    """
    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = to_list
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg.set_content(content, subtype='html', charset='utf-8', cte='8bit')
    if attach_path:
        ctype, encoding = mimetypes.guess_type(attach_path)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(attach_path, 'rb') as fp:
            msg.add_attachment(fp.read(), maintype, subtype,
                               filename=attach_path)
    with smtplib.SMTP_SSL(server) as smtp:
        # HELO向服务器标志用户身份
        smtp.ehlo_or_helo_if_needed()
        # 登录邮箱服务器
        smtp.login(email, password)
        smtp.send_message(msg)


if __name__ == '__main__':
    send_email('smtp.163.com', 'xiaoxm_002@163.com', os.getenv('smtp_code'),
               'xiaoxm_001@163.com', 'good morning', 'good', None)
