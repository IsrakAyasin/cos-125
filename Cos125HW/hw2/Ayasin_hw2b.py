# Collaboration:
# I didn't collaborate with anyone

def grading():
    print("Hello, I will calculate your grade.")
    homework_weight=float(input("What is the homework weight? "))
    homework_grade=float(input("What is your homework grade?"))
    project_weight=float(input("What is the Project weight? "))
    project_grade=float(input("What is your Project grade?"))
    lab_weight=float(input("What is the Lab weight? "))
    lab_grade=float(input("What is your Lab grade?"))
    engagement_weight=float(input("What is the Engagement Opportunities weight? "))
    engagement_grade=float(input("What is your Engagement Opportunities grade?"))
    hourly_weight=float(input("What is the Hourly Exam weight? "))
    hourly_grade=float(input("What is your Hourly Exam grade?"))
    final_weight=float(input("What is the Final Exam weight? "))
    final_grade=float(input("What is your Final Exam grade?"))

    total=homework_weight*homework_grade+ project_grade*project_weight+lab_grade*lab_weight+engagement_grade*engagement_weight+hourly_grade*hourly_weight+final_weight*final_grade

    print("Your grade is "+str(total))

grading()