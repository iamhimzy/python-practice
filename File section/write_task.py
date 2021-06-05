f=open("input.txt","w")
user=input("name - ")
if len(user) > 5:
    f.write("hello-_mr- " + user)

else:
    print("minimun 5 char")
f.close()
