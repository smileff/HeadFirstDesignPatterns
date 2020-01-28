# The state pattern

import random

# I don't want

class GumballState(object):

    def __init__(self, stateName, gumballMachine):
        self.stateName = stateName
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "# Nothing happens."

    def ejectQuarter(self):
        print "# Nothing happens."

    def turnCrank(self):
        print "# Nothing happens."

    def dispense(self):
        print "# Nothing happens."

    def refill(self):
        print "# Nothing happens."

    def __str__(self):
        return self.stateName


class GumballStateNoQuarter(GumballState):

    def __init__(self, gumballMachine):
        super(GumballStateNoQuarter, self).__init__("NoQuarter", gumballMachine)

    def insertQuarter(self):
        self.gumballMachine.setState(GumballStateHasQuarter(self.gumballMachine))


class GumballStateHasQuarter(GumballState):

    def __init__(self, gumballMachine):
        super(GumballStateHasQuarter, self).__init__("HasQuarter", gumballMachine)

    def insertQuarter(self):
        print "# The gumball machine already has a quarter."
        self.gumballMachine.returnQuarter()

    def ejectQuarter(self):
        self.gumballMachine.returnQuarter()
        self.gumballMachine.setState(GumballStateNoQuarter(self.gumballMachine))

    def turnCrank(self):
        if self.gumballMachine.isLuckyCustomer():
            self.gumballMachine.setState(GumballStateWinner(self.gumballMachine))
        else:
            self.gumballMachine.setState(GumballStateSold(self.gumballMachine))
        self.gumballMachine.dispense()


class GumballStateSold(GumballState):

    def __init__(self, gumballMachine):
        super(GumballStateSold, self).__init__("Sold", gumballMachine)

    def insertQuarter(self):
        self.gumballMachine.returnQuarter()

    def dispense(self):
        self.gumballMachine.launchOneGumball()
        if self.gumballMachine.getGumballNumber() > 0:
            self.gumballMachine.setState(GumballStateNoQuarter(self.gumballMachine))
        else:
            self.gumballMachine.setState(GumballStateSoldOut(self.gumballMachine))
        

class GumballStateWinner(GumballState):

    def __init__(self, gumballMachine):
        super(GumballStateWinner, self).__init__("Winner", gumballMachine)

    def insertQuarter(self):
        self.gumballMachine.returnQuarter()

    def dispense(self):
        self.gumballMachine.launchOneGumball()
        self.gumballMachine.launchOneGumball()
        if self.gumballMachine.getGumballNumber() > 0:
            self.gumballMachine.setState(GumballStateNoQuarter(self.gumballMachine))
        else:
            self.gumballMachine.setState(GumballStateSoldOut(self.gumballMachine))


class GumballStateSoldOut(GumballState):

    def __init__(self, gumballMachine):
        super(GumballStateSoldOut, self).__init__("SoldOut", gumballMachine)

    def insertQuarter(self):
        print "# Gumball machine is sold-out."
        self.gumballMachine.returnQuarter()

    def refill(self):
        if self.gumballMachine.getGumballNumber() > 0:
            self.gumballMachine.setState(GumballStateNoQuarter(self.gumballMachine))


class GumballMachine(object):

    def __init__(self, initGumballCount = 5):
        self.gumballCount = initGumballCount
        if self.gumballCount > 0:
            self.currState = GumballStateNoQuarter(self)
        else:
            self.currState = GumballStateSoldOut(self)

    def insertQuarter(self):
        print "* Insert a quarter."
        self.currState.insertQuarter()

    def ejectQuarter(self):
        print "* Eject quarter."
        self.currState.ejectQuarter()

    def turnCrank(self):
        print "* Turn crank."
        self.currState.turnCrank()

    def dispense(self):
        self.currState.dispense()

    def refill(self, gumballNumber):
        print "* Refill the gumball machine"
        self.gumballCount += gumballNumber
        self.currState.refill()

    # 

    def setState(self, state):
        assert isinstance(state, GumballState)
        self.currState = state

    def returnQuarter(self):
        print "# Return the inserted quarter."

    def isLuckyCustomer(self):
        if self.gumballCount >= 2 and random.randint(0, 9) == 0:
            return True
        else:
            return False

    def getGumballNumber(self):
        return self.gumballCount

    def launchOneGumball(self):
        if self.gumballCount > 0:        
            print "# Prepare one gambull, 3, 2, 1, launch!"
            self.gumballCount -= 1
        else:
            raise Exception("Gumball machine out of gumball.")

    def __str__(self):
        return "# Gumball Machine, gumball count: {}, current state: {}.".format(self.gumballCount, self.currState)


def Test1():
    gumballMachine = GumballMachine(5)
    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()
    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    print gumballMachine

    gumballMachine.refill(5)
    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print gumballMachine

Test1()