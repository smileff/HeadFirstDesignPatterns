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

# List menu ----------------------

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


class ListMenu(Menu):

    def __init__(self):
        # Use a list to store the menu items.
        self.menu = []

    def add(self, item):
        assert isinstance(item, MenuItem)
        self.menu.append(item)

    def createIterator(self):
        return ListMenuIterator(self.menu)

    
# Dict menu ----------------------

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



# Dict menu -----------------------------

class DictMenu(Menu):
    def __init__(self):
        # Dinner menu use a dict to store the menu items.
        self.menu = {}

    def add(self, item):
        assert isinstance(item, MenuItem)
        self.menu[item.getName()] = item

    def createIterator(self):
        return DictMenuIterator(self.menu)

# Tree menu ------------------------------

class TreeMenuNodeIterator(object):
    def __init__(self, nodeList):
        assert isinstance(nodeList, list)
        self.nodeList = nodeList
        self.currIndex = 0

    def hasNext(self):
        return self.currIndex < len(self.nodeList)

    def next(self):
        assert self.currIndex < len(self.nodeList)
        currIndex = self.currIndex
        self.currIndex += 1
        return self.nodeList[currIndex]

    def peek(self):
        assert self.currIndex < len(self.nodeList)
        return self.nodeList[self.currIndex]


# In the book, a component class is defined as the base class of composite class and leaf class, to achieve the transparency.
# Here seperate the composite class (TreeMenuNode) from the leaf class (MenuItem).

class TreeMenuNode(object):

    def __init__(self):
        #  Use a list to store the children components
        self.children = []

    def add(self, node):
        assert isinstance(node, MenuItem) or isinstance(node, TreeMenuNode)
        self.children.append(node)

    def createIterator(self):
        return TreeMenuNodeIterator(self.children)


class TreeMenuIterator(MenuIterator):

    def __init__(self, root):
        # The input it must be a iterator, even can be a tree menu iterator.
        assert isinstance(root, TreeMenuNode)
        # Use a list as a stack to do the DFS iteration.
        self.iterStack = []
        it = root.createIterator()
        assert isinstance(it, TreeMenuNodeIterator)
        self.iterStack.append(it)

    def gotoNextLeafNode(self):
        while len(self.iterStack) > 0:
            it = self.iterStack[-1]
            if it.hasNext():
                # Check the last iterator
                if isinstance(it.peek(), MenuItem):
                    # We find the first leaf node.
                    return True
                elif isinstance(it.peek(), TreeMenuNode):
                    newIt = it.next().createIterator()
                    assert isinstance(newIt, TreeMenuNodeIterator)
                    self.iterStack.append(newIt)
            else:
                self.iterStack.pop()

        # Reach here means the whole tree has no leaf node.
        return False

    def hasNext(self):
        return self.gotoNextLeafNode()

    def next(self):
        if self.gotoNextLeafNode():
            return self.iterStack[-1].next()
        else:
            raise Exception("No next node.")


class TreeMenu(Menu):

    def __init__(self):
        self.root = TreeMenuNode()

    def add(self, item):
        if isinstance(item, MenuItem):
            self.root.add(item)
        elif isinstance(item, TreeMenu):
            self.root.add(item.root)
        else:
            raise Exception("Unsupported item: {}".format(type(item)))

    def createIterator(self):
        return TreeMenuIterator(self.root)

# Waitress ---------------------------------------

class Waitress(object):

    def __init__(self):
        self.menus = {}

    def addMenu(self, name, menu):
        assert isinstance(menu, Menu)
        self.menus[name] = menu

    def printAllMenu(self):
        print "ALl menu item."
        for name, menu in self.menus.items():
            print name

            iterator = menu.createIterator()
            assert isinstance(iterator, MenuIterator)
            while iterator.hasNext():
                menuItem = iterator.next()
                assert isinstance(menuItem, MenuItem)
                print "{}, {}\n\t-- {}.".format(menuItem.getName(), menuItem.getPrice(), menuItem.getDescription())
            print ""

    def printVegetalMenu(self):
        print "All vegetal menu item."
        for name, menu in self.menus.items():
            print name
            iterator = menu.createIterator()
            assert isinstance(iterator, MenuIterator)
            while iterator.hasNext():
                menuItem = iterator.next()
                assert isinstance(menuItem, MenuItem)
                if menuItem.getIsVegetal():
                    print "{}, {}\n\t-- {}.".format(menuItem.getName(), menuItem.getPrice(), menuItem.getDescription())
            print ""



