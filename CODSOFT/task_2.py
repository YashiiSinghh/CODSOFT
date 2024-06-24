                                    #Task2: PASSWORD GENERATOR
import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "`~!@#$%^&*()_-+{}[]()\|''?.,<>/="
characters = lowercase+uppercase+numbers+symbols
length = int(input("Enter the length for your password: "))
Password = ""
for a in range(length):
    Password+=random.choice(characters)
print("Your password is: ",Password)