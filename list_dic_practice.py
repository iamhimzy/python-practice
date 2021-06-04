'''
print("List")
a=[10,20,30,40,50,"hello wolrd"]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print("<---------------------------------->")

print("Dictionary")
b={1:"raj",2:"rohan",3:"atul"}
c={"sonam":100,"pinki":200,"mini":300}

print(b[1])
print(b[2])
print(b[3])

print("<----------------------------------->")

c["sonam"]=5000
c["mini"]=8000
print(c["sonam"])
print(c["pinki"])
print(c["mini"])'''
'''
print("Dictionary practice")
#dictionary is nothing but key value pairs

d1={}
d2={
    'harry':'burger',
    'titu' : 'rolls',
    'robert':'veggie',
    'allen':{"mrng":"milk","noon":"egg","night":"meal"}

}
d2 ["aki"]:"coffee"
#some operations of dictionary

print(d2.get("titu"))
d2.update({'leena':'toffee'})
print(d2.keys())
print(d2)
'''
'''
print("dictionary")

d1={
    'a':'goku',
    'b':'vegita',
    'c':'piclo',
    'car':{'ferrari':10,'maruti':1}
}
d1['plane']='jet'
d1.update({"ash":"pokemon"})
print(d1.keys())
print(d1['a'])
print(d1['ash'])
#print(d1)
'''

'''
print("<------------List----------------->")
#list=[100,200,500,7.59,"krishh"]



W=["goku","cell","majin buu","dragon ball Z"]

a="frieza","god of destruction"
W.append(a)
print(W)
print(W[4])
print(W[3])
print(W[2])
'''

'''

print("----Function----")

def my_function():
    x=10
    y=20
    c=x+y
    print(c)
my_function()

def my_function2(y):
    x=100
    c=(x+y)
    print(c)

my_function2(70)


def disp():
    name="Keep calm programmers"
    print("welcome to",name)
disp()


a=1
c=2
print(a+c)

print(a-c)
print(a*c)
print(a/c)
'''
'''
print("Return statement in function")

def add(y):
    x=20
    c=(x+y)
    return (c)
#sum=add(20)
a=add(100)
print(a)
'''

'''
def add_sum(y):
    x=10
    c=x+y
    d=x-y
    return(c,d)
w,z=add_sum(50)
print(w)
print(z)
'''


for x in ("shubhanshu"):
    print(x)
