print("Signup")
print("*" * 8)

# User Signup
empName = input("Enter Your Name: ")
empEmail = input("Enter Your Email: ")
empPass = input("Enter Your Password: ")
empContact = input("Enter Your Contact: ")

print("Account Successfully Created")

# User Login
empEmaiLogin = input("Enter Your Login Email: ")
empPassLogin = input("Enter Your Login Password: ")

if (empEmail == empEmaiLogin) and (empPass == empPassLogin):
    print("Account Successfully Logged In")
    
    # Even or Odd Number Check
    num = int(input("Enter Your Number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
    # Leap Year Check
    year = int(input("Enter Your Year: "))
    if year % 4 == 0:
        print("Is a Leap Year")
    else:
        print("Is Not a Leap Year")
    
    # Marks Calculation
    eng = float(input("Enter Your English Marks: "))
    math = float(input("Enter Your Math Marks: "))
    urdu = float(input("Enter Your Urdu Marks: "))
    obtainedMarks = eng + math + urdu
    percentage = (obtainedMarks / 300) * 100
    
    print("Obtained Marks:", obtainedMarks)
    print("Percentage:", percentage)
    
    # Grade Evaluation
    if 100 >= percentage >= 80:
        print("Grade: A1")
    elif 79 >= percentage >= 70:
        print("Grade: A")
    elif 69 >= percentage >= 60:
        print("Grade: B")
    elif 59 >= percentage >= 50:
        print("Grade: C")
    elif 49 >= percentage >= 40:
        print("Grade: D")
    else:
        print("IU Jaien")
else:
    print("Incorrect Email Or Password")
