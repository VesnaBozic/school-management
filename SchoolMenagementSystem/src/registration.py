import json
import csv



def register():
    print("*************************REGISTRATION*********************") #registration menu
    print("Please, choose who do you want to register: ")
    print("----------------------------------------------------------")
    print("1. Professor")
    print("2. Student")
    print("3. Return to Main Menu")
    print("----------------------------------------------------------")

    while True: #we are using while loop in case if entry is wrong to be able to choose again and it will repeat until we choose one of 3 options
        try:
            select = int(input("Choose 1 , 2 or 3: "))
            if select == 1: #registration for new teachers 

                professors_csv = open("data/professors.csv",
                                     "r", encoding="utf-8")

                teachers = [] 
                for row in csv.reader(professors_csv, delimiter=';'):
                    if row != []:
                        teachers.append({
                            "code": row[0],
                            "password": row[1],
                            "name": row[2],
                            "surname": row[3],
                            "email": row[4],
                            "consultation": row[5]

                        })
                


                print("-------------------------------------------------------------")
                code = int(input("Please, enter your code: "))
                exists = False
                for t in teachers: #after new teacher input code we are checking does entered code exist in teachers list
                    if int(t["code"]) == code: #if exist, we ask him to try new code
                        print("-------------------------------------------------------------")
                        print("Code already exists. Try again.") 
                        exists = True
                        break
                if not exists: #if code doesn't exist we procced with entering other data
                    print("-------------------------------------------------------------")
                    password = input("Please, enter your password: ")
                    name = input("Please, enter your name: ")
                    surname = input("Please, enter your surname: ")
                    email = input("Please enter your email: ")
                    consultation = input(
                        "Please, enter your consultation time: ")
                    fields = [code, password, name,surname, email, consultation] #list with new teacher data

                    with open(r'data/professors.csv', 'a', newline='', encoding="utf-8") as f: #we are writing new teacher data into csv professors file
                        writer = csv.writer(f, delimiter=";")
                        writer.writerow(fields)
                        return

            elif select == 2: #registration for new students
                students = json.loads(open('data/students.json', encoding="UTF-8").read()) #we are reading direct from json students file
                print("-------------------------------------------------------------")
                student_card = int(input("Please, enter your student card number: "))
                exists = False
                for s in students: #checking if student card number already exists
                    if s["student_card_number"] == student_card: 
                        print("-------------------------------------------------------------")
                        print("Card number already exists. Try again.")
                        exists = True
                        break
                if not exists: #if doesn't exist ask for student data
                    print("-------------------------------------------------------------")
                    student_password = input("Please, enter your password: ")
                    student_name = input("Please, enter your name: ")
                    student_surname = input("Please, enter your surname: ")
                    student_email = input("Please, enter your email: ")
                    student = {
                        "student_card_number": student_card,
                        "password": student_password,
                        "name": student_name,
                        "surname": student_surname,
                        "email": student_email,
                        "grades": []
                    }
                    students = [] #creating students list
                    with open(r'data/students.json', 'r', newline='', encoding="utf-8") as f:
                        students = json.load(f) #this returns json object
                    students.append(student) #we append new student in students object
                    with open(r'data/students.json', 'w', newline='', encoding="utf-8") as f: 
                        json.dump(students, f) #and we are dumping students file as a string in json file
                        return
            elif select == 3:
                return    
                    
            else:
                print("-------------------------------------------------------------")
                print("Wrong entry. Please, try again.")

        except ValueError:
            print("-------------------------------------------------------------")
            print("Wrong entry. Please try again.")
    register()
