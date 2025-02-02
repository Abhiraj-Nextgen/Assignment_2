class Class:
    def __init__(self, section_name: str, class_teacher_name: str): #Initializing class details
        self.section_name = section_name
        self.class_teacher_name = class_teacher_name

    def display(self): #Display class details
        print(f"Section Name: {self.section_name}")
        print(f"Class Teacher: {self.class_teacher_name}")

    def update_details(self, section_name=None, class_teacher_name=None): #Updating class details
        if section_name:
            self.section_name = section_name
        if class_teacher_name:
            self.class_teacher_name = class_teacher_name
        print("Class details updated")

class Students(Class): #Child class inheriting from Class
    def __init__(self, name: str, roll_no: int, subject_marks: list, section_name: str, class_teacher_name: str): #Initializing student details with inherited class details
        super().__init__(section_name, class_teacher_name)  # Inheriting from Class
        self.name = name
        self.roll_no = roll_no
        self.subject_marks = subject_marks

    def display(self): #Displaying student and class details
        super().display()  # Calling parent class display method
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Subject Marks: {self.subject_marks}")

    def calculate_average(self): #Calculate and return average marks
        return sum(self.subject_marks) / len(self.subject_marks) if self.subject_marks else 0

    def update_details(self, name=None, roll_no=None, subject_marks=None, section_name=None, class_teacher_name=None): #Updating student and class details
        super().update_details(section_name, class_teacher_name)  # Call parent method
        if name:
            self.name = name
        if roll_no:
            self.roll_no = roll_no
        if subject_marks:
            self.subject_marks = subject_marks
        print("Student details updated")

student1 = Students("Abhiraj", 101, [85, 90, 78], "10A", "Mr. X")
student1.display()

print(f"Average Marks: {student1.calculate_average()}")

student1.update_details(name="Krish", subject_marks=[92, 88, 95], section_name="10B", class_teacher_name="Mrs. Y")
student1.display()

print(f"Average Marks: {student1.calculate_average()}")