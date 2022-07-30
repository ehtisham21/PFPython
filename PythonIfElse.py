print("======================Login Page======================")

user_name=input("Enter Username")

if user_name=="admin":
    password = input("Enter Password")

    if password=="admin123":
        print("User Logged in")
        total_marks=int(input("Enter your Total Marks"))
        obt_marks=int(input("Enter your Obtained Marks"))
        if ((obt_marks*100)/total_marks)>=70:
            print("Total Percentage is", ((obt_marks*100)/total_marks))
            print("Excellent")
        elif ((obt_marks*100)/total_marks)>=60:
            print("Total Percentage is", ((obt_marks * 100) / total_marks))
            print("Good")
        else:
            print("Bad")
    else:
        print("Please Enter Correct Password")
else:
    print("Please Enter Correct User Name")

print("======================Login Page======================")
