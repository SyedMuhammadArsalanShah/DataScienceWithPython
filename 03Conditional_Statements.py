print("Signup")
print("*"*8)
empName= input("Enter Your Name \n")
empEmail= input("Enter Your Email \n")
empPass= input("Enter Your Password\n")
empContact= input("Enter Your Contact \n")



print("Account Successfully Created")


empEmaiLogin= input("Enter Your Login Email \n")
empPassLogin= input("Enter Your Login Password\n")

if(empEmail==empEmaiLogin) and (empPass==empPassLogin):
    print("Account SuccessFully Login")


    num = int(input("Enter Your Number"))
    if num%2==0:
        print("Even")
    else:
        print("odd")

    year = int(input("Enter Your Year"))
    if year%4==0:
        print("Is leap Year")
    else:
        print("is not a leap Year")

    eng= float(input("Enter Your Eng Marks "))
    math= float(input("Enter Your Math Marks "))
    urdu= float(input("Enter Your Urdu Marks "))
    obtainedMarks = eng+math+urdu
    percentage= (obtainedMarks/300)*100
    print("Obtained Marks ", obtainedMarks)
    print("Percentage ", percentage)
    if percentage<=100 and percentage>=80:
        print("grade A1")
    elif percentage<=79 and percentage>=70:
        print("grade A")
    elif percentage<=69 and percentage>=60:
        print("grade B")
    elif percentage<=59 and percentage>=50:
        print("grade C")
    elif percentage<=49 and percentage>=40:
        print("grade D")
    else:
        print("IU Jaien")


else:
    print("Incorrect Email Or Pass")