# # from datetime import datetime

# # ## calculate age

# # today = datetime.today()
# # # print(today)  #2026-10-07 09:06:43.087099 (date time duitai dinxa)

# # today_date = today.date()
# # # print(today_date)  #2026-10-07 (date matra dinxa )

# # birth_date = input("Enter your birth date (YYYY-MM-DD): ")
# # actual_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
# # # print(actual_birth_date)

# # date_difference = today_date - actual_birth_date
# # print(date_difference)

# # years = date_difference.days // 365
# # remaining_days = date_difference.days % 365
# # months = remaining_days // 30
# # days = remaining_days % 30
# # print(years)
# # print(months)
# # print(days)

# # print(type(today_date))
# # print(type(birth_date))
# # print(type(actual_birth_date))

# # print(actual_birth_date)

# # # age = today_date - birth_date  #Error aauxa tyo different data type vako karan le
# # # print(age)
# # print(birth_date)
# # print(today_date)

from dateutil.relativedelta import relativedelta
from datetime import datetime

# today = datetime.today()
# today_date = today.date()
# birth_date = input("Enter your birth date (YYYY-MM-DD): ")
# actual_birth_date = datetime.strptime(birth_date, "%Y-%M-%d").date()
# date_difference = relativedelta(today_date, actual_birth_date)
# print("Year: ",date_difference.years)
# print("Months: ", date_difference.months)
# print("Days: ",date_difference.days)

# OTPs -> expiry time
otp = {
    "value": "123789",
    "created_at": datetime,
    "expires_at": datetime
}

from datetime import datetime, timedelta
import time

otp = {
    "value": "123456"
}

now = datetime.now()
# print(now)

otp["created_at"] = now

expiry_time = now + timedelta(seconds=2)

otp["expires_at"] = expiry_time

print(otp)

time.sleep(5)

## otp verification
if otp["expires_at"] < datetime.now():
        print("Expired")
else:
        print("Verified")