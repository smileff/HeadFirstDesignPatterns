# Command pattern

# The interface of a command.
# A command object encapsulate a receiver and its action, decouping invoker from the concrete action.
class Command(object):
    def execute(self):
        assert False
        
    def undo(self):
        assert False

    def description(self):
        return "Command"


class EmptyCommand(Command):
    # Just no nothing.

    def execute(self):        
        pass

    def undo(self):
        pass


# A concrete invoker class
class RemoteControl(object):

    def __init__(self):
        super(RemoteControl, self).__init__()
        self.commandNum = 8
        self.onCommandList = [EmptyCommand for i in range(self.commandNum)]
        self.offCommandList = [EmptyCommand for i in range(self.commandNum)]

        self.commandHistoryCapcity = 10
        self.commandHistory = []


    def addCommandToHistory(self, command):
        # If the history stack is full, remove the earliest one.
        if len(self.commandHistory) >= self.commandHistoryCapcity:
            self.commandHistory = self.commandHistory[1:]
        self.commandHistory.append(command)

    def setCommand(self, index, onCommand, offCommand):
        assert index >= 0 and index < self.commandNum
        assert isinstance(onCommand, Command)
        assert isinstance(offCommand, Command)

        self.onCommandList[index] = onCommand
        self.offCommandList[index] = offCommand

    def onCommandPressed(self, index):
        assert index >= 0 and index < self.commandNum
        self.onCommandList[index].execute()
        self.addCommandToHistory(self.onCommandList[index])

    def offCommandPressed(self, index):
        assert index >= 0 and index < self.commandNum
        self.offCommandList[index].execute()
        self.addCommandToHistory(self.offCommandList[index])

    def undo(self):
        if len(self.commandHistory) > 0:
            command = self.commandHistory.pop()
            command.undo()
        else:
            print "[RemoteControl] no more command history."

    def report(self):
        print "Remote control system"
        assert len(self.onCommandList) == len(self.offCommandList)
        for i in range(len(self.onCommandList)):
            print "slot {}, on: {}, off: {}".format(i, self.onCommandList[i].description(),  self.offCommandList[i].description())

        
# A use case

class Light(object):
    def __init__(self, location):
        super(Light, self).__init__()
        assert isinstance(location, str)
        self.location = location

    def on(self):
        print "{} light is on".format(self.location)

    def off(self):
        print "{} light is off".format(self.location)

    def getLocation(self):
        return self.location


class LightOnCommand(Command):

    def __init__(self, light):
        super(LightOnCommand, self).__init__()
        assert isinstance(light, Light)
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()        # Feel a little silly.

    def description(self):
        return super(LightOnCommand, self).description() + ".LightOn." + self.light.getLocation()

        
class LightOffCommand(Command):

    def __init__(self, light):
        super(LightOffCommand, self).__init__()
        assert isinstance(light, Light)
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

    def description(self):
        return super(LightOffCommand, self).description() + ".LightOff." + self.light.getLocation()


class CeilingFan(object):

    TURN_OFF = 0
    SLOW_SPEED = 1
    MIDDLE_SPEED = 2
    HIGH_SPEED = 3

    def __init__(self, location):
        super(CeilingFan, self).__init__()
        assert isinstance(location, str)
        self.location = location
        self.state = CeilingFan.TURN_OFF
        
    def set(self, speed):
        if speed == CeilingFan.TURN_OFF:
            print "{} fan is turned off".format(self.location)
        elif speed == CeilingFan.SLOW_SPEED:
            print "{} fan is set to slow speed".format(self.location)
        elif speed == CeilingFan.MIDDLE_SPEED:
            print "{} fan is set to middle speed".format(self.location)
        elif speed == CeilingFan.HIGH_SPEED:
            print "{} fan is set to high speed".format(self.location)
        else:
            assert False

    def getState(self):
        return self.state

    def getLocation(self):
        return self.location


