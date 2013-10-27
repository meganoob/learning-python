cars = ["mustang", "bmw", "mercedes", "audi", "bmw"]
print cars[0:2]

#print "test {0} {1}".format("ryan", "isobel")
#print str(int("1") + 4)

def add(a, b):
  return a + b
#print add("mary", "poppins")

class Car():
  def __init__(self, brand, model,wheels):
    self.brand = brand
    self.model = model
    self.wheels = wheels

  def whats_my_name(self):
    return "brand: {0}, model: {1}, number of wheels: {2}".format(self.brand, self.model, str(self.wheels))

cars = [Car("mustang", "sally", 1), Car("bmw", "1 series", 9)]

for car in cars:
  print car
  print car.whats_my_name()


class Puppy():
  def __init__(self, breed, sex, age):
    self.breed = breed
    self.sex = sex
    self.age = age

  def __str__(self):
    return "breed: {0}, sex: {1}, age: {2} weeks".format(self.breed, self.sex, str(self.age))

  def is_too_old(self):
    if self.age > 12:
      return True
    else:
      return False

puppies = [Puppy("corgi", "male", 6), Puppy("labrador", "female", 14), Puppy("pug", "male", 8)]
for puppy in puppies:
  if not puppy.is_too_old():
    print str(puppy)
