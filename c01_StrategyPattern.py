
# Behavior delegate

class FlyBehavior:
    def fly(self):
        assert False

class QuackBehavior:
    def quack(self):
        assert False


class Duck:

    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None

    # The method default for all kind of ducks 

    def swim(self):
        print "Default swim style."

    def display(self):
        print "Default duck look."

    # The strategy pattern behavior

    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior

    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior

    def performFly(self):
        if self.flyBehavior != None:
            self.flyBehavior.fly()

    def performQuack(self):
        if self.quackBehavior:
            self.quackBehavior.quack()

# An instance

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print "Flying with a rocket !"

class FlyNoWay(FlyBehavior):
    def fly(self):
        print "Can't fly."

class QuackLoudly(QuackBehavior):
    def quack(self):
        print "Quack very loudly !"


class MallardDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyRocketPowered())
        self.setQuackBehavior(QuackLoudly())

    
# Test

mallardDuck = MallardDuck()
mallardDuck.swim()
mallardDuck.display()
mallardDuck.performFly()
mallardDuck.performQuack()

mallardDuck.setFlyBehavior(FlyNoWay())
mallardDuck.performFly()