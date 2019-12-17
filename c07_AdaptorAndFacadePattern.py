# Adaptor pattern: convert one interface to another.

# Interface of a duck
class Duck(object):

    def getName(self):
        pass

    def quack(self):
        pass

    def fly(self):
        pass


# Interface of a turkey

class Turkey(object):

    def getName(self):
        pass

    def gobble(self):
        pass

    def fly(self):
        pass


# The adaptor class adapting a turkey to a duck

class TurkeyToDuckAdaptor(Duck):

    def __init__(self, turkey):
        assert isinstance(turkey, Turkey)
        # So can handle all child class of Turkey.
        self.turkey = turkey

    # So the interface should be same as a Duck.

    def getName(self):
        return self.turkey.getName()

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        # Fly t times.
        for i in range(5):
            self.turkey.fly()


# So a concete turkey class

class FatTurkey(Turkey):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def gobble(self):
        print "{} is gobbling !!!".format(self.name)

    def fly(self):
        print "{} is fly a very short distance.".format(self.name)


# Test

fatTurkeyTom = FatTurkey("Tom")

duckOnly = TurkeyToDuckAdaptor(fatTurkeyTom)
if isinstance(duckOnly, Duck):
    print "{} is a duck, perform duck behaviors.".format(duckOnly.getName())
    duckOnly.quack()
    duckOnly.fly()
else:
    print "{} is not a duck, can't perform duck behaviors.".format(duckOnly.getName())



# Facade pattern: simplify an interface.

# A simpler version of home theater.
class TV:
    def on(self):
        print "TV is on."

    def off(self):
        print "TV is off."

class Amp:
    def on(self):
        print "Amp if on."
    
    def volumeUp(self):
        print "Amp volume up."

    def off(self):
        print "Amp is off."

    def volumeDown(self):
        print "Amp volume down."

class CoffeeMachine:
    def on(self):
        print "Coffee machine is on."

    def makeCoffee(self):
        print "Make a americano !!!"

    def off(self):
        print "Coffee machine is off."


# So if we directly operate these three things.

print ""

tv = TV()
amp = Amp()
coffeeMachine = CoffeeMachine()

print "Prepare to watch TV:"
tv.on()
amp.on()
amp.volumeUp()
coffeeMachine.on()
coffeeMachine.makeCoffee()

print "TV show ends."
coffeeMachine.off()
amp.volumeDown()
amp.off()
tv.off()

print ""

# Encapslate these into a facade class

class LivingRoomFacade:

    def __init__(self, tv, amp, coffeeMachine):
        self.tv = tv
        self.amp = amp
        self.coffeeMachine = coffeeMachine

    def startWatchTV(self):
        print "Prepare to watch TV:"
        self.tv.on()
        self.amp.on()
        self.amp.volumeUp()
        self.coffeeMachine.on()
        self.coffeeMachine.makeCoffee()

    def stopWatchTV(self):
        print "TV show ends."
        self.coffeeMachine.off()
        self.amp.volumeDown()
        self.amp.off()
        self.tv.off()


# So now we can enjoy an easy life.

facade = LivingRoomFacade(tv, amp, coffeeMachine)
facade.startWatchTV()
facade.stopWatchTV()