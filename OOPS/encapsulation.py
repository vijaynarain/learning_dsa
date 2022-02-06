#By Using Protechted
"""
#base class
class Car:
  def __init__(self):
    #default milege
    self._milege = 21  #"_" means protechted 

#derived class
class Tesla(Car):
  def __init__(self):
    Car.__init__(self)
    print(f"tesla milege default {self._milege} ")

    #milege updated
    self._milege = 45
    print(f"tesla milege after modified {self._milege}")

#derived class
class Toyota(Car):
  def __init__(self):
    Car.__init__(self)
    print(f"toyota milege default {self._milege} ")

car1 = Tesla()
car2 = Toyota()
"""

#By Using Private
#base class
class Car:
  def __init__(self):
    #default milege
    self.milege = 21
    self.__milege = 21  #"_" means protechted 

#derived class
class Tesla(Car):
  def __init__(self):
    Car.__init__(self)
    print(f"tesla milege default {self.__milege} ")

    #milege updated
    self.__milege = 45
    print(f"tesla milege after modified {self.__milege}")

#derived class
class Toyota(Car):
  def __init__(self):
    Car.__init__(self)
    print(f"toyota milege default {self__milege} ")

car1 = Car()
print(f"this milege = {car1.milege} is not private")
car2 = Toyota()