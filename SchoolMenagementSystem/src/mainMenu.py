from registration import register
#with next function we print to user main menu options
import json  # import of json built-in package so that we can work with JSON data
from student import*  # import of everything from the student module
import csv  # import of csv file so that we can work with such CSV data
from professor import prof  # import of function prof() from professor module


def menu():
    print("*******************************MAIN MENU*********************************")
    print("Please, choose option: ")
    print("-------------------------------------------------------------------------")
    print("1. Log into the system")
    print("2. Registration")
    print("3. Leave the aplication")
    print("-------------------------------------------------------------------------")


    try: #with try and except we are avoiding breaking of program if wrong value is entered
        print("")
        option = int(input("Choose your option: "))
        if option == 1 :
            log()
            menu()
            
        elif option == 2 :
            register()
            menu()
        
        elif option == 3 :
            print("-------------------------------------------------------------")
            print("You left the aplication.")
            exit() #exiting program
        
        else:
            print("-------------------------------------------------------------")
            print("Wrong enter! Please, try again.")
            menu()
    
    except ValueError: #with this exeption we are preventing program from breaking if string is entered
        print("-------------------------------------------------------------")
        print("Wrong enter. Please, try again.")
        menu() 
def log():
# open() function returns a file objects, then we pass it to the reader
    professors_csv = open("data/professors.csv", "r", encoding="utf-8")
    teachers = []  # we are making new list to read csv data in to it
# we iterate over lines in professorsCSV file
    for row in csv.reader(professors_csv, delimiter=';'):
        if row != []:
            teachers.append({  # we are making key words, adding values from csv professors data in it and then appending this dict into teachers list
            "code": row[0],
            "password": row[1],
            "name": row[2],
            "surname": row[3],
            "email": row[4],
            "consultation": row[5]

        })
    with open("data/students.json") as json_file:
        students=json.load(json_file)
       
    try:
        print("-------------------------------------------------------------")
        code = int(
            input("Please, enter your professor code or student card number: "))
        print("-------------------------------------------------------------")
        password = input("Please, enter your password: ")
        # for loop we use to check does entered student card number and password match
        students = json.loads(open('data/students.json', encoding="UTF-8").read()) 
        for i in range(len(students)):
            if students[i]["student_card_number"] == code and students[i]["password"] == password:
                print("-------------------------------------------------------------")
                stud(students[i])
                return

        for i in range(len(teachers)):  # professor password and code match
            if teachers[i]["code"] == str(code) and teachers[i]["password"] == password:
                print("-------------------------------------------------------------")
                prof(teachers[i])
                return

        print("-------------------------------------------------------------")
        print("Wrong password or code. Please, try again.")
        print("-------------------------------------------------------------")
        

    except ValueError:
        print("-------------------------------------------------------------")
        print("Wrong entry. Please try again.")
        menu()
menu()