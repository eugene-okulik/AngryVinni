from datetime import datetime


date = "Jan 15, 2023 - 12:05:33"
date_object = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")

# print month full name
print(date_object.strftime("%B"))

# print formatted date
formatted_date = date_object.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)
