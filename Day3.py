# num1=input("Enter a number")
# num2 = input("Enter a number")
# result=num1+num2
# print(result)
# #Output value 
# # Enter a number788
# # Enter a number877
# # 788877

# num1=int(input("Enter a number"))
# num2 = int(input("Enter a number"))
# result=num1+num2
# print(result)
# output
# Enter a number788
# Enter a number877
# 1665

marks = int(input("Enter the marks obtained:"))
if marks > 100 or marks < 0:   #logical or operator use gareyxam yeha
    print("Invalid marks, marks must be between 0-100 range.You entered", marks)
elif marks >= 90:
    print("GradeA")
elif marks>=85:
    print("Grade A-")
elif marks>=85:
    print("Grade B+")
else:
    print("Failed")