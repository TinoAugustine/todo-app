
member = input("Add a new member:")
file = open(f"../files/members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open(f"../files/members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()