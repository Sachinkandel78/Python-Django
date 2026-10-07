#Advanced topics
#1. Comprehension (list,set,dict)

# #Without comprehension
# numbers = [1,2,3,4,5,6,7,8,9.10,11,12,13,14]
# even_numbers = []
# for number in numbers:
#     if number % 2 ==0:
#         even_numbers.append(number)
# print(even_numbers)

#With comprehension
numbers = [1,2,3,4,5,6,7,8,9.10,11,12,13,14]
even_numbers = [number for number in numbers if number%2==0] 
#or yesarin lekhna ni milxa jasai same ho 
#yo vanya even_numbers vitra euta number rakhni jun; aba for bata number ma aauxa ani teslai % 2 ==0 garda aako number rakhni
# even_numbers = [number
#                  for number in numbers
#                    if number%2==0]
print(even_numbers)

users = [
    {
    "name": "Sachin",
    "email": "sachin@gmail.com"
    },
    {
    "name": "Ram",
    "email": "ramu@gmail.com"
    },
    {
    "name": "hari",
    "email": "hari@gmail.com"
    },
    {
    "name": "Shyam",
    "email": "shyamey@gmail.com"
    },
    {
        "name": "hari",
        "email": "hari@gmail.com"
        }
    
        ]
# send_email(["sachin@gmail.com" "shyamey@gmail.com"])

emails1 = [user["email"] for user in users]  #list contains duplicacy
emails2 = {user["email"] for user in users}  #set dont accept duplicacy
print(emails1)
print(emails2)

#2. Higher order Functions