class CeilingFanCommand(Command):

    def __init__(self, fan, workState):
        assert isinstance(fan, CeilingFan)        
        self.fan = fan
        self.work_state = workState
        self.prev_state = self.fan.getState()

    def execute(self):
        self.prev_state = self.fan.getState()
        self.fan.set(self.work_state)

    def undo(self):
        temp = self.fan.getState()
        self.fan.set(self.prev_state)
        self.prev_state = temp


class CeilingFanHighCommand(CeilingFanCommand):
    def __init__(self, fan):
        super(CeilingFanHighCommand, self).__init__(fan, CeilingFan.HIGH_SPEED)

    def description(self):
        return super(CeilingFanHighCommand, self).description() + ".HighSpeed." + self.fan.getLocation()


class CeilingFanMiddleCommand(CeilingFanCommand):
    def __init__(self, fan):
        super(CeilingFanMiddleCommand, self).__init__(fan, CeilingFan.MIDDLE_SPEED)

    def description(self):
        return super(CeilingFanMiddleCommand, self).description() + ".MiddleSpeed." + self.fan.getLocation()


class CeilingFanLowCommand(CeilingFanCommand):
    def __init__(self, fan):
        super(CeilingFanLowCommand, self).__init__(fan, CeilingFan.SLOW_SPEED)

    def description(self):
        return super(CeilingFanLowCommand, self).description() + ".LowSpeed." + self.fan.getLocation()


class CeilingFanOffCommand(CeilingFanCommand):
    def __init__(self, fan):
        super(CeilingFanOffCommand, self).__init__(fan, CeilingFan.TURN_OFF)

    def description(self):
        return super(CeilingFanOffCommand, self).description() + ".Off." + self.fan.getLocation()


# 

guestRoomLight = Light("guest room")
guestRoomLightOnCommand = LightOnCommand(guestRoomLight)
guestRoomLightOffCommand = LightOffCommand(guestRoomLight)

kitchLight = Light("kitch")
kitchLightOnCommand = LightOnCommand(kitchLight)
kitchLightOffCommand = LightOffCommand(kitchLight)

guestRoomFan = CeilingFan("guest room")
guestRoomFanHighCommand = CeilingFanHighCommand(guestRoomFan)
guestRoomFanMiddleCommand = CeilingFanMiddleCommand(guestRoomFan)
guestRoomFanLowCommand = CeilingFanLowCommand(guestRoomFan)
guestRoomFanOffCommand = CeilingFanOffCommand(guestRoomFan)

kitchFan = CeilingFan("kitch")
kitchFanHighCommand = CeilingFanHighCommand(kitchFan)
kitchFanMiddleCommand = CeilingFanMiddleCommand(kitchFan)
kitchFanLowCommand = CeilingFanLowCommand(kitchFan)
kitchFanOffCommand = CeilingFanOffCommand(kitchFan)

# The remote control doesn't need to know the detail of the command.

remoteControl = RemoteControl()

remoteControl.setCommand(0, guestRoomLightOnCommand, guestRoomLightOffCommand)
remoteControl.setCommand(1, kitchLightOnCommand, kitchLightOffCommand)

remoteControl.setCommand(2, guestRoomFanHighCommand, guestRoomFanOffCommand)
remoteControl.setCommand(3, guestRoomFanMiddleCommand, guestRoomFanOffCommand)
remoteControl.setCommand(4, guestRoomFanLowCommand, guestRoomFanOffCommand)

remoteControl.setCommand(5, kitchFanHighCommand, kitchFanOffCommand)
remoteControl.setCommand(6, kitchFanMiddleCommand, kitchFanOffCommand)
remoteControl.setCommand(7, kitchFanLowCommand, kitchFanOffCommand)

remoteControl.report()

remoteControl.onCommandPressed(0)
remoteControl.offCommandPressed(0)
remoteControl.onCommandPressed(1)
remoteControl.onCommandPressed(2)

for i in range(10):
    remoteControl.undo()

remoteControl.onCommandPressed(4)
remoteControl.onCommandPressed(5)
remoteControl.onCommandPressed(6)
remoteControl.onCommandPressed(7)

remoteControl.offCommandPressed(4)
remoteControl.offCommandPressed(5)
remoteControl.offCommandPressed(6)
remoteControl.offCommandPressed(7)