file = open(f"../files/essay.txt", 'r')
readtext = file.read()
convert = readtext.title()

print(convert)