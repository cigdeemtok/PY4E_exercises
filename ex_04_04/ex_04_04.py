di = dict()
lst = list()
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    pos = words[5].find(':')
    hour = words[5][ : pos]
    if hour not in di:
        di[hour] = 1
    else:
        di[hour] += 1

for key, val in list(di.items()):
    lst.append((key, val))

lst.sort()                            

for key, val in lst:
    print(key, val)
