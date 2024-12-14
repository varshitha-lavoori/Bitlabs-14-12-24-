def total_avg():
    std_num=int(input("Enter the student number:"))
    std_name=input("Enter the student name:")
    marks1=int(input("Enter the marks secured in C language:"))
    mark2=int(input("Enter the marks secured in C++ language:"))
    marks3=int(input("Enter the marks secured in Java language:"))
    total=(marks1+mark2+marks3)
    print("total marks secured in the subjects are:",total)
    avg=int(total)/3
    print("The average marks received by student is:",avg)
    result=avg
    if result<70:
        print("The student result is: Failed")
    else:
        print("The student result is: Passed")
    grades=avg
    if grades<=100 and grades>91:
        print("The grade received is: A+ ")
    elif grades<=90 and grades>81:
        print("The grade received is: A")
    elif grades<=80 and grades>=71:
        print("The grade received is: B+")
    elif grades==70:
        print("The grade received is: B")
    else:
        print("The grade is F(failed)")
total_avg()
