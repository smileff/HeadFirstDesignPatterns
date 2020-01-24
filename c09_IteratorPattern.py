# Iterator Pattern

# The interface -------------------------

class MenuItem(object):

    def __init__(self, name, price, desc, isVegetal):
        assert isinstance(name, str)
        assert isinstance(price, float) or isinstance(price, int)
        assert isinstance(desc, str)
        assert isinstance(isVegetal, bool)

        self.name = name
        self.price = price
        self.description = desc
        self.isVegetal = isVegetal

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def getIsVegetal(self):
        return self.isVegetal


class MenuIterator(object):

    # The base class of iterator class.

    def hasNext(self):
        raise Exception("Call not implemented method MenuIterator.hasNext.")
        return False

    def next(object):
        # Should return an MenuItem
        raise Exception("Call not implemented method MenuIterator.next.")
        return None


class Menu(object):
    # The interface of the Menu class.

    def createIterator(self):
        # Should return a 
        raise Exception("Call not implemented method Menu.createIterator.")
        return None

# Concrete MenuIterators 

class ListMenuIterator(MenuIterator):

    def __init__(self, listMenu):
        assert isinstance(listMenu, list)
        self.listMenu = listMenu
        self.currIndex = 0

    def hasNext(self):
        return self.currIndex < len(self.listMenu)

    def next(self):
        if self.currIndex >= len(self.listMenu):
            raise Exception("ListMenuIterator, index: {} of of range: {}.".format(self.currIndex, len(self.listMenu)))
        elif not isinstance(self.listMenu[self.currIndex], MenuItem):
            raise Exception("ListMenuIterator, list element is not of type MenuItem.")
        else:
            index = self.currIndex
            self.currIndex += 1
            return self.listMenu[index]


class DictMenuIterator(MenuIterator):

    def __init__(self, dictMenu):
        assert isinstance(dictMenu, dict)
        self.dictMenu = dictMenu
        self.keyList = self.dictMenu.keys()
        self.currIndex = 0

    def hasNext(self):
        return self.currIndex < len(self.keyList)

    def next(self):
        if not self.currIndex < len(self.keyList):
            raise Exception("DictMenuIterator, index out of range.")
        elif not isinstance(self.dictMenu[self.keyList[self.currIndex]], MenuItem):
            raise Exception("DictMenuIterator, dict value is not of type MenuItem.")
        else:
            index = self.currIndex
            self.currIndex += 1
            return self.dictMenu[self.keyList[index]]



# Concrete menu

class PancakeHouseMenu(Menu):

    def __init__(self):
        # Use a list to store the menu items.
        self.menu = []

        # Add the food
        self.menu.append(MenuItem("K&B's Pancake Breakfast", 2.99, "Pancakes with scrambled eggs and toast", True))
        self.menu.append(MenuItem("Regular Pancake Breakfast", 2.99, "Pancakes with fired eggs, sausage", False))
        self.menu.append(MenuItem("Blueberry Pancakes", 3.49, "Pancakes made with fresh blueberrie", True))
        self.menu.append(MenuItem("Waffles", 3.59, "Waffles, with your choice of blueberries or strawberries", True))

    def createIterator(self):
        return ListMenuIterator(self.menu)

class DinnerMenu(Menu):
    def __init__(self):
        # Dinner menu use a dict to store the menu items.
        self.menu = {}
        self.menu["Vegetarian BLT"] = MenuItem("Vegetarian BLT", 2.99, "(Fakin') Bacon with lettuce & tomato on whole wheat", True)
        self.menu["BLT"] = MenuItem("BLT", 2.99, "Bacon with lettuce & tomato on whole wheat", False)
        self.menu["Soup of the day"] = MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False)
        self.menu["Hotdog"] = MenuItem("Hotdog", 3.05, "A hot dog, with saurkraut, relish, onions, topped with cheese", False)

    def createIterator(self):
        return DictMenuIterator(self.menu)


class CafeMenu(Menu):
    def __init__(self):
        self.menu = {}
        # Cafe menu uses a dict to store the menu items.
        self.menu["Veggie Burger and Air Fries"] = MenuItem("Veggie Burger and Air Fries", 3.99, "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True)
        self.menu["Soup of the day"] = MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False)
        self.menu["Burrito"] = MenuItem("A large burrito", 4.29, "A large burrito, with whole pinto beans, salsa, guacamole", False)

    def createIterator(self):
        return DictMenuIterator(self.menu)

class WaitressV1(object):
    # The waiteress version 1, print menu items.

    def __init__(self, pancakeHouseMenu, dinnerMenu, cafeMenu):
        assert isinstance(pancakeHouseMenu, Menu)
        assert isinstance(dinnerMenu, Menu)
        assert isinstance(cafeMenu, Menu)

        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinnerMenu = dinnerMenu
        self.cafeMenu = cafeMenu

    def printMenu(self, iterator):
        # A polymorpic method, loop menu item using interface of the iterator (programming to interface).
        assert isinstance(iterator, MenuIterator)
        while iterator.hasNext():
            menuItem = iterator.next()
            assert isinstance(menuItem, MenuItem)
            print "{}, {} -- {}.".format(menuItem.getName(), menuItem.getPrice(), menuItem.getDescription())

    def printAllMenu(self):
        print "*** Pancake House Menu ***"
        self.printMenu(self.pancakeHouseMenu.createIterator())
        print ""

        print "*** Dinner Menu ***"
        self.printMenu(self.dinnerMenu.createIterator())
        print ""

        print "*** Cafe Menu ***"
        self.printMenu(self.cafeMenu.createIterator())
        print ""

    
pancakeHouseMenu = PancakeHouseMenu()
dinnerMenu = DinnerMenu()
cafeMenu = CafeMenu()

waitress = WaitressV1(pancakeHouseMenu, dinnerMenu, cafeMenu)
waitress.printAllMenu()