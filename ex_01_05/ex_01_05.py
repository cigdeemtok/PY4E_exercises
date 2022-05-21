score = input("Enter Score: ")

try :
    grd= float(score)
except :
    print("Error, your input is not a number ")
    quit()

if grd >0.0 and grd<1.0 :
    if grd>=0.9:
        print("Your grade is A")
    elif grd>=0.8:
        print("Your grade is B")
    elif grd>=0.7:
        print("Your grade is C")
    elif grd>=0.6:
        print("Your grade is D")
    else :
        print("Your grade is F")
else :
    print("Error, your input is out of range ")
