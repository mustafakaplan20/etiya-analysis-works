#self = this other languages
#In each class every function reserved with self inside, reserved parameter
#İllada self yazmana gerek yok, humanobj bile yazsan olur ama communtiy

class Human:
    name="Mustafa"
    #built-in, constructor alanı
    def __init__(self,name):
        self.name=name
        print("Bir human instance üretildi")
    def talk(self,sentence):
        print(f"{self.name} Talk {sentence}")
        #self.walk()
    def walk(self):
        print("Walk")
        #dönüş tipi str onu söylüyor(toString gibi)
    def __str__(self) -> str:
        return f"STR function result {self.name}"

#create instance
human1= Human("Ali")
human1.talk("loudly")
human1.walk()

human2=Human("Abbas")

human2.name="Veli"
human2.talk("hello")
human2.walk()

print(human2)

Human("Kaplan").talk("Miyav")