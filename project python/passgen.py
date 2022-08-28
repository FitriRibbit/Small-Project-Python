import random

print('Welcome to Your Password Generator')

charts = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Input amount of password to generate: ')
number = int(number)

length = input('Input your password length:')
length = int(length)

print('\nhere are your password:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(charts)
    print(password)