myfile = open("files/deneme.txt")
content = myfile.read()
print(content)
myfile.close()
myfile = open("files/deneme.txt")
content2 = myfile.read()
print(content2)
myfile.close()

with open("files/deneme.txt") as file:
    print(file.read())

with open("files/vegetables.txt", "a+") as file:
    file.write("tomato\n")
    file.seek(0)
    print(file.read())