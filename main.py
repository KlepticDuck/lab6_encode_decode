'''
Author: Christian Rodriguez
Lab 6 COP3502C
'''

def printMenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def encode():
    password_to_encode = input("Please enter your password to encode: ")
    encoded_password = ""
    for ch in password_to_encode:
        if int(ch) + 3 <= 9:
            num = int(ch) + 3
        else:
            num = int(ch) + 3 - 10
        encoded_password += str(num)
    print("Your password has been encoded and stored!")
    return encoded_password

def decode(encoded_password):
    og_password = ''
    for ch in encoded_password:
        if int(ch) - 3 >= 0:
            num = int(ch) - 3
        else:
            num = int(ch) - 3 + 10
        og_password += str(num)
    return og_password


def main():
    printMenu()
    option = 0
    while option != '3':
        option = input("Please enter an option: ")
        if option == "1":
            password = encode()
            printMenu()
        elif option == "2":
            og_password = decode(password)
            print(f'The encoded password is {password}, and the original password is {og_password}')
            printMenu()


if __name__ == '__main__':
    main()
