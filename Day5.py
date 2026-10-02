#Data structures
#1.List -already covered in day4.py
#2.Tuple
#Tuple is similar to list but it is immutable.It means we cannot change the values of tuple once it is created.

# participants = ("rohit","gill","virat","ruturaj")
# print(participants)
# # output will be - ('rohit', 'gill', 'virat', 'ruturaj')

# ORDER_STATUS_CHOICES = (
#     "received",
#     "packed",
#     "in-transit",
#     "reached-destination",
#     "delivered"
# )
# # ouput will be - ('rohit', 'gill', 'virat', 'ruturaj')

#3. Set
#Yad gara tw hamley kun kun bracket use gareym [] -list, () - tuple 
# aba baki kun cha? yo {} matra xa yo aba set ko lagi use garxau 
# set doesnot allow duplicate values 

# ram_hobbies = {"reading","cricket","football","swimming", "coding"}
# print(ram_hobbies)
# # output will be - {'coding', 'cricket', 'reading', 'swimming', 'football'}
# # yesma order follow gardaina jun order ma aauna ni sakxa k ouput tei vara no indexing availabe
# # yedi manau football duita xa set vitra vaney output ma euta matra aauxa because set doesnot allow duplicate values.

# ram_hobbies = {"football","reading","football","cricket","football","swimming", "coding"}
# print(ram_hobbies)
# # output will be - {'cricket', 'coding', 'reading', 'swimming', 'football'}

ram_hobbies = {"reading","cricket","football","swimming", "coding"}
hari_hobbies = {"football","fishing", "coding", "dancing", "singing"}

# #Aba herau 
# #a.Intesection
#  (R n H) ram rw hari ko hobbies ko 
# common_hobbies =ram_hobbies.intersection(hari_hobbies)
# print(common_hobbies)
# #O/P- {'football', 'coding'} 
#Intesection lai & ley represent garna ni sakinxa

#b.Union 
# (R U H) ram rw hari ko hobbies ko union
# all_hobbies = ram_hobbies.union(hari_hobbies)
# print(all_hobbies)
#Output will be -{'fishing', 'dancing', 'reading', 'singing', 'cricket', 'coding', 'football', 'swimming'}
#Union lai | yo symbol ley represent garna ni sakinxa

# #c.Difference 
# ram_hobbies_only = ram_hobbies.difference(hari_hobbies)
# print(ram_hobbies_only)
# #Output will be {'cricket', 'swimming', 'reading'}
# #Difference lai minus symbol ley ni represent garna sakinx - . Difference vanya euta ma matra bhako set ho similar to mathematics
# hari_hobbies_only = hari_hobbies.difference(ram_hobbies)
# print(hari_hobbies_only)
# # output will be - {'dancing', 'fishing', 'singing'}

#4.