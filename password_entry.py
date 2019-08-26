"""Adrian"""
min_length = 6
password = input("Enter a password that is {} characters long".format(min_length))
while len(password)< min_length:
    password = input("Enter a password that is {} characters long".format(min_length))
print('*' * len(password))
