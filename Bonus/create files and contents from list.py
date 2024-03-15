contents = ["learn python withing 60 days and create a new application",
            "build a new application with python",
            "try to sell the item and generate some money for the company"]

filenames = ['learnpython.txt', 'buildapp.txt', 'sellapp.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)