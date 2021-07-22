# inheritance allows us to definte attributes and functions within a class and create another class that inherits those attributes
# this means you don't have to repeat your code

from Chef import Chef

myChef = Chef()
myChef.make_chicken()

from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
