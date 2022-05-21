fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File does not exist")
    quit()
myList = list()
for line in fh:
    words=line.split()
    for i in range(len(words)):
        if words[i] in myList:
            continue
        myList.append(words[i])
myList.sort()
print(myList)
