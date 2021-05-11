import smtplib
import os
SUBJECT = "Customer Care"
s = smtplib.SMTP('smtp.gmail.com', 587)


def sendmail(TEXT,email):
    print("successfully registered")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("rahulbhere999@gmail.com", "RockyRahule090862")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("rahulbhere999@gmail.com", email, message)
    s.quit()

