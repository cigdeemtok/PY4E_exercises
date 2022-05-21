name = input("Enter file:")
#enter a basarak direkt varsayilan dosyayi acabilirsin
#baska dosya adi girersen de onu acar
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
pn=list()
people=dict()
for line in handle:
    if not line.startswith("From"):
        continue
    words=line.split()
    pn.append(words[1])
for word in pn:
    people[word] = people.get(word,0) + 1
bigcount = None
bigword = None
for k,v in people.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword,bigcount)
