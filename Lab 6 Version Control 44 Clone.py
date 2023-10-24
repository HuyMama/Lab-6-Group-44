# Huy Ma

# Encoding password function
def encoder(password):
    if len(password) != 8:
        return "Password must be 8 digits long"

    encoded_password = ""
    for digit in password:
        if digit.isdigit():
            shifted_digit = (int(digit) + 3) % 10
            encoded_password += str(shifted_digit)
        else:
            return "Password must only contain integers"

    return encoded_password


# decoder function
def decoder(password):
    result = ''

    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result


def main():
    # Defines necessary variables
    password = ""
    encoded_password = ""
    in_program = True

    while in_program:

        # Prints the menu
        print("Welcome to Password Encoder/Decoder Program!\n1. Encode Password\n2. Decode Password\n3. Quit Program")

        # Stores user option input
        user_input = int(input("Please Enter an Option: "))

        # Asks for a password to encode and encodes it
        if user_input == 1:
            password = input("Write the password you want to encode: ")
            encoded_password = encoder(password)
            print(f"Password encoded! Your encoded password is {encoded_password}")
            continue

        # Decodes the encoded password if there is one
        if user_input == 2:
            if password == "":
                print("Please choose option 1 and encode a password first!")
            else:
                decoded_password = decoder(encoded_password)
                print(f"Your encoded password is {encoded_password} and your decoded password is {decoded_password}")
            continue

        # Quits the Program
        if user_input == 3:
            in_program = False
            print("Thank you for using the Password Encoder/Decoder Program!")
            continue

        # For if there is an invalid input
        else:
            print("Invalid Selection")
            print()
            continue


if __name__ == "__main__":
    main()
