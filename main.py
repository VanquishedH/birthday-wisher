import pandas
import datetime as dt
from random import randint
import smtplib

password = "uegf qwqq ukxt ttyz"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

now = dt.datetime.now()
day = now.day
month = now.month

file_name = f"letter_templates/letter_{randint(1,10)}.txt"

for value_1, value_2 in zip(data_dict["month"].values(), data_dict["day"].values()):
    if value_1 == month and value_2 == day:
        data_row = data[data["month"] == value_1]
        name = data_row.name.item()
        address = data_row.email.item()
        with open(file_name, "r") as file:
            data = file.read()
            data_processed = data.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=address, password=password)
            connection.sendmail(from_addr=address, to_addrs=address, msg=f"Subject: Happy Birthday!\n\n{data_processed}")