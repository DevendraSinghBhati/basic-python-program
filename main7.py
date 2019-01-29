#while loops

print("Enter a number")
number=int(input())

while(number>5):
    print("Number is greater then 5")
    number=int(input())
    if(number==11):
        break
    if number ==8:
        continue
    print("loop ended")