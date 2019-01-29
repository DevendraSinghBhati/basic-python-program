#if else statements
print("Enter Your Marks")
number =int(input())
print(number)
if(number>90):
    grade='A'

elif(number>80):
    grade='B'

elif(number>70):
    grade='C'

else:
    grade='Dont know'

print("This grade is",grade)
