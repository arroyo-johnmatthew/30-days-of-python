# --------------------------- EXERCISE 1 -----------------------------------
dog = {}
dog = {"Color": "Black", "Breed": "Poodle", "Legs": 4, "Age": 11}

student = {
    "First Name": "John Matthew", 
    "Last Name": "Arroyo", 
    "Gender": "Male", 
    "Age": 21, 
    "Marital Status": "Single", 
    "Skills": ["HTML", "CSS", "JS", "PHP", "JAVA", "PYTHON"],
    "Country": "Philippines",
    "City": "Pasay",
    "Address": {
        "street": "Grove Street",
        "zipcode": "6770"
    },
}

student["Skills"].append("GITHUB")

keys = student.keys()
values = student.values()
dict_tuple = student.items()

del student





