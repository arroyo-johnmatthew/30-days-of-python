class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        
        # self is basically the place holder for the object (variable)
        # example, student = Student(name, house)
        # "self.name = name" becomes "student.name = name"
        self.name = name

        # the house setter will also run this because it sees "self.house" and
        # "=" so no need to place the ValueError raising inside this method!
        self.house = house

    # Special method that whenever an object is only called, example:
    # "print(student)" and not "print(student.name)"
    # it will return the proper output as string
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getters
    @property
    def house(self):
        return self.house
    
    # Setters
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self.house = house

    # Basically setter will automatically run if there is a code like for example
    # student.house = "Pasay" where if Python sees the "=" it will know that it is for setter
    # situations like print(student.house) is where getter will do its job
    # TAKE NOTE def names of the getter and setter must be the same
    # that must mean the it should also be the same for the __init__ method attributes (elf.house, self.name, etc)

def main():
    student = get_student()
    student.house = "Number Four"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()