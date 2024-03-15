filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in (filenames):
    file = open(f"../files/{filename}", 'r')
    content = file.read()
    print(content)