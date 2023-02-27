from pathlib import Path

myfile = open( "Myfile.txt", "a")

# myfile.write("This is just another")

data =[['Michael', 'Joshua',], ['Precious', 'Joshua']]

with open("Names.txt", "w") as file:
    for line in data:
        file.write(' '.join(line) + "\n")