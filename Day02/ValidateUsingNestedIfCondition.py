Exam_Name = input("Enter the Exam Name: ")
Obtained_Marks = int(input("Enter the Obtained Marks:"))

if Obtained_Marks >= 35:
    print("Exam Name is: ", Exam_Name)
    print("Obtained Marks are: ", Obtained_Marks)
    print("Result is: Pass")

    if Obtained_Marks <=60:
        print("Grade is: Second Class")
    elif Obtained_Marks >= 90:
        print("Grade is: First Class")

else:
    print("Exam Name is: ", Exam_Name)
    print("Obtained Marks are: ", Obtained_Marks)
    print("Result is: Fail")        

