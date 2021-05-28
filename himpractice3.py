
# user_age = 17
def age_verifier( user_age, username ):
    if user_age >= 18:
        print(username.upper(),",Eligible for driving.")
    else:
        print(username.upper(),',Not eligible for driving.')


#age_verifier(19)  # <--- argument
