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
# numbers = [1,2,3,4,5,6,7,8,9.10,11,12,13,14]
# even_numbers = [number for number in numbers if number%2==0] 
# #or yesarin lekhna ni milxa jasai same ho 
# #yo vanya even_numbers vitra euta number rakhni jun; aba for bata number ma aauxa ani teslai % 2 ==0 garda aako number rakhni
# # even_numbers = [number
# #                  for number in numbers
# #                    if number%2==0]
# print(even_numbers)

# users = [
#     {
#     "name": "Sachin",
#     "email": "sachin@gmail.com"
#     },
#     {
#     "name": "Ram",
#     "email": "ramu@gmail.com"
#     },
#     {
#     "name": "hari",
#     "email": "hari@gmail.com"
#     },
#     {
#     "name": "Shyam",
#     "email": "shyamey@gmail.com"
#     },
#     {
#         "name": "hari",
#         "email": "hari@gmail.com"
#         }
        # ]
# send_email(["sachin@gmail.com" "shyamey@gmail.com"]) # yo paxi padxau send_mail() function user garera afulai ma lageyko email id ma mail pathauni ho

# emails1 = [user["email"] for user in users]  #list contains duplicacy
# emails2 = {user["email"] for user in users}  #set dont accept duplicacy
# print(emails1)
# print(emails2)

#2. Higher order Functions
# Function -> parameters and arguments vitra pani function

# #A. Filter
# numbers = [1,2,3,4,5,6,7,8,9.10,11,12,13,14]

# def odd_filter(x):
#     if x%2 == 1:
#         return True
#     else:
#         return False
# #     return x%2 == 1 # 1%2 == 1 => 1 == 1 => True (mathiko if else ko shortcut ho hai yo lekheyni hunxa same ho kura bas yo shortcut vayo)
# # print(odd_filter(1)) # ouptut=true
# # print(odd_filter(2)) # output = false

# odd_numbers = filter(odd_filter, numbers)
# print(odd_numbers)    # o/p = <filter object at 0x0000027D84112650>

# odd_numbers_list = list(odd_numbers)
# print(odd_numbers_list)  #o/p = [1, 3, 5, 7, 11, 13]


# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))


#B. Map# 
# users = [
#     {
#     "name": "Sachin",
#     "email": "sachin@gmail.com"
#     },
#     {
#     "name": "Ram",
#     "email": "ramu@gmail.com"
#     },
#     {
#     "name": "hari",
#     "email": "hari@gmail.com"
#     },
#     {
#     "name": "Shyam",
#     "email": "shyamey@gmail.com"
#     },
#     {
#         "name": "hari",
#         "email": "hari@gmail.com"
#         }
#         ]
# def get_email(user):
#     return user["email"]

# emails= map(get_email,users)
# print(emails)   #ouput = <map object at 0x000002990E6C9300>
# # print(set(emails))  # output set ko form ma aauxa ={'sachin@gmail.com', 'shyamey@gmail.com', 'ramu@gmail.com', 'hari@gmail.com'}
# print(list(emails)) # output list ko form ma aauxa =['sachin@gmail.com', 'ramu@gmail.com', 'hari@gmail.com', 'shyamey@gmail.com', 'hari@gmail.com']


# #C. Sorted
# #normal order sort
# numbers = [1,3,2,7,6,4,5,4,8,10,0,1]
# numbers.sort()
# print(numbers)   #[0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 10]

# #Higher order sort

# students = [
#     {
#         "name": "ram", 
#         "total_marks": 345
#     },
#     {
#         "name": "roshan",
#         "total_marks": 500,
#     },
#     {
#         "name": "harry",
#         "total_marks": 150,
#     }
# ]

# def get_total_marks(student):
#     return student["total_marks"]

# # sorted_list = sorted(students, key= get_total_marks)  
# # print(sorted_list)  #[{'name': 'harry', 'total_marks': 150}, {'name': 'ram', 'total_marks': 345}, {'name': 'roshan', 'total_marks': 500}]

# sorted_list = sorted(students, key= get_total_marks , reverse=True)  # Yesso reverse = true garda ascending ko reverse vanya descending bata aauxa answer . By default chai ascending naee hunxa
# print(sorted_list) #[{'name': 'roshan', 'total_marks': 500}, {'name': 'ram', 'total_marks': 345}, {'name': 'harry', 'total_marks': 150}]


#D. Lambda Function
#Tyo mathiko filter wala example yesari garna pani sakinxa without declaring one time function vaneyko filter use garda function ko name chaeenxa .yedi tyo function paxi hamlai kam lagdeyna
#vaney hami fokkat ma function define garirahanu vanda lambda use garxau jun afai ma one time fucntion so yeso garda code ko size ni ghatxa tei ho kura
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]
odd_numbers = filter(lambda x:x%2 ==1, numbers)
print(list(odd_numbers))  #[1, 3, 5, 7, 9]


""" ===============
     class code 
    ===============
    """
# Advanced concepts

# 1. comprehension (list, set, dict)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
        
        
# print(even_numbers)

# even_numbers = [number for number in numbers if number % 2 == 0]

# print(even_numbers)

# users = [
#     {
#         "name": "Ram", 
#         "email": "ram@gmail.com"
#     },
#     {
#         "name": "hari", 
#         "email": "hari@gmail.com"
#     },
#     {
#         "name": "geeta", 
#         "email": "geeta@gmail.com"
#     },
#     {
#         "name": "saugat", 
#         "email": "saugat@gmail.com"
#     },
#     {
#         "name": "Roshan", 
#         "email": "ram@gmail.com"
#     }
# ]


# send_mail(["ram@gmail.com", "saugat@gmail.com"])

# emails = [user["email"] for user in users]
# emails = {user["email"] for user in users}

# print(emails)

# 2. Higher order functions
# function -> paramters and arguments

# filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# def odd_filter(x):
#     # if x%2 == 1:
#     #     return True
#     # else:
#     #     return False
#     return x%2 == 1 # 1%2 == 1 => 1 == 1 => True

# print(odd_filter(1))
# print(odd_filter(2))

# odd_numbers = filter(odd_filter, numbers)

# print(odd_numbers)

# odd_numbers_list = list(odd_numbers)

# print(odd_numbers_list)

# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))


# users = [
#     {
#         "name": "Ram", 
#         "email": "ram@gmail.com"
#     },
#     {
#         "name": "hari", 
#         "email": "hari@gmail.com"
#     },
#     {
#         "name": "geeta", 
#         "email": "geeta@gmail.com"
#     },
#     {
#         "name": "saugat", 
#         "email": "saugat@gmail.com"
#     },
#     {
#         "name": "Roshan", 
#         "email": "ram@gmail.com"
#     }
# ]

# def get_email(user):
#     return user["email"]

# emails = map(get_email, users)

# print(set(emails))


# sorted

# numbers = [3, 5, 1, 0, 10]

# numbers.sort()

# print(numbers)

# students = [
#     {
#         "name": "ram", 
#         "total_marks": 345
#     },
#     {
#         "name": "roshan",
#         "total_marks": 500,
#     },
#     {
#         "name": "harry",
#         "total_marks": 150,
#     }
# ]

# def get_total_marks(student):
#     return student["total_marks"]

# print(get_total_marks({
#         "name": "harry",
#         "total_marks": 150,
#     }))

# ranked_list = sorted(students, key=get_total_marks, reverse=True)

# print(ranked_list)

# lambda function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# odd_numbers = filter(lambda x:x%2 == 1, numbers)

# print(list(odd_numbers))