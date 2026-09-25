class Employee:
    def __init__(self,name,department):
        self.name =name
        self.department = department

    def dispay_info(self):
        print(f"employer:{self.name}---{self.department}")

# creating an object
employerone = Employee("Amit Kumar","Software Engineer")
employerone.dispay_info()        
            


     
