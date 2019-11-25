# Factory Method Pattern


class Pizza(object):

    def __init__(self, pizzaName = "Imaginary pizza"):
        self.pizzaName = pizzaName

    def name(self):
        return self.pizzaName

# The first version, factory method pattern

class PizzaStore(object):

    def __init__(self, storeName = "Imaginary store"):
        self.storeName = storeName        

    def createPizza(self, pizzaName):        
        # The abstract factory method, should return a pizza object.
        return Pizza()

    def prepare(self, pizza):
        print "{} is preparing the {}.".format(self.storeName, pizza.name())

    def bake(self, pizza):
        print "{} is baking the {}.".format(self.storeName, pizza.name())

    def cut(self, pizza):
        print "{} is cutting the {}.".format(self.storeName, pizza.name())

    def box(self, pizza):
        print "{} is boxing the {}.".format(self.storeName, pizza.name())

    def orderPizza(self, pizzaName):
        # First call the factory method to create a pizza
        pizza = self.createPizza(pizzaName)

        self.prepare(pizza)
        self.bake(pizza)
        self.cut(pizza)
        self.box(pizza)

        return pizza


# The concrete pizza store.

class NYCheesePizza(Pizza):
    def __init__(self):
        super(NYCheesePizza, self).__init__("NYCheesePizza")

class NYBeefPizza(Pizza):
    def __init__(self):
        super(NYBeefPizza, self).__init__("NYBeefPizza")

class NYFruitPizza(Pizza):
    def __init__(self):
        super(NYFruitPizza, self).__init__("NYFruitPizza")

class NYPizzaStore(PizzaStore):

    def __init__(self):
        super(NYPizzaStore, self).__init__("NYPizzaStore")

    def createPizza(self, pizzaName):
        # Implement the factor method
        if pizzaName == "CheesePizza":
            return NYCheesePizza()
        elif pizzaName == "BeefPizza":
            return NYBeefPizza()
        elif pizzaName == "FruitPizza":
            return NYFruitPizza()
        else:
            return None



class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoCheesePizza, self).__init__("ChicagoCheesePizza")

class ChicagoBeefPizza(Pizza):
    def __init__(self):
        super(ChicagoBeefPizza, self).__init__("ChicagoBeefPizza")

class ChicagoFruitPizza(Pizza):
    def __init__(self):
        super(ChicagoFruitPizza, self).__init__("ChicagoFruitPizza")

class ChicagoPizzaStore(PizzaStore):

    def __init__(self):
        super(ChicagoPizzaStore, self).__init__("ChicagoPizzaStore")

    def createPizza(self, pizzaName):
        # Implement the factor method
        if pizzaName == "CheesePizza":
            return ChicagoCheesePizza()
        elif pizzaName == "BeefPizza":
            return ChicagoBeefPizza()
        elif pizzaName == "FruitPizza":
            return ChicagoFruitPizza()
        else:
            return None

    

# Test

nyPizzaStore = NYPizzaStore()
nyPizzaStore.orderPizza("CheesePizza")
nyPizzaStore.orderPizza("BeefPizza")
nyPizzaStore.orderPizza("FruitPizza")

chicagoPizzaStore = ChicagoPizzaStore()
chicagoPizzaStore.orderPizza("CheesePizza")
chicagoPizzaStore.orderPizza("BeefPizza")
chicagoPizzaStore.orderPizza("FruitPizza")