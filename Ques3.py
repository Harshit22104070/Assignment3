import datetime
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
if not (1 <= month <= 12) or not (1 <= day <= 31) or not (1800 <= year <= 2025):
  print("Invalid input date")

else:
  input_date = datetime.datetime(year, month, day)
  
  next_date = input_date + datetime.timedelta(days=1)

  print("Next date:", next_date.strftime("%Y-%m-%d"))
