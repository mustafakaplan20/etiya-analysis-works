class Student:
    name= ""
    surname=""
    student_id=""
    # Declaring the atributes as "None", it provides pretend to be no-args constructor
    def __init__(self,name=None,surname=None,student_id=None) -> None:
        self.name=name
        self.surname=surname
        self.student_id=student_id
    
    #Same as with __str__ but for practice
    def showInfo(self):
        print("Inside the showInfo function!")
        return f"Name: {self.name}, Surname: {self.surname}, Student ID: {self.student_id}"
    def __str__(self) -> str:
        print("Inside the built-in function!")
        return f"Name: {self.name}, Surname: {self.surname}, Student ID: {self.student_id}"