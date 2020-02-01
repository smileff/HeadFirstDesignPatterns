# The proxy pattern

# I use the GumballMachine class in c10_StatePattern.py
from c10_StatePattern import GumballMachine

# Mimic the remote proxy
class GumballMachineServer(object):

    instance = None

    @staticmethod
    def getInstance():
        if GumballMachineServer.instance == None:
            GumballMachineServer.instance = GumballMachineServer()
        return GumballMachineServer.instance

    def __init__(self):
        self.machineStock = {}

    def addMachine(self, machineName, machine):
        self.machineStock[machineName] = machine

    def getMachineGumballNumber(self, machineName):
        machine = self.machineStock[machineName]
        return machine.getGumballNumber()

    def getMachineState(self, machineName):
        machine = self.machineStock[machineName]
        return machine.getState().getName()


# The proxy called locally. 
# It access the control of the real GumballMachine: through the server.
class GumballMachineProxy(object):

    def __init__(self, machineName):
        self.machineName = machineName

    def getName(self):
        return self.machineName

    def getState(self):
        server = GumballMachineServer.getInstance()
        return server.getMachineState(self.machineName)

    def getGumballNumber(self):
        server = GumballMachineServer.getInstance()
        return server.getMachineGumballNumber(self.machineName)


# The client: GumballMonitor
class GumballMachineMonitor(object):

    def __init__(self, machineName):
        self.gumballMachineProxy = GumballMachineProxy(machineName)

    def report(self):
        print "Gumball Machine: {}".format(self.gumballMachineProxy.getName())
        print "Current inventory: {} gumballs".format(self.gumballMachineProxy.getGumballNumber())
        print "Current state: {}".format(self.gumballMachineProxy.getState())


# Test case

if __name__ == "__main__":

    machineServer = GumballMachineServer.getInstance()

    machine1 = GumballMachine(5)
    machineServer.addMachine("Machine1", machine1)

    machine2 = GumballMachine(5)
    machineServer.addMachine("Machine2", machine2)

    machine1.insertQuarter()
    machine1.turnCrank()

    machine2.insertQuarter()
    machine2.turnCrank()

    machine2.insertQuarter()
    machine2.turnCrank()

    machineMonitor1 = GumballMachineMonitor("Machine1")
    machineMonitor1.report()

    machineMonitor2 = GumballMachineMonitor("Machine2")
    machineMonitor2.report()