class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def myfunc(self):
    print("Hello my name is " + self.name + " I am a " + self.gender + " and I am " + str(self.age) + " years old")

p1 = Person("John", 36, "Male")
p1.myfunc()

p2 = Person("Deshaw", 27, "Female")
p2.myfunc()



class Building:
  def __init__(self, type, condition):
    self.type = type
    self.condition = condition

  def dialog(self):
    print("This is a " + self.type + " it looks " + self.condition)

b1 = Building("Hotel", "brand new")
b2 = Building("Dive Bar", "run down")

b1.dialog()
b2.dialog()