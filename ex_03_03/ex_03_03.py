# Dosya adı olarak mbox-short.txt dosya adını kullanın

fname = "mbox-short.txt"
fh = open(fname)
sumOfNum=0
average=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
   # print(line)
    count+=1
    cpos=line.find(":")
    nline=line[cpos+2:]
    try :
        num=float(nline)
    except :
        continue
    sumOfNum=sumOfNum+num
    average=sumOfNum/count
print("Ortalama X_DSPAM_Confidence:",average)
print("Done")
