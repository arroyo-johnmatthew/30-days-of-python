class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    """ We placed the get_student func inside this class to comply to design
        principles. It uses cls (check lecture 2) so basically cls(name, house)
        is the same as Student(name, house)
    """
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
   
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()