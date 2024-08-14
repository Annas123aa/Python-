#practice 1
#create a class called person with attributes name and age.create an object of the class and print it's attributes.
#class Person:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#teacher = Person("Ali",32)
#print(teacher.name)
#print(teacher.age)



#practice 2
#Add a method called greet to the person class that prints a greeting message including the persons name.
#class Person:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def greet(self):
#        print("hello " + self.name)
#teacher = Person("Ali",32)
#teacher.greet()




#practice 3
#Create a class called Car with attributes make, model and year. Include a method to print out the car details.
#class Car:
#    def __init__(self,make,model,year):
#        self.make = make
#        self.model = model
#        self.year = year
#    def info(self):
#        print(f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}")

#taxi = Car("LKA company","X200",2024)
#taxi.info()




#practice 4
#class Circle:
#    def __init__(self,r):
#        self.radius = r
#    def area(self):
#        return 3.14 * self.radius ** 2
#a = Circle(2)
#print(a.area())




#practice 5
#class Rectangle:
#    def __init__(self, width,length):
#        self.width = width
#        self.length = length
#    def area(self):
#        return self.width * self.length
#    def perimeter(self):
#        return 2 * self.width + 2 * self.length
#A = Rectangle(2,4)
#print(A.area())
#print(A.perimeter())

#----------------------------------------------------------------
                          #Inheritance

#practice 6
#class Animal:
#    def speak(self):
#        print("Animal sound")
#class Cat(Animal):
#    def speak(self):
#        print("Meow Meow")
#class Dog(Animal):
#    def speak(self):
#        print("Wow Wow")

#a = Cat()
#b = Dog()
#a.speak()
#b.speak()



#practice 7
#class Shape:
#    def area(self):
#        print("a method for calculating area of a shape")

#class Square(Shape):
#    def __init__(self,side):
#        self.side = side
#    def area(self):
#        print("Area of square:",self.side * self.side)
#class Triangle(Shape):
#    def __init__(self,base, height):
#        self.base = base
#        self.height = height 
#    def area(self):
#        print("Area of triangle:",self.base * #self.height * (1/2))
#my_square = Square(5)
#my_triangle = Triangle(4,6)
#my_square.area()
#my_triangle.area()



#practice 8
#create a class Employee with attributes name and salary.create a derived class Manager with an additional attribute department.

#class Employee:
#    def __init__(self,name, salary):
#        self.name = name
#        self.salary = int(salary)
#class Manager(Employee):
#    def __init__(self,name, salary, department):
#        super().__init__(name, salary)
#        self.department = department
#        
#man1 = Manager("Ahmad",20000,"IT")



#practice 9
#Create a base class vehicle with a method drive.create derived classes Bike and Truck that override the drive method.

#class Vehicle:
#    def __init__(self,name):
#        self.name = name
#    def drive(self):
#        print(f"The {self.name} is driving")

#class Bike(Vehicle):
#    def drive(self):
#        print(f"The {self.name} is being pedaled")    
#class Truck(Vehicle):
#    def drive(self):
#        print(f"The {self.name} is being trucking along")
#my_vehicle = Vehicle("generic vehicle")
#my_bike = Bike("mountain bike")
#my_truck = Truck("truck number 1")
#my_bike.drive()
#my_truck.drive()



#practice 10
#10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly.
#class Bird:
#    def __init__(self, name):
#        self.name = name
#    def fly(self):
#        print(f"The {self.name} is flying.")

#class Eagle(Bird):
#    pass

#class Penguin(Bird):
#    def fly(self):
#        print(f"Penguins can't fly!")
#my_bird = Bird("Generic Bird")
#my_eagle = Eagle("Bald Eagle")
#my_penguin = Penguin("Emperor Penguin")
#my_bird.fly()
#my_eagle.fly()
#my_penguin.fly()
#---------------------------------------------------------------


        