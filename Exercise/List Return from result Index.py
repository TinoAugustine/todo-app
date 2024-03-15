#Return the result from list using Index

ips = ['100.122.133.105', '100.122.133.111']

user_choice = input("Enter the Index")
user_choice = int(user_choice)
checkip = ips[user_choice]
print(f"You chose {checkip}")

