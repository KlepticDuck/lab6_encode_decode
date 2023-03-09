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


def main():
    printMenu()
    option = 0
    while option != '3':
        option = input("Please enter an option: ")
        if option == "1":
            password = encode()
        elif option == "2":
            pass


if __name__ == '__main__':
    main()
