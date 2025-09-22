import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_notification(subject, content, receiver_email, sender_email, sender_password, smtp_server, smtp_port):
    """发送邮件通知"""
    try:
        # 创建邮件对象
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header(sender_email)
        msg['To'] = Header(receiver_email)
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接SMTP服务器并发送邮件
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print("邮件通知已发送")
    except Exception as e:
        print(f"发送邮件失败: {e}")

def monitor_log_file(file_path, keyword, email_config):
    """监听日志文件，检测是否出现指定关键字并发送邮件通知"""
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return

    # 获取文件初始大小
    file_size = os.path.getsize(file_path)

    try:
        while True:
            # 获取当前文件大小
            current_size = os.path.getsize(file_path)

            # 如果文件大小增加，说明有新内容写入
            if current_size > file_size:
                # 打开文件并定位到上次读取的位置
                with open(file_path, 'r', encoding='utf-8') as file:
                    file.seek(file_size)
                    new_content = file.read()

                    # 检查新内容中是否包含关键字
                    if keyword in new_content:
                        print(f"检测到关键字 '{keyword}' 在日志中出现！")
                        print("新增内容：")
                        print(new_content)

                        # 发送邮件通知
                        subject = f"日志监控警告：发现关键字 '{keyword}'"
                        content = f"在日志文件 {file_path} 中检测到关键字 '{keyword}'\n\n新增内容：\n{new_content}"
                        send_email_notification(
                            subject, content, 
                            email_config['receiver_email'],
                            email_config['sender_email'],
                            email_config['sender_password'],
                            email_config['smtp_server'],
                            email_config['smtp_port']
                        )

                # 更新文件大小
                file_size = current_size

            # 每隔1秒检查一次
            time.sleep(1)

    except KeyboardInterrupt:
        print("程序已停止")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 配置日志文件路径和要监听的关键字
    log_file_path = "flask.log"  # 请替换为实际的日志文件路径
    target_keyword = "webhook"

    # 配置邮件通知信息
    email_config = {
        'sender_email': 'xxxx@qq.com',  # 发件人邮箱
        'sender_password': 'xxxxx',  # 发件人邮箱密码或授权码
        'receiver_email': 'xxxxx@qq.com',  # 收件人邮箱
        'smtp_server': 'smtp.qq.com',  # SMTP服务器地址
        'smtp_port': 465  # SMTP服务器端口
    }
    
    print(f"开始监听日志文件: {log_file_path}")
    print(f"监听关键字: {target_keyword}")
    monitor_log_file(log_file_path, target_keyword, email_config)