# Test, list and dict menu

print "Test list and dict menu"
print ""
    
pancakeHouseListMenu = ListMenu()
pancakeHouseListMenu.add(MenuItem("K&B's Pancake Breakfast", 2.99, "Pancakes with scrambled eggs and toast", True))
pancakeHouseListMenu.add(MenuItem("Regular Pancake Breakfast", 2.99, "Pancakes with fired eggs, sausage", False))
pancakeHouseListMenu.add(MenuItem("Blueberry Pancakes", 3.49, "Pancakes made with fresh blueberrie", True))
pancakeHouseListMenu.add(MenuItem("Waffles", 3.59, "Waffles, with your choice of blueberries or strawberries", True))

dinnerDictMenu = DictMenu()
dinnerDictMenu.add(MenuItem("Vegetarian BLT", 2.99, "(Fakin') Bacon with lettuce & tomato on whole wheat", True))
dinnerDictMenu.add(MenuItem("BLT", 2.99, "Bacon with lettuce & tomato on whole wheat", False))
dinnerDictMenu.add(MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False))
dinnerDictMenu.add(MenuItem("Hotdog", 3.05, "A hot dog, with saurkraut, relish, onions, topped with cheese", False))


cafeDictMenu = DictMenu()
cafeDictMenu.add(MenuItem("Veggie Burger and Air Fries", 3.99, "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True))
cafeDictMenu.add(MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False))
cafeDictMenu.add(MenuItem("A large burrito", 4.29, "A large burrito, with whole pinto beans, salsa, guacamole", False))

waitress1 = Waitress()
waitress1.addMenu("*** Pancake House Menu ***", pancakeHouseListMenu)
waitress1.addMenu("*** Dinner Menu ***", dinnerDictMenu)
waitress1.addMenu("*** Cafe Menu ***", cafeDictMenu)

waitress1.printAllMenu()
waitress1.printVegetalMenu()

# Test tree menu

print "Test tree menu"
print ""

pancakeHouseTreeMenu = TreeMenu()
pancakeHouseTreeMenu.add(MenuItem("K&B's Pancake Breakfast", 2.99, "Pancakes with scrambled eggs and toast", True))
pancakeHouseTreeMenu.add(MenuItem("Regular Pancake Breakfast", 2.99, "Pancakes with fired eggs, sausage", False))
pancakeHouseTreeMenu.add(MenuItem("Blueberry Pancakes", 3.49, "Pancakes made with fresh blueberrie", True))
pancakeHouseTreeMenu.add(MenuItem("Waffles", 3.59, "Waffles, with your choice of blueberries or strawberries", True))

dinnerTreeMenu = TreeMenu()
dinnerTreeMenu.add(MenuItem("Vegetarian BLT", 2.99, "(Fakin') Bacon with lettuce & tomato on whole wheat", True))
dinnerTreeMenu.add(MenuItem("BLT", 2.99, "Bacon with lettuce & tomato on whole wheat", False))
dinnerTreeMenu.add(MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False))
dinnerTreeMenu.add(MenuItem("Hotdog", 3.05, "A hot dog, with saurkraut, relish, onions, topped with cheese", False))

cafeTreeMenu = TreeMenu()
cafeTreeMenu.add(MenuItem("Veggie Burger and Air Fries", 3.99, "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True))
cafeTreeMenu.add(MenuItem("Soup of the day", 3.29, "Soup of the day, with a side of potato salad", False))
cafeTreeMenu.add(MenuItem("A large burrito", 4.29, "A large burrito, with whole pinto beans, salsa, guacamole", False))

dessertTreeMenu = TreeMenu()
dessertTreeMenu.add(MenuItem("Apple Pie", 1.59, "Apple pie with a flaskey crust, topped with vanilla icecream", True))
dinnerTreeMenu.add(dessertTreeMenu)

allTreeMenu = TreeMenu()
allTreeMenu.add(pancakeHouseTreeMenu)
allTreeMenu.add(dinnerTreeMenu)
allTreeMenu.add(cafeTreeMenu)

waitress2 = Waitress()
waitress2.addMenu("*** All menu ***", allTreeMenu)

waitress2.printAllMenu()
waitress2.printVegetalMenu()