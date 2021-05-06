print(1)
#1111111111111111111111
class Fruit:
  def __init__(self,name,color,weight):
    self.color=color
    self.weight=weight
    self.name=name
  def __show_parmeters__(self):
    print(f'The weight of {self.name} is {self.weight} , its color - {self.color}')


lemon=Fruit('lemon','yellow',58)
lemon.__show_parmeters__()


#222222222222222222222
print()
print(2)

class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree') 

JeyJey=Monkey()
CoCo=Monkey()

print(f'JeyJey\'s max age is {JeyJey.max_age} ')
if JeyJey.loves_bananas:
  print('JeyJey loves bananas')

print(f'CoCo\'s max age is {CoCo.max_age} ')
if CoCo.loves_bananas:
  print('CoCo loves bananas')

JeyJey.climb()
CoCo.climb()

#33333333333333333333333
print()
print(3)

class Person:
  def __init__(self,name,age,gender):
    self.name=name
    self.gender=gender
    self.age=age
  def calculate_age(self,years):
    print(f'{self.name} will be {self.age+years} in {years} years ')

#Пропустила урок про тестирования , теперь стараюсь понять
#Когда пойму , пришлю дз
  
individual = Person('Luxemburg', 99, 'gender-fluid')
individual.calculate_age(10)
