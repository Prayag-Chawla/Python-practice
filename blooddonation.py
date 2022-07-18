age = int(input('Enter age: '))
try:
    user_age = int(input("Enter your age: "))
    if user_age >= 18:
        print("You are eligible for blood donation.")
    else:
        print("You are not eligible for blood donation.")
        
except:
    print("Enter valid age.")
    
finally:
    print("Thank You")
