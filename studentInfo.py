class StudentInfo:
    def __init__(self,name,rollno,course,semester,location):
        self.name = name,
        self.rollno = rollno,
        self.course = course,
        self.semester = semester,
        self.location = location

    def studentInfo(self):
        print(f"{self.name}--{self.rollno}--{self.course}--{self.semester}--{self.location}") 

stu = StudentInfo("Amrit",10220,"UPSC","4TH","MUMBAI")
stu.studentInfo()           

