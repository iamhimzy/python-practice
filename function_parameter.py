'''# default parameter value

def myFunction( myk=0 ):            # parameter
    if myk > 50:
        print('Value if greater than 50')

myFunction()  # argument - parameter's value
myFunction(100)'''

'''a=input("Please enter your gender - ").lower()

def gender_checker( gender=True ):

    if gender == "male":
        print("You are male")
    elif gender == "female":
        print("you are Female")
    else:
        print('Others')

gender_checker(a)   # gender=a
gender_checker()    # error'''


a=int(input("Enter your first name - "))
b=int(input("Enter your last name - "))\

def addition(para1,para2):
    # para1 = 10
    # para2 = 5
    print(para1+para2)

addition(10,5)
addition(a,b)
