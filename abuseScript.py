# package used for actually sending things
import imaplib
import smtplib
import email
import time
import email.parser
import re

GMAIL_USER = 'pythontesting1234@gmail.com'
GMAIL_PWD = 'kuksugarbert'
SMTP_SERVER = "imap.gmail.com"


def read_email():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(GMAIL_USER, GMAIL_PWD)
        mail.select("inbox")

        type, data = mail.search(None, "All")
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            type, data = mail.fetch(str(i), '(RFC822)')

            msg = email.message_from_string(data[0][1].decode('utf-8'))

            '''
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_string(response_part[1])
                    email_subject = message['subject']
                    email_from = message['from']
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')
            '''
            containsInfringement(msg)
            print(msg)
            print("################################################")
            # print("Connected successfully to mail")

    except Exception as e:
        print(e)
        print("Error: Could not connect to mail")


def containsInfringement(mail):
    # print(mail)
    stringMail = str(mail)

    regexp = re.compile('kalle')
    if regexp.search(stringMail):
        print("Contains infringement")
    else:
        print("Nope")


    # raw_email_string = mail.decode("utf-8")
    # print(raw_email_string)

    # b = email.message_from_string(mail)
    # print(email['To'])
    # print(email['From'])
    # print(b)


"""
if(b).is_multipart():
    for payload in b.get_payload():
        print(payload.get_payload())
else:
    print(b.get_payload)
"""


def send_email():
    sender = GMAIL_USER
    receiver = GMAIL_USER

    message = """From: From person
    To: To Person

    This is a mail??
    """

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PWD)
        server.sendmail(sender, receiver, message)
        server.close()
        print("NU FAN SKA DET HA FUNKAT, HELVETE")


    except:
        print("Could not send email")


# Read through the mail, if it contains <infringement> move forward
def checkIfInfringement():
    infringement = False

    infringement = readFromFile()

    return infringement


def readFromFile():
    file = open("testfile.txt")
    for line in file:
        if 'infringement' in line:
            file.close()
            return True
        else:
            file.close()
            return False


# Code starts executing here
while True:
    read_email()

if checkIfInfringement():
    send_email()

else:
    print("No infringement")
