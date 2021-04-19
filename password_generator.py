import random

print(" - cyberjj999 Password Generator - ")
number_of_password = int(input("Please enter the number of password you want to generate: "))
length_of_password = int(input("Please enter the desired length of password you want to generate: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()`,./';[]"

list_of_password = []
for password in range(number_of_password):
    password = ""
    for char in range(length_of_password):
        random_index = random.randint(0, len(characters) - 1)        
        password += characters[random_index]
    list_of_password.append(password)

print("")
print(" - Generated Password - ")
i = 1
for password in list_of_password:
    print(str(i) + ". " + password)
    i+=1