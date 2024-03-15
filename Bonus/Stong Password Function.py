def strength(password):
    result = {"Length": False, "Digit": False, "Upper": False}

    if len(password) > 8:
        result["Length"] = True

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
            break
    result["Digit"] = digit

    upper = False
    for i in password:
        if i.isupper():
            upper = True
            break
    result["Upper"] = upper

    return result

password = input("Enter Password:")
result = strength(password)

print(result)

if all(result.values()):
    print('Strong Password!')
else:
    print('Weak Password')
