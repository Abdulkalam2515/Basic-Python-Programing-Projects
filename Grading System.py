num1=int(input("Enter Marks"))
if(num1>=75 and num1<=100):
    print("it is A Grade")
elif(num1>=60 and num1<=74):
    print("it is B Grade")
elif(num1>=40 and num1<=59):
    print("it is C Grade")
elif(num1>=0 and num1<=39):
    print("it is Fail")
else:
    print("Enter proper input")