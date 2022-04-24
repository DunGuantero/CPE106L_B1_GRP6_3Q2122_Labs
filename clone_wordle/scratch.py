with open('targets.txt') as f:
    lines = [x.upper() for x in f.readlines()]
    

for i in range(len(lines)):
    c = ","
    index = lines[i].find(c)+1
    lines[i] = lines[i][index:]
textfile = open("targets.txt", "w")

for element in lines:

    textfile.write(element)

textfile.close()
print("")