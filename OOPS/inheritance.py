class Car:
  def __init__(self):
    self.color = "white"
    self.wheel = 4
    self.gear = "manual"

  def rto(self):
    print("you need rto files for this")
    

class Tesla(Car):
  def __init__(self):
    self.color = "blue"
    self.gear = "auto"

car1 = Tesla()
car2 = Car()
print(car1.color)
print(car2.color)

