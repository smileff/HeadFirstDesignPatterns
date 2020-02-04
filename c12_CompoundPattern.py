# The Compound Pattern

# Use a lot pattern together to solve the problem: 
# Adapter pattern to adapt goose to a quackable.
# Decorator pattern to count quack numbers.
# Composite and iterator pattern to manage quackable group.
# Observer pattern to let quackologist know ducks are quacking.
# It's realy a messy, hard to understand.

# The Observer pattern to make our class obeserverable
class Observer(object):
    def update(self, observable):
        raise Exception("Observer::update not implemented.")

class Observable(object):

    def __init__(self, subject):
        self.subject = subject
        self.observers = []

    def registerObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.subject)


# The interface of a quackable duck and its concrete class
# Use composition to put observer into the Quackable, instead of inheriting the Observable class.

class Quackable(object):

    def __init__(self):
        self.observable = Observable(self)

    def typeName(self):
        raise Exception("Quackable::name not implemented.")

    def quack(self):
        raise Exception("Quackable::quack not implmented.")

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()


# The concrete quackable classes.

class MallardDuck(Quackable):

    def __init__(self):
        super(MallardDuck, self).__init__()

    def typeName(self):
        return "MallardDuck"
    
    def quack(self):
        print "Mallard quack"
        self.notifyObservers()


class RedHeadDuck(Quackable):

    def __init__(self):
        super(RedHeadDuck, self).__init__()

    def typeName(self):
        return "RedHeadDuck"

    def quack(self):
        print "Red head Quack"
        self.notifyObservers()


class DuckCall(Quackable):

    def __init__(self):
        super(DuckCall, self).__init__()

    def typeName(self):
        return "DuckCall"

    def quack(self):
        print "Kwak"
        self.notifyObservers()

    
class RubberDuck(Quackable):

    def __init__(self):
        super(RubberDuck, self).__init__()

    def typeName(self):
        return "RubberDuck"

    def quack(self):
        print "Squeak"
        self.notifyObservers()


# Goose

class Goose(object):
    def honk(self):
        print "Honk"

# Use adaptor to make Goose compitable with quackable.
class GooseAdaptor(Quackable):

    def __init__(self, goose):
        super(GooseAdaptor, self).__init__()

        assert isinstance(goose, Goose)
        self.goose = goose

    def typeName(self):
        return "GooseAdaptor"

    def quack(self):
        self.goose.honk()
        self.notifyObservers()


# Use decorator pattern to count the quack number
class QuackCounter(Quackable):

    numberOfQuacks = 0

    def __init__(self, quackable):
        super(QuackCounter, self).__init__()
        self.quackable = quackable

    def typeName(self):
        return self.quackable.typeName()

    def quack(self):
        self.quackable.quack()
        QuackCounter.numberOfQuacks += 1

    @staticmethod
    def getQuackNumber():
        return QuackCounter.numberOfQuacks


# Use the factory pattern to encapsolute the object creation
class AbstractDuckFactory(object):

    @staticmethod
    def createMallardDuck():
        return QuackCounter(MallardDuck())

    @staticmethod
    def createRedheadDuck():
        return QuackCounter(RedHeadDuck())

    @staticmethod
    def createDuckCall():
        return QuackCounter(DuckCall())

    @staticmethod
    def createRubberDuck():
        return QuackCounter(RubberDuck())

    @staticmethod
    def createGoose():
        return QuackCounter(GooseAdaptor(Goose()))


# Use composite pattern to treat an individual duck and a flock of duck uniformly.

class DuckFlock(Quackable):

    def __init__(self):
        super(DuckFlock, self).__init__()
        self.quackableList = []     # Use a list to store quackables.

    def quack(self):
        for quackable in self.quackableList:
            quackable.quack()
            quackable.notifyObservers()

    # This is not a method in the Quackable interface, only DuckFlock can call this.
    def add(self, quackable):
        if isinstance(quackable, DuckFlock):
            self.quackableList.extend(quackable.quackableList)
        else:
            self.quackableList.append(quackable)


    def registerObserver(self, observer):
        for quackable in self.quackableList:
            quackable.registerObserver(observer)

    # def notifyObservers(self):
    #     self.observable.notifyObservers()

# The observer: Quackoologist
class Quackologist(Observer):

    def update(self, quackable):
        assert isinstance(quackable, Quackable)
        print "Quackologist: {} just quacked".format(quackable.typeName())


# The test driver for quackable.
class DuckSimulator(object):

    def simulateQuack(self, quackable):
        assert isinstance(quackable, Quackable)
        quackable.quack()

    def simulate(self):

        quackologist = Quackologist()

        mallardDuck = AbstractDuckFactory.createMallardDuck()
        redHeadDuck = AbstractDuckFactory.createRedheadDuck()
        duckCall = AbstractDuckFactory.createDuckCall()
        rubberDuck = AbstractDuckFactory.createRubberDuck()
        goose = AbstractDuckFactory.createGoose()

        flockOfDucks = DuckFlock()
        flockOfDucks.add(mallardDuck)
        flockOfDucks.add(redHeadDuck)
        flockOfDucks.add(duckCall)
        flockOfDucks.add(rubberDuck)
        flockOfDucks.add(goose)

        mallardOne = AbstractDuckFactory.createMallardDuck()
        mallardTwo = AbstractDuckFactory.createMallardDuck()
        mallardThree = AbstractDuckFactory.createMallardDuck()
        mallardFour = AbstractDuckFactory.createMallardDuck()
        mallardFive = AbstractDuckFactory.createMallardDuck()
        
        flockOfMallards = DuckFlock()
        flockOfMallards.add(mallardOne)
        flockOfMallards.add(mallardTwo)
        flockOfMallards.add(mallardThree)
        flockOfMallards.add(mallardFour)
        flockOfMallards.add(mallardFive)

        flockOfDucks.add(flockOfMallards)

        flockOfDucks.registerObserver(quackologist)

        print "\nDuck Simulator"

        # self.simulateQuack(mallardDuck)
        # self.simulateQuack(redHeadDuck)
        # self.simulateQuack(duckCall)
        # self.simulateQuack(rubberDuck)
        # self.simulateQuack(goose)
        self.simulateQuack(flockOfDucks)

        print "Goose quack count: {}".format(QuackCounter.getQuackNumber())


if __name__ == "__main__":
    duckSimulator = DuckSimulator()
    duckSimulator.simulate()