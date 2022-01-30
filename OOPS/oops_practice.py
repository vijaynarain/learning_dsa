class Student:
    increment = 1.5
    num = 0
    def __init__(self,name,stipend,company):
        self.name = name
        self.stipend = stipend
        self.company = company
        #self.rollnoIncre = 10
        Student.num += 1
        
    def increments(self):
        self.stipend = int(self.stipend * self.increment)
        
    def __add__(self,other):
        return self.stipend + other.stipend
    
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
    @classmethod
    def from_str(cls, student_details):
        name, stipend, company = student_details.split(" ")
        return cls(name, stipend, company)
        
    @staticmethod
    def max_std(number):
        if number <= 100:
            return f"You can store {number - Student.num} more data"
        else:
            return f"You can store {number - Student.num} less data"

class Programmer(Student):
    def __init__(self, name, stipend, company, bond, domain):
        super().__init__(name, stipend, company)
        self.bond = bond
        self.domain = domain
        
    def increments(self):
        self.stipend = int(self.stipend * (self.increment + 1.5))
        
        

student1 = Programmer("Vijay",10000,"Google","2year","SDE")
student2 = Programmer("Pranay",7000,"Meta","1year","JSDE")
print(student1.stipend)
student1.increments()
print(student1.stipend)
print(student1.name,student1.bond)
print(student1 + student2)
# student1 = Student('Vijay',10000,'Google')
# student2 = Student('Pranay',7500,'Meta')
# student3 = Student.from_str("Rahul 5000 Wipro")

#print(Student.max_std(97))
#print(student3.name)
# print(student1.stipend)
# print(student2.stipend)
# Student.change_increment(3)
# student1.increments()
# 
# print(student1.stipend)



