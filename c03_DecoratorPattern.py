# DecoratorPattern.py

# Base class of beverage

class Beverage(object):
    def __init__(self):
        pass

    def cost(self):
        return 0.0

    def description(self):
        return "Unknown beverage"
    

class Decorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def condimentCost(self):
        return 0.0

    def condimentDescription(self):
        return ""

    def cost(self):
        return self.beverage.cost() + self.condimentCost()

    def description(self):
        return self.beverage.description() + ", " + self.condimentDescription()


# Example

class HouseBlend(Beverage):
    def cost(self):
        return 25.0

    def description(self):
        return "Houseblend coeffee"

class Expresso(Beverage):
    def cost(self):
        return 17.0

    def description(self):
        return "Expresso"


class WithMilk(Decorator):
    def condimentCost(self):
        return 5.0

    def condimentDescription(self):
        return "with milk"


class WithSuger(Decorator):
    def condimentCost(self):
        return 0.5

    def condimentDescription(self):
        return "with suger"



# Use case

americanoWithMilkAndSugre = WithSuger(WithMilk(HouseBlend()))
print "{}, ${}".format(americanoWithMilkAndSugre.description(), americanoWithMilkAndSugre.cost())

espressoWithDoubleMilk = WithMilk(WithMilk(Expresso()))
print "{}, ${}".format(espressoWithDoubleMilk.description(), espressoWithDoubleMilk.cost())



    


