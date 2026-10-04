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