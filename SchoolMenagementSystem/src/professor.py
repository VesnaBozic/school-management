import json 
import csv


professors_csv = open("data/professors.csv", "r", encoding="utf-8")
teachers = []  

for row in csv.reader(professors_csv, delimiter=';'):
    if row != []:
        teachers.append({
            "code": int(row[0]),
            "password": row[1],
            "name": row[2],
            "surname": row[3],
            "email": row[4],
            "consultation": row[5]

        })




subjects_csv = open("data/subjects.csv", "r", encoding="utf-8")
next(csv.reader(subjects_csv, delimiter=','))
subjects = []  
for row in csv.reader(subjects_csv, delimiter=','):
    if row != []: 
        subjects.append({
            "code": int(row[0]),
            "name": row[1]
        })


def add_grade(teacher): #function with argument, parametar will be  teacher who is logged 
  
    print("-------------------------------------------------------------")
    
    student_name = input("Please, enter student name: ") #we are asking from professor to input student name
    print("-------------------------------------------------------------")
    with open("data/students.json") as json_file:
        students=json.load(json_file)
    exist = False
    counter=0
    for i in range(len(students)): #with for loop going through all students
        if student_name.lower() in students[i]["name"].lower(): # if entered just one letter we list all students with that letter in name
            counter +=1
            print(str(counter)+".", students[i]["student_card_number"],
                  students[i]["name"], students[i]["surname"])
            exist = True
    if not exist:
        print("-------------------------------------------------------------")
        print("Students with this name does not exist.")
        return
    try:
        print("-------------------------------------------------------------")
        
        index_number = int(input("Please, enter student card number: ")) 
        print("-------------------------------------------------------------")
        for student in students:
            if student["student_card_number"] == index_number:
                counter = 0
                print("Here is the list of all subjects: ")
                print("")
                for subject in subjects: #we are printing all subjects
                    counter += 1
                    print(str(counter)+".", subject["code"], subject["name"])
                print("-------------------------------------------------------------")
                sub_code = int(input("Please, enter subject code: "))
                condition = True
                for s in subjects:
                    if int(s["code"])==sub_code:
                        print("-------------------------------------------------------------")
                        grade = int(input("Please, enter student's grade: "))
                        if grade < 5 or grade > 10: #setting that professor can only enter valid grade
                            print("-------------------------------------------------------------")
                            print("Wrong entry!")
                        else:
                            for s in students:
                                if s["student_card_number"] == index_number: #appeding subject code that teacher entered, logged teacher's code and grade
                                    s["grades"].append(
                                        {"subject_code": sub_code, "professor_code": int(teacher["code"]), "grade": grade})
                            with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f:
                                json.dump(students, f)
                            print("-------------------------------------------------------------")
                            print("You added grade.")
                        condition = False
                if condition:            
                    for s in subjects:
                        if s["code"] != sub_code:
                            print("-------------------------------------------------------------")
                            print("That subject code doesn't exist.")
                            break
            

                    

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")


def delete_grade(teacher):
    with open("data/students.json") as json_file:
        students=json.load(json_file)
    print("-------------------------------------------------------------")
    student_name = input("Please, enter student name: ")
    exist = False
    print("-------------------------------------------------------------")
    counter=0
    for i in range(len(students)):
        if student_name.lower() in students[i]["name"].lower(): #with lower() it doesn't matter if capital or small letter is entered
            counter+=1
            print(str(counter)+".", students[i]["student_card_number"],students[i]["name"], students[i]["surname"])
            exist = True
    if not exist:
        print("-------------------------------------------------------------") 
        print("This students do not exist.")
        return
    try:
        print("-------------------------------------------------------------")
        index_number = int(input("Please, enter student card number: "))
        print("-------------------------------------------------------------")
        for student in students:
            if student["student_card_number"] == index_number:
                counter = 0
                grades_indices = [] #here we will store indices of grades so that we can find right index of grade that professor want to delete
                original_index = -1 #we are setting it on -1, because we need to go from index 0 
                for g in student["grades"]:
                    original_index+=1
                    if g["professor_code"]==int(teacher["code"]):
                        counter+=1
                        print("-------------------------------------------------------------")
                        print(str(counter)+".", g["subject_code"], g["grade"])
                        grades_indices.append(original_index) #here we are appending original indices of professors subjects in the list 
                        
                if len(grades_indices)>0:
                    try:
                        print("-------------------------------------------------------------")
                        number = int(input("Please enter number of grade: "))
                        if number < 1 and number > len(student["grades"]):
                            print("-------------------------------------------------------------")
                            print("Wrong entry. Please, try again.")
                        else:
                            student["grades"].pop(grades_indices[number-1]) # pop() in-built function that removes item, we are using original index that we stored in list
                            with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f:
                                json.dump(students, f)
                            print("-------------------------------------------------------------")
                            print("You deleted grade.")
                            
                    except ValueError:
                        print("-------------------------------------------------------------")
                        print("Wrong entry. Please, try again.")
                else:
                    print("-------------------------------------------------------------")
                    print("This student doesn't have your grade.")
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")

