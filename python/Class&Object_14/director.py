#from Class&Object_14 
from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef

student1 = Student("Jim", "Business", 3.1, False)
print(student1.gpa)

myChef = Chef()
myChef.make_salad()

myChineseChef = ChineseChef()
myChineseChef.make_salad()