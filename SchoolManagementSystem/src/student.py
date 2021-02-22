import csv
import json



subjects_csv = open("data/subjects.csv", "r", encoding="utf-8")
next(csv.reader(subjects_csv, delimiter=','))
subjects = [] 
for row in csv.reader(subjects_csv, delimiter=','):
    if row != []:
        subjects.append({
            "code": int(row[0]),
            "name": row[1]
        })


def calculate_av_grade(student): #function with parameter, on call of te function we pass logged student as argument
    
    grades = []
    for g in student["grades"]: #going through logged student grades
        grades.append(g["grade"]) #and appending them in grades list
    if(len(grades)>0):
        print("-------------------------------------------------------------")
        print("Your average grade is: " + "{:.2f}".format(sum(grades)/len(grades))) #we sum grades and divide with lenght of grades and format a result
    else:
        print("-------------------------------------------------------------")
        print("You don't have any grades yet.")

def exams(student):
    print("-------------------------------------------------------------")
    print("1. Passed exams")
    print("2. Failed exams")
    print("-------------------------------------------------------------")
    passed_exams = []
    for g in student["grades"]: #here we append passed exams in list so that later we can use it to know which are failed exams if the first option is 2
        if g["grade"] > 5:
            for s in subjects:
                if s["code"] == g["subject_code"]:
                    passed_exams.append(s)
    try:
        print("-------------------------------------------------------------")
        exam = int(input("Choose, your option: "))
        if exam == 1:
            print("-------------------------------")
            print("You have passed next exams: ")
            print("-------------------------------")
            for g in student["grades"]:
                if g["grade"] > 5:
                    for s in subjects:
                        if s["code"] == g["subject_code"]:
                            print(s["code"], s["name"])
                            passed_exams.append(s)
            if passed_exams == []:
                print("-------------------------------------------------------------")
                print("You haven't passed any exam.")
        elif exam == 2:
            print("-------------------------------")
            print("You haven't passed next exams: ")
            print("")
            for s in subjects:
                passed=False
                for p in passed_exams:
                    if s["code"]==p["code"]:
                        passed=True
                if not passed:
                  print(s["code"], s["name"])
        else:
            print("-------------------------------------------------------------")
            print("Wrong entry.")
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry.")

def professor_data():
    professors_csv= open("data/professors.csv", "r", encoding="utf-8" ) 
    teachers = [] 
    for row in csv.reader(professors_csv, delimiter = ';'):
        if row!=[]:
            teachers.append({
            "code": row[0],
            "password": row[1],
            "name": row[2],
            "surname": row[3],
            "email":row[4],
            "consultation": row[5]

        })
    students = json.loads(open('data/students.json', encoding="UTF-8").read())
    counter = 0 
    print("-------------------------------------------------------------")
    print("Here is list of your exams: ")
    for subject in subjects: #printing subjects codes and names
        counter +=1
        print(str(counter)+".", subject["code"], subject["name"]) 
    print("-------------------------------------------------------------")
    sub_code = int(input("Please, enter subject code: "))
    print("-------------------------------------------------------------")
    for s in students: #checking are such code in students grades
        for g in s["grades"]:
            if g["subject_code"]==sub_code:
                for t in teachers: # does the subject code match with teacher code if does print code and his name
                    if int(t["code"])==g["professor_code"]:
                        print("")
                        print("-------------------------------------------------------")
                        print("Professor code is: " + t["code"])
                        print("Professor's name is: " + t["name"] +" " + t["surname"] )
                        print("Email: " + t["email"])
                        print("Consulation time is: " + t["consultation"])
                        print("")
                        return
    print("-------------------------------------------------------------")
    print("Doesn't exist.")


def stud(student):
    print("----------------------------------------------")
    print("Please, choose what you want to do: ")
    print("1. Calculating the average grade.")
    print("2. Passed exams or non-passed exams display by student's choice.")
    print("3. Professor's data display.")
    print("4. Return to Main Menu.")
    print("-------------------------------------------------------------")

    try:  # with try and except block we are catching and hendling execeptions, if string value  is entered
        option = int(input("Choose your option: "))
        if option == 1:
            print("---------------------------------------")
            calculate_av_grade(student)
            stud(student)

        elif option == 2:
            print("----------------------------------------")
            exams(student)
            stud(student)

        elif option == 3:
            professor_data()
            stud(student)

        elif option == 4:
            return

        else:
            print("-------------------------------------------------------------")
            print("Wrong enter! Please, try again!")
            stud(student)

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong enter! Please, try again!")
        stud(student)
