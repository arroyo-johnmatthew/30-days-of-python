class Wizard:
    def __init__(self, name):
        self.name = name

class Professor(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Student(Wizard):
   def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def main():
    student = Student("Harry", "Gryffindor")
    professor = Professor("Snape", "Defense Against the Dark Arts")

if __name__ == "__main__":
    main()