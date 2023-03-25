import smtplib
import time

successfull=0

test=0

email_adres=input("enter target e-mail adres (example: example@gmail.com)\n")

word = input("what do you want to send? (example: hello my friend)\n")

num=int(input("enter how many attempts to make (example: 5) \n"))

invertal=int(input("enter send invertal (example: 5) \n"))



mail_send=smtplib.SMTP("smtp.gmail.com",587)

mail_send.ehlo()

mail_send.starttls()

mail_send.login("wqesacxzsadweqweqweew@gmail.com","zxqc wqtb zjug qjwq")

while successfull < num and test < num:
    try:
        mail_send.sendmail("wqesacxzsadweqweqweew@gmail.com",email_adres,word)
        successfull+=1
        print(f"email {successfull} send succesfully")
    except:
        test+=1

if test==num:
    print("sending failed")
    print("check your internet connection")
    print("try enter valid email adress")
else:
    print(f"{num} emails send")
    print("sending completed successfully")

mail_send.quit()