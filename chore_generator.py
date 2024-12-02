# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# Import things

import pandas
import matplotlib
import datetime

# Set up variables

upper_floor_people = ["Ishayu","Jackson"]
lower_floor_people = ["Dan","Aidan","Hamza"]
first_floor_people = ["Ishayu","Dan","Aidan","Hamza"]
today = datetime.date.today()
sundays = []
chores = []

# Create list of sundays

while today <= datetime.date(2025, 5, 6):
    if today.weekday() == 6:
        sundays.append(today)
    today += datetime.timedelta(days=1)
print(sundays)

# populate chores with correct information

for i in range(len(sundays)):
    if i % 2:
        chores.append([sundays[i], "Clean First floor", first_floor_people[i % 4]])
    else:
        chores.append([sundays[i], "Clean Upper Floors", f"{upper_floor_people[(i // 2) % 2]};{lower_floor_people[(i // 2) % 3]}"])

# convert to dataframe and save

df = pandas.DataFrame(chores, columns=["Date","Chore","Person"])
df.to_csv("chores.csv", index=False)
