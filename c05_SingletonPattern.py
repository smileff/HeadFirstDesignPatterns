# Singleton pattern

class ChocolateBoiler(object):

    singleInstance = None

    def __init__(self):
        # Should not call initialize publicly
        print "Create ChocolateBoiler instance."
        self.chocolateCounter = 0

    @staticmethod
    def getInstance():
        if ChocolateBoiler.singleInstance == None:
            ChocolateBoiler.singleInstance = ChocolateBoiler()
        return ChocolateBoiler.singleInstance

    def produceChocolate(self):
        self.chocolateCounter += 1

        if self.chocolateCounter == 1:
            print "Produce the {}-st chocoloates.".format(self.chocolateCounter)
        elif self.chocolateCounter == 2:
            print "Produce the {}-nd chocoloates.".format(self.chocolateCounter)
        else:
            print "Produce the {}-th chocoloates.".format(self.chocolateCounter)

    
# Test

ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()
ChocolateBoiler.getInstance().produceChocolate()