                                                     #Task1: CALCULATOR FOR CODSOFT INTERNSHIP                                
print("WELCOME BACK!")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=input("Please press:  '+' or '-' or '*' or '/' or '^' or 'EXIT'")
if c =='+':
    print("Result: ",a+b)
elif c =='-':
    print("Result: ",a-b)
elif c =='*':
    print("Result: ",a*b)
elif c =='/':
    if b==0:
        print("Result: Infinity")
    else:
        print("Result: ",a/b)
elif c =='^':
    print("Result: ",a**b)
elif c =='EXIT':
    print("Bye! Have a good day.")
else:
    print("Please press valid key!")


