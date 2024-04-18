import json # imported for file writing and reading
from datetime import datetime # imported for time calculations

class Student:

    # constructor that initializes all the properties of a student
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.student_number = student_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.country_of_birth = country_of_birth

    # getter methods for each Student property
    def get_student_number(self):
        return self.student_number
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_sex(self):
        return self.sex
    def get_country_of_birth(self):
        return self.country_of_birth

    # setter methods for each Student property
    def set_student_number(self, student_number):
        self.student_number = student_number
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def set_sex(self, sex):
        self.sex = sex
    def set_country_of_birth(self, country_of_birth):
        self.country_of_birth = country_of_birth

# initializing an array that stores each of the Student objects
students_array = []

# function to write student data to a file
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, default=lambda obj: obj.__dict__)
        # python lambda is used to serialize our Student object with key-pair values suitable for json files

# function to read student data from a file and populate the array
def read_from_file(file_path):
    try:
        # open and read from json file
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("Loaded data from file:", data)  # debugging to see if the data loaded is what we want
            students = []
            if isinstance(data, list):  # debugging to check if the loaded data is a list
                for student_data in data:
                    if isinstance(student_data, dict):  # check if each item is a dictionary
                        # append the student array with objects possessign the Student parameters (**)
                        students.append(Student(**student_data)) 
                    else:
                        print("Invalid data format in the file.")
                        return []
            else:
                print("Invalid data format in the file.")
                return []
            
            # return the array containing student data
            return students
    # try catch error
    except FileNotFoundError:
        return []




# function to calculate age based on the date of birth
def calculate_age(date_of_birth):
    today = datetime.now() # date of TODAY
    # parses the input date of birth and converts it into a time python can read using datetime
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    # calculating the student age
    age = today.year - birth_date.year

    return age

# function to add a new student
def add_student():

    # first, check if student array is full
    if len(students_array) < 101:
        # user inputs
        student_number = int(input("Enter student number: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        sex = input("Enter sex: ")
        country_of_birth = input("Enter country of birth: ")

        new_student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        # after creating a student object with the user input, add to the array holding all students
        students_array.append(new_student)
        print("New student added successfully.")
    else:
        print("Sorry, we cant add any more students")

# function to find a student by student number
def find_student_by_number():
    student_number = int(input("Enter student number to find: "))
    
    for student in students_array:
        # if an element (each "student") in the student array possesses the stu number searched, proceed
        if student.get_student_number() == student_number:
            print(f"Student found!\n")
            print(f"Student Number: {student.get_student_number()}")
            print(f"Name: {student.get_first_name()} {student.get_last_name()}")
            print(f"Date of Birth: {student.get_date_of_birth()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of Birth: {student.get_country_of_birth()}")
            print(f"Age: {calculate_age(student.get_date_of_birth())} years")
            return
    # otherwise, print no student found
    print(f"No student found with student number {student_number}.")

# function that shows all students
def show_all_students():
    # if there is no student in the array, print no students
    if not students_array:
        print("No students in the array.")
        return

    # display every student element in the students_array
    for student in students_array:
        print(f"Student Number: {student.get_student_number()}")
        print(f"Name: {student.get_first_name()} {student.get_last_name()}")
        print(f"Date of Birth: {student.get_date_of_birth()}")
        print(f"Sex: {student.get_sex()}")
        print(f"Country of Birth: {student.get_country_of_birth()}")
        # calculate_age is a function that calculates the age of a student based on their DOB ^^
        print(f"Age: {calculate_age(student.get_date_of_birth())} years")
        print("\n")

# function that shows students born in a given year
def show_students_by_birth_year():
    birth_year = input("Enter the birth year to filter students: ")

    # filter array that obtains every student with a specific birth year, hense we use .startswith()
    filtered_students = [student for student in students_array if student.get_date_of_birth().startswith(birth_year)]
    
    # if there are no students with the birth year, print this:
    if not filtered_students:
        print(f"No students found born in the year {birth_year}.")
        return
    
    # display the filtered students data
    for student in filtered_students:
        print(f"Student Number: {student.get_student_number()}")
        print(f"Name: {student.get_first_name()} {student.get_last_name()}")
        print(f"Date of Birth: {student.get_date_of_birth()}")
        print(f"Sex: {student.get_sex()}")
        print(f"Country of Birth: {student.get_country_of_birth()}")
        # calculate_age is a function that calculates the age of a student based on their DOB ^^
        print(f"Age: {calculate_age(student.get_date_of_birth())} years")
        print("\n")

# function to modify a student record
def modify_student_record():
    student_number = int(input("Enter student number to modify: "))

    # looks for student inside the array holding students
    for student in students_array:
        if student.get_student_number() == student_number:
            field_to_modify = input("Enter the field to modify (first_name, last_name, date_of_birth, sex, country_of_birth): ")

            new_value = input(f"Enter the new value for {field_to_modify}: ")

            # Use setter methods to modify the record
            if field_to_modify == 'first_name':
                student.set_first_name(new_value)
            elif field_to_modify == 'last_name':
                student.set_last_name(new_value)
            elif field_to_modify == 'date_of_birth':
                student.set_date_of_birth(new_value)
            elif field_to_modify == 'sex':
                student.set_sex(new_value)
            elif field_to_modify == 'country_of_birth':
                student.set_country_of_birth(new_value)
            print("Student record modified successfully.")
            return
    print(f"No student found with student number {student_number}.")

# function for deleting a student with a specific student number
def delete_student():
    student_number = int(input("Enter student number to delete: "))

    for student in students_array:
        if student.get_student_number() == student_number:
            students_array.remove(student) # removes the student from the array
            print("Student deleted successfully.")
            return
    print(f"No student found with student number {student_number}.")

# the menu when the program starts
while True:
    print("\nMenu:")
    print("1. Write the contents of the student array to a file")
    print("2. Read student data from a file and populate the student array")
    print("3. Add a new student")
    print("4. Find a student by student number")
    print("5. Show all students")
    print("6. Show all students born in a certain year")
    print("7. Modify a student record")
    print("8. Delete a student record")
    print("9. Quit")

    choice = input("Enter your choice (1-9): ")

    # based on choice, it will run the following:
    if choice == '1':
        write_to_file('./student_data.json', students_array)
        print("Student data written to file.")
    elif choice == '2':
        students_array = read_from_file('./student_data.json')
        print("Student data read from file and populated in the array.")
    elif choice == '3':
        add_student()
    elif choice == '4':
        find_student_by_number()
    elif choice == '5':
        show_all_students()
    elif choice == '6':
        show_students_by_birth_year()
    elif choice == '7':
        modify_student_record()
    elif choice == '8':
        delete_student()
    elif choice == '9':
        print("Exiting the program, thanks ! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
