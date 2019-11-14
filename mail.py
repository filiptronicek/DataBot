import yagmail 

from mailAuth import auth, emailTo

def sendMail(message):
    yag = yagmail.SMTP(auth[0],auth[1])
    yag.send(emailTo, 'DataBot', message)