class student:
    def __init__(self,name,grade,gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
    def honors(self):
        if (self.gpa >= 4.0):
            return "Highest Honors"
        elif (self.gpa >= 3.75):
            return "High Honors"
        elif (self.gpa >= 3.5):
            return "Honors"
        else:
            return None
student1 = student("Ted", 10, 3.97)
student2 = student("Bob", 9, 4.1)
#print(student1.honors())
#print(student2.honors())