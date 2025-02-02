class Students:
    def __init__(self, name: str, roll_no: int, subject_marks: list): #Initializing student details
        self.name = name
        self.roll_no = roll_no
        self.subject_marks = subject_marks

    def display(self): #Display all student details
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Subject Marks: {self.subject_marks}")

    def calculate_average(self): #Calculate and return average marks
        if not self.subject_marks:
            return 0
        return sum(self.subject_marks) / len(self.subject_marks)

    def update_details(self, name=None, roll_no=None, subject_marks=None): #Update student details based on user input
        if name:
            self.name = name
        if roll_no:
            self.roll_no = roll_no
        if subject_marks:
            self.subject_marks = subject_marks
        print("Student details updated")

student1 = Students("Abhiraj", 101, [85, 90, 78])
student1.display()

print(f"Average Marks: {student1.calculate_average()}")

student1.update_details(name="Krish", subject_marks=[92, 88, 95])
student1.display()

print(f"Average Marks: {student1.calculate_average()}")
