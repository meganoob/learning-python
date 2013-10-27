import pprint
from puppymodule.puppies import Puppy

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

puppies = [Puppy("corgi", "male", 6), Puppy("labrador", "female", 14), Puppy("pug", "male", 8)]

named_puppies = { "Ralph" : Puppy("corgi", "male", 6), "Mindy" : Puppy("labrador", "female", 14), "Harold" : Puppy("pug", "male", 8) }

for puppy in puppies:
  if not puppy.is_too_old():
    print str(puppy)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(puppies)

print named_puppies["Ralph"]

for k, v in named_puppies.items():
  print k

for v in named_puppies.itervalues():
  print v.breed 

f = open("isobel.txt", "w")
myvalues = "\n".join(["test1", "test2", "test3"])
f.write(myvalues)
f.close()

f = open("isobel.txt", "r")
myfile = f.read()
if "te" in myfile:
  print "POOP"

print myfile