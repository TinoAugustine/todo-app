result = {"Length": False, "Digit": False, "Upper": False}

while True:
    password = input("Enter Password:")

    if len(password) > 8:
        result["Length"] = True

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
            break  # No need to continue checking if one digit is found
    result["Digit"] = digit

    upper = False
    for i in password:
        if i.isupper():
            upper = True
            break  # No need to continue checking if one uppercase letter is found
    result["Upper"] = upper

    print(result)

    if all(result.values()):
        print('Strong Password!')
        break
    else:
        print('Weak Password')



