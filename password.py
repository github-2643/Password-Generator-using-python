import random
print("\t**********PASSWORD GENERATOR**********\t")
print("\t___________________________________________\t\n")
name: str=input("Enter your Name:") #user name
chars = 'abcdefghijklmnopqrstuvwxyz@#$&' #small letter and special symbol
chars1: str ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'#capital letter and numeric value
lenght =input ('how many password u have to generate\t') #number of password generate
lenght =int(lenght)
lenght1 =input('Enter your password lenght\t')
lenght1 =int(lenght1)
for p in range(lenght):
    password =''
    for c in range(lenght1):
        password +=random.choice(chars+chars1)
    print(password)
print('__________________________________')
print('Thank you see u Mr.' + name)
print('__________________________________')
