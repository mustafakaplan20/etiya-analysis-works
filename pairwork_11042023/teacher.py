class Teacher:
    name=""
    surname=""
    department=""
    # Declaring the atributes as "None", it provides pretend to be no-args constructor
    def __init__(self,name=None,surname=None,department=None) -> None:
        self.name=name
        self.surname=surname
        self.department=department
    
    #Same as with __str__ but for practice
    def showInfo(self):
        print("Inside the showInfo function!")
        return f"Name: {self.name}, Surname: {self.surname}, Department: {self.department}" 
    
    def __str__(self) -> str:
        print("Inside the built-in function!")
        return f"Name: {self.name}, Surname: {self.surname}, Department: {self.department}"