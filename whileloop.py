a = int(input ("how many candidates-"))

for x in range(a):

    b = input ("username-").title()
    c = int(input ("weight-"))

    if c < 85 and c > 46 :
        print ( b,"you are pass\n")
    else :
        print (b, "you are fail\n" )
print ("program close")
