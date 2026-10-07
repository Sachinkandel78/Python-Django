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

# 

import random
# # print(random.randint(1,11))

# secret_number = random.randint(1,10)
# life = 5
# while True:
#     print("Life: ", life)
#     user_guess = int(input("Guess the secret:"))

#     if user_guess == secret_number:
#         print("You won the game")
#         break
#     else:
#         life = -1
#         if life == 0:
#             print("You lost the game")
#             break
#         else:
#             print("Wrong guess. Please try again!")

coupons = ["120312392394", "19284792834", "1982739182", "29837983745"]
winner = random.choices(coupons)
print(winner)


cards = [1,2,3,4,5,6,7,8,9,10,"A","J","K","Q"]

random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
print(cards)


ram = cards[0:3] # yo vanya 0,1,2 (3 include hudaina)
hari = cards[3:6]
shyam = cards[6:9]

print(ram)
print(hari)
print(shyam)