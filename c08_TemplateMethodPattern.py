# The Template Method Pattern.

# Differences from the Strategy pattern: 
# In the strategy pattern, the concrete class implements the whole algorithm.
# In the tempalte method pattern, the template method implements the outline of the algorithm, concreate class implement a step of the algorithm.


# A helper function to get input from stdin.
def GetStdinInput(hint):
    response = raw_input(hint)
    if response.endswith("\r"):
        response = response[:-1]
    return response


class CoffeineBeverage(object):

    def prepareBeverage(self):
        # The algorithm template
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.doesCustomerWantsCondiments():
            self.addCondiments()
        

    def boilWater(self):
        print "Boiling water."

    def brew(self):
        print "This method should be overridden."
        assert False

    def pourInCup(self):
        print "Pour beverage into a cup."

    def doesCustomerWantsCondiments(self):
        # This is a hook method: return default value, and the subclass can override it.
        return True

    def addCondiments(self):
        print "This method should be overridden."
        assert False


class Coffee(CoffeineBeverage):
    
    # The first concrete class should not override the prepareBeverage method.

    def brew(self):
        print "Extract coffee from grinded coffee powder."

    def addCondiments(self):
        print "Add milk and sugar."

    def doesCustomerWantsCondiments(self):
        while True:
            response = GetStdinInput("Do you want milk and sugar?").lower()
            print "Answer: {}".format(response)
            if response == "y" or response == "yes":
                return True
            elif response == "n" or response == "no":
                return False
            else:
                print "Please answer yes(y) or no(n)."


class Tea(CoffeineBeverage):
    
    # The second concrete class should not override the prepareBeverage method.

    def brew(self):
        print "Extract tea from tea leaves."

    def addCondiments(self):
        print "Add lemon."

    def doesCustomerWantsCondiments(self):
        while True:
            response = GetStdinInput("Do you want lemon?").lower()
            print "Answer: {}".format(response)
            if response == "y" or response == "yes":
                return True
            elif response == "n" or response == "no":
                return False
            else:
                print "Please answer yes(y) or no(n)."


class PureWater(CoffeineBeverage):
    # The third concrete class which doesn't override the hook method.

    def brew(self):
        # Nothing to brew
        pass

    # Don't add condiments, so no need to override this method. 
    # def addCondiments(self):

    def doesCustomerWantsCondiments(self):
        return False


# Test

print "Prepare a cup of coffee."
coffee = Coffee()
coffee.prepareBeverage()
print ""

print "Prepare a cup of tea."
tea = Tea()
tea.prepareBeverage()
print ""

print "Prepare a cup of pure water."
pureWater = PureWater()
pureWater.prepareBeverage()
print ""