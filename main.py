import pandas
import random
import datetime as dt
from smtplib import *

FORMAT_CHOICE = ["letters/letter_1.txt","letters/letter_2.txt","letters/letter_2.txt"]

SENDING_EMAIL = input("Sender emai: ")
PASSWORD = input("Sender password: ")

#-----------Creating message---------------#
def message_creation(name):
    with open(random.choice(FORMAT_CHOICE)) as file:
        letter_format= file.readlines()
        letter_format[0] = f'Dear {name},\n'
        return f"Subject:Happy birthday\n\n\n{''.join(letter_format)}"

#-------------Current date/time------------#
date = dt.datetime.now()
today_month = date.month
today_day = date.day

#-------------Pandas reading csv------------#
data = pandas.read_csv("birthdays.csv")
data_dic  = data.to_dict(orient="records")

#-----------Condition statement-------------#
for dics in data_dic:
    name = dics['name']
    email = dics['email']
    month = dics['month']
    day = dics['day']
    if today_day == day and today_month == month:
        with  SMTP('smtp.gmail.com',587,timeout=120) as connection:
            connection.starttls()
            connection.login(user=SENDING_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=SENDING_EMAIL,to_addrs=email,msg=message_creation(name=name))
            print("message send")


        

