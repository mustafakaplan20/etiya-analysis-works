from student import Student
from teacher import Teacher

teacherList = []
studentList = []

def addStudent(student):
    studentList.append(student)

def addTeacher(teacher):
    teacherList.append(teacher)

def showTeacherList():
    print("\n-----Teacher(s) List-----")
    if (len(teacherList) == 0):
        print("There is no teacher!\n")
    else:
        for index, teacher in enumerate(teacherList, start=1):
            print(f"{index}-> {teacher} ")
    print("\n")

    #It is also solution moreover we can use __str__ function

def showStudentList():
    print("\n-----Student(s) List-----")
    if (len(studentList) == 0):
        print("There is no student!\n")
    else:
        for index, student in enumerate(studentList, start=1):
            print(f"{index}-> {Student.showInfo(student)} ")
    print("\n")

    # print(f"Öğrenciler  : {studentList}") It is also solution moreover we can use __str__ function

def staticOperation():
    teacher_1 = Teacher("Ali", "VELI", "CSE")
    teacher_2 = Teacher("Ayse", "FATMA", "EE")

    student_1 = Student("Mustafa", "KAPLAN", "CSE-001")
    student_2 = Student("Deniz", "GUNES", "EE-001")

    addTeacher(teacher_1)
    addTeacher(teacher_2)

    addStudent(student_1)
    addStudent(student_2)

    showTeacherList()
    showStudentList()

def dynamicOperation():
    while True:

        option = input(
            "Press '1' for Showing Teachers' List\n"
            "Press '2' for Showing Students' List\n"
            "Press '3' for Adding a Teacher\n"
            "Press '4' for Adding a Student\n"
            "Quit for 'q' \n")

        if option == "1":
            showTeacherList()
        elif option == "2":
            showStudentList()
        elif option == "3":
            name = input("What's the name of teacher? :")
            surname = input("What's the surname of teacher? :")
            department = input("Which department of teacher? :")
            teacher = Teacher(name, surname, department)
            addTeacher(teacher)
        elif option == "4":
            name = input("What's the name of student? :")
            surname = input("What's the surname of student? :")
            student_id = input("What's the ID of student? :")
            student = Student(name, surname, student_id)
            addStudent(student)
        elif option == "q":
            print(
                "-----------------------\n"
                "Operation Terminated!\n"
                "-----------------------")
            break
        else:
            print("Incorrect Option Selected, Please Try Again!")


dynamicOperation()
