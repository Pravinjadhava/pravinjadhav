#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("r07.pravin@gmail.com","8792437080")
message ="Message_you_need_send"
s.sendmail("r07.pravin@gmail.com","nikhiln559@gmail.com",message)
s.quit()