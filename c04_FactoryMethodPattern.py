# Factory Method Pattern

# It's a modification version of the source in the book: I put the PizzaIngredientFactory into PizzaStore, instead of Pizza class.

# The abstract ingredient factory

class PizzaIngredientFactory(object):

    def __init__(self, factoryName):
        self.factorName = factoryName

    def createDough(self):
        return "no dough"

    def createSauce(self):
        return "no sauce"

    def createCheese(self):
        return "no cheese"


# The interface of pizza (Dependency Inversion Priciple: the PizzaStore depends on it, and the concrete pizza depends on it too.)

class Pizza(object):

    def __init__(self, pizzaName):
        self.pizzaName = pizzaName
        self.dough = ""
        self.sauce = ""
        self.cheese = ""

    def name(self):
        return self.pizzaName

    def setDough(self, dough):
        self.dough = dough

    def setSauce(self, sauce):
        self.sauce = sauce

    def setCheese(self, cheese):
        self.cheese = cheese

    def present(self):
        desc = self.pizzaName
        if self.dough != "":
            desc += ": " + self.dough
        if self.sauce != "":
            desc += " + " + self.sauce
        if self.cheese != "":
            desc += " + " + self.cheese
        print desc
    

# The first version, factory method pattern

class PizzaStore(object):

    def __init__(self, storeName, ingredientFactory):
        self.storeName = storeName
        self.ingredientFactory = ingredientFactory

    def createPizza(self, pizzaName):        
        # The abstract factory method, should return a pizza object.
        # We could provide an default implementation here, or we could let the subclass decide whihc concrete pizza to initiailize.        
        return Pizza()

    def prepare(self, pizza):
        print "{} is preparing the {}.".format(self.storeName, pizza.name())
        if (isinstance(self.ingredientFactory, PizzaIngredientFactory)):
            pizza.setDough(self.ingredientFactory.createDough())
            pizza.setSauce(self.ingredientFactory.createSauce())
            pizza.setCheese(self.ingredientFactory.createCheese())

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


# The NY style concrete pizza and it's ingredient factory.

class NYCheesePizza(Pizza):
    def __init__(self):
        super(NYCheesePizza, self).__init__("NYCheesePizza")

class NYBeefPizza(Pizza):
    def __init__(self):
        super(NYBeefPizza, self).__init__("NYBeefPizza")

class NYFruitPizza(Pizza):
    def __init__(self):
        super(NYFruitPizza, self).__init__("NYFruitPizza")


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        super(NYPizzaIngredientFactory, self).__init__("NYPizzaIngredientFactory")

    def createDough(self):
        return "NY style dough"

    def createSauce(self):
        return "NY style sauce"

    def createCheese(self):
        return "NY style cheese"


class NYPizzaStore(PizzaStore):

    def __init__(self):
        super(NYPizzaStore, self).__init__("NYPizzaStore", NYPizzaIngredientFactory())

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

# Chicago style pizza 

class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoCheesePizza, self).__init__("ChicagoCheesePizza")

class ChicagoBeefPizza(Pizza):
    def __init__(self):
        super(ChicagoBeefPizza, self).__init__("ChicagoBeefPizza")

class ChicagoFruitPizza(Pizza):
    def __init__(self):
        super(ChicagoFruitPizza, self).__init__("ChicagoFruitPizza")


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        super(ChicagoPizzaIngredientFactory, self).__init__("ChicagoPizzaIngredientFactory")

    def createDough(self):
        return "Chicago style dough"

    def createSauce(self):
        return "Chicago style sauce"

    def createCheese(self):
        return "Chicago style cheese"

class ChicagoPizzaStore(PizzaStore):

    def __init__(self):
        super(ChicagoPizzaStore, self).__init__("ChicagoPizzaStore", ChicagoPizzaIngredientFactory())

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
nyPizzaStore.orderPizza("CheesePizza").present()
nyPizzaStore.orderPizza("BeefPizza").present()
nyPizzaStore.orderPizza("FruitPizza").present()

chicagoPizzaStore = ChicagoPizzaStore()
chicagoPizzaStore.orderPizza("CheesePizza").present()
chicagoPizzaStore.orderPizza("BeefPizza").present()
chicagoPizzaStore.orderPizza("FruitPizza").present()
