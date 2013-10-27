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
