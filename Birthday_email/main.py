import random
import smtplib
import datetime
import pandas


birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
now = datetime.datetime.now()
year = now.year
mnt = now.month
day = now.day
today_birthday = []

for birthday in birthdays:
    b_year = birthday["year"]
    b_month = birthday["month"]
    b_day = birthday["day"]
    if b_month==mnt and b_day==day:
        today_birthday.append(birthday)

for birthday in today_birthday:
    password = "your app password"
    my_email = "your email"
    # pick random letter
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open(random.choice(letters)) as file_letter:
        letter = file_letter.read()
        correct_letter = letter.replace("[NAME]", str(birthday["name"]))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{birthday["email"]}",
                                msg=f"Subject:Happy Birthday\n\n{correct_letter}")











