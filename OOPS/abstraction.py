#in abstraction we have to use abstract class and method
#in python this can be done with abc module
from abc import ABC

#this is abstract class with abstract method
class Car(ABC):
  def milege(self):
    pass

#this classes is using abstarct method
class Tesla(Car):
  def milege(self):
    print("it have milege of 45")

#this classes is using abstarct method
class Toyota(Car):
  def milege(self):
    print("it have milege of 18")

#this classes is using abstarct method
class Suzuki(Car):
  def milege(self):
    print("it have milege of 12")

car1 = Tesla()
car1.milege()

car2 = Toyota()
car2.milege()

car3 = Suzuki()
car3.milege()