def average_grade(teacher):
    counter = 0
    print("-------------------------------------------------------------")
    print("Here is the list of all the subjects.")
    for subject in subjects:
        counter += 1
        print(str(counter)+".", subject["code"], subject["name"])
    try:
        number = int(input("Please, enter number of subject: "))
        if number < 1 or number > len(subjects):
            print("-------------------------------------------------------------")
            print("Wrong entry. Please, try again.")
        else:
            grades = []
            with open("data/students.json") as json_file:students=json.load(json_file)
            for s in students:
                for g in s["grades"]:
                    if g["subject_code"] == int(subjects[number-1]["code"]) and g["professor_code"] == int(teacher["code"]):
                        grades.append(g["grade"])
            print("-------------------------------------------------------------")
            print("Average grade of your subject is: " + "{:.2f}".format(sum(grades)/len(grades)))
    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please, try again.")
    except ZeroDivisionError:
        print("-------------------------------------------------------------")
        print("None of the students has your grade or you entered wrong subject code.")


def consultation(teacher):
    professors_csv = open("data/professors.csv", "r", encoding="utf-8")
    teachers = []  

    for row in csv.reader(professors_csv, delimiter=';'):
        if row != []:
            teachers.append({
            "code": int(row[0]),
            "password": row[1],
            "name": row[2],
            "surname": row[3],
            "email": row[4],
            "consultation": row[5]

        })
    print("-------------------------------------------------------------")
    print("Your current time of consultation is: " + teacher["consultation"])
    print("-------------------------------------------------------------")
    new_consultation = input("Enter new consultation time: ")
    print("-------------------------------------------------------------")
    
    if new_consultation.strip() != "": #strip method removes spaces, so if professor just hit enter we don't change nothing
        teacher["consultation"] = new_consultation  # memory of computer
        for t in teachers:
            if t["code"] == int(teacher["code"]):
                t["consultation"] = new_consultation  # memory of file
        with open(r'data/professors.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
        for t in teachers:
            with open(r'data/professors.csv', 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(t.values())
    print("You succesfully changed your consultation date.")


def prof(teacher):
    print("-------------------------------------------------------------")
    print("Please, choose what you want to do: ")
    print("-------------------------------------------------------------")
    print("1. Add Student grade.")
    print("2. Delete Student grade.")
    print("3. Calculating the average grade for a subject.")
    print("4. Change of consultation date.")
    print("5. Return to Main Menu.")
    print("-------------------------------------------------------------")

    try:  # with try and except we are avoiding breaking of program if wrong value is entered
        print("-------------------------------------------------------------")
        option = int(input("Choose your option: "))
        print("-------------------------------------------------------------")
        if option == 1:
            add_grade(teacher)
            prof(teacher)

        elif option == 2:
            delete_grade(teacher)
            prof(teacher)

        elif option == 3:
            average_grade(teacher)
            prof(teacher)

        elif option == 4:
            consultation(teacher)
            prof(teacher)

        elif option == 5:
            return

        else:
            print("-------------------------------------------------------------")
            print("Wrong enter! Please, try again!")
            prof(teacher)

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong enter! Please, try again!")
        prof(teacher)
