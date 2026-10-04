# #Functions

# def send_email():    #Function definition
#     print("Finding user from the db")
#     print("check if the user email id is valid")
#     print("Prepare mail message")
#     print("Mail sent")

# send_email()           #function call 
# #ouput will be 
# # Finding user from the db
# # check if the user email id is valid
# # Prepare mail message
# # Mail sent

# def send_email():
#     print("Sending email to ram,status:'order placed'")

# send_email()
# #Aba in real life hamley ram lai matra pathaune tw haina so we take input from user 
# #rw tesko lagi hami aba parameters and arguments ko use garxau

# def send_email(name):
#     print(f"sending email to {name} ")

# user_input=input("Enter the name to whom the email is to be send: ")
# send_email(user_input)

#Aba sidhai function call garda arguments diyera heram

# def send_email(name):
#     print(f"Sending emails to {name}, status:'order placed'")

# send_email("Hari")

#Hari- arguments  (yo real value ho)
#name - parameter   (yo chai variable jasto jasley tyo real value store garxa vanam matlab hari chai name vitra janxa ani name call garda name = hari hunxa )

# def send_email(name, order_status):
#     print(f"Sending emails to {name}, status: '{order_status}'")

# send_email("Hari", "in-transit")
#output will be -Sending emails to Hari, status: 'in-transit'
#aba yesari argument dida kunai kunai bela mix max hunxa sakxa aba testo belama ouput useless aaux like herau 


# def send_email(name, order_status):
#     print(f"Sending emails to {name}, status: '{order_status}'")

# send_email("in-transit", "hari")
# #output will be -Sending emails to in-transit, status: 'hari'

#So aba hami function call garda argument sang sangai kun thauma yah kun parameter ma kun arguments dini ho vanera pani vanidinxau
#Yesley garda code understanding ni clear hunxa no mix max 

# def send_email(name, order_status):
#     print(f"Sending emails to {name}, status: '{order_status}'")

# send_email(name="Hari", order_status="in-transit")
# #output will be -Sending emails to Hari, status: 'in-transit'

# def send_email(name, order_status, greeting):
#     print(f"{greeting}, Mr. {name}")
#     print(f"Your order status: '{order_status}'")

# send_email(name="Sachin", order_status="packed", greeting="Goodmorning")

#Output will be - 
# Goodmorning, Mr. Sachin
# Your order status: 'packed'



#aba hami parameter ma default value halera herxau
# def send_email(name, order_status, greeting="Hello"):
#     print(f"{greeting}, Mr. {name}")
#     print(f"Your order status: '{order_status}'")

# send_email(name="Sachin", order_status="delivered")
#output will be -
# Hello, Mr. Sachin
# Your order status: 'delivered'


# Yedi parameter ma default value ni xa rw call garda ni arguments value pass gareyxa vaney 
# tei argument use hunxa ,default vanya arguments nadida kei nahuda use garney ho

# def send_email(name, order_status, greeting="Hello"):
#     print(f"{greeting}, Mr. {name}")
#     print(f"Your order status: '{order_status}'")

# send_email(name="Sachin", order_status="delivered", greeting="Goodmorning")
# output will be -
#  Goodmorning, Mr. Sachin
# Your order status: 'delivered'

#yedi parameter declare gareyxam rw teslai default value ni nadida rw arguments pani pass nagarada 
#error aauxa
# def send_email(name, order_status, greeting):
#     print(f"{greeting}, Mr. {name}")
#     print(f"Your order status: '{order_status}'")

# send_email(name="Sachin", order_status="delivered")
#output will be -send_email(name="Sachin", order_status="delivered")  
# TypeError: send_email() missing 1 required positional argument: 'greeting'


#Aba return type herau yedi function vitra ko kei kura out of function block ma use garna xa vaney hamley return garnuparxa

# def add(a,b):
#     result= a+b;
#     print(result)

# add_result=add(5,6)
# X= add_result * 70
# print(X)
#yesso garda error aauxa kina ki hamley function call gareyni tyo vitra ko result pauna return type use garnu parxa
#ani matra tyo value add_result ma return hunxa add_result= 5+6=11 , aba vaney yo function vitra ko result ko value jata ni use garna milyo add_result use garera

# def add(a,b):
#     result= a+b;
#     print(result)
#     return result

# add_result=add(5,6)
# X= add_result * 70
# print(X)
#Output will be 11 and 770 
#Function vitra ko print(result)=11 ani function baeeera ko call garera add_result variables ma 11 rakheu 
#ani tei value lai * 70 garera X variable vitra rakheu ani print(X) garda =770 vayo.


def add_sub(a,b):
    add_result= a+b
    sub_result=a-b
    return add_result, sub_result

result= add_sub(6,7)
print(result)
#Output will be (13, -1)
#Function praye tw euta matra kura return garxa rw mathi pani reuturn tw euta matra kura vaeeraxa euta packed tuple vitra 
# 2 ta value return gareyxa tara return tw euta matra hunxa so aba teslai unpack garna parxa

add_result, sub_result = add_sub(6,7)  # yesto vaye 11 add_result vitra janxa ani -1 sub_result vitra janxa // yo unpacking gareyko ho hai
print(f"Addition: {add_result}, Subtraction: {sub_result}")
#ouput will be 
# (13, -1)
#Addition: 13, Subtraction: -1







#######
"""class notes"""
#########

# Repeated/ Reusable
# a = 10

# DRY -> Don't Repeat Yourself
# def send_mail(): # function defination
#     print("finding user from db")
#     print("check if user email is verified")
#     print("check if user email is active/online")
#     print("Prepare mail message")
#     print("Mail sending")
#     print("Mail sent")



# send_mail() # function call






# send_mail() # function call









# print("finding user from db")
# print("check if user email is verified")
# print("Prepare mail message")
# print("Mail sending")
# print("Mail sent")








# print("finding user from db")
# print("check if user email is verified")
# print("Prepare mail message")
# print("Mail sending")
# print("Mail sent")




# def send_mail(name, order_status): # function defination
#     print(f"Sending email to {name}, status '{order_status}'")



# value we pass/send to function is called as argument
# send_mail("Hari", "order placed") # function call
# send_mail("Reeta") # function call

# in above example, the arguments are based on position, therefore these type of arguments are called as positional arguments

# send_mail("Hari", "in-transit") # function call
# send_mail("in-transit", "Hari") # function call

#
# send_mail(order_status="in-transit", name="Hari") # function call
# in above example, the arguments are based on parameter name, therefore these type of arguments are called as keyword arguments



# greeting="Hello", here it is called as default argument
# def send_mail(name, order_status, greeting="Hello"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
    

# send_mail(
#     name="Hari",
#     order_status="delivered",
#     # greeting="Good morning"
#     )


# def send_mail(name, order_status, greeting="Hello"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
#     return "Your task has started"

    

# response = send_mail(
#         name="Hari",
#         order_status="delivered",
#         greeting="Good morning"
#     )

# print("Response:", response)

# def add(a, b):
#     result = a+b
#     # print(result)
#     return result
#     # return None
    
# add_result = add(5,60)

# x = add_result * 70
# print(x)


# def add_sub(a,b):
#     a_result = a+b
#     s_result = a-b
#     m_result = a*b
    
#     return a_result, s_result, m_result


# result = add_sub(5,6)
# a, s, m = add_sub(5,6)

# a, s = (11, -1)
# a, s, m = result

# print(result)


# def send_mail(name, order_status, greeting="Hello", a = "1", b="5"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
#     return "Your task has started"


# send_mail(
#     "hari",
#     "placed",
#     greeting="Good moring",
#     b="6"
# )