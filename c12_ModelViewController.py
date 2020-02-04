# The Model View Controller pattern.

# BeatModel, which composits BeatApplication and Observer, is the simulator of the beats generator.
# DJView, is the display to visualize the beats, and accept input by controls (power of/off, bpm increase/decrease, volume increase/decrease.)
# Controller, translate the input to DJView to actions on the BeatModel.
# DJView is observer of BeatModel.

# Observer interface.

class Observer(object):
    def update(self, subject, id):
        raise Exception("Observer.update not implemented.")


class Observable(object):
    def __init__(self, subject):
        self.subject = subject
        self.observers = {} # {id : [Observer]}

    def registerObserver(self, observer, id):
        assert isinstance(observer, Observer)
        if not id in self.observers:
            self.observers[id] = []
        self.observers[id].append(observer)

    def notifyAllObservers(self, id):
        for observer in self.observers[id]:
            observer.update(self.subject, id)


# The beat application interface.

class BeatApplication(object):

    UPDATE_POWER = "update_power"

    INIT_BPM = 80
    MAX_BPM = 200
    UPDATE_BPM = "update_bpm"

    INIT_VOLUME = 5
    MAX_VOLUME = 10        
    UPDATE_VOLUME = "update_volume"

    def __init__(self):
        self.bpm = BeatApplication.INIT_BPM
        self.volume = BeatApplication.INIT_VOLUME
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def isTurnedOn(self):
        return self.on

    def clamp(self, v, a, b):
        v = max(v, a)
        v = min(v, b)
        return v

    def setBPM(self, bpm):
        if self.on:
            bpm = self.clamp(bpm, 0, BeatApplication.MAX_BPM)
            self.bpm = int(bpm)

    def getBPM(self):
        return self.bpm

    def setVolume(self, volume):
        if self.on:
            volume = self.clamp(volume, 0, BeatApplication.MAX_VOLUME)
            self.volume = int(volume)

    def getVolume(self):
        return self.volume


# Beat model, composite Observer and BeatApplication

class BeatModel(object):
    # Composite the observer and beat application

    def __init__(self):
        self.beatApp = BeatApplication()
        self.observable = Observable(self.beatApp)

    def turnOn(self):
        self.beatApp.turnOn()
        self.observable.notifyAllObservers(BeatApplication.UPDATE_POWER)

    def turnOff(self):
        self.beatApp.turnOff()
        self.observable.notifyAllObservers(BeatApplication.UPDATE_POWER)

    def isTurnedOn(self):
        return self.beatApp.isTurnedOn()

    def setBPM(self, bpm):
        self.beatApp.setBPM(bpm)
        self.observable.notifyAllObservers(BeatApplication.UPDATE_BPM)

    def getBPM(self):
        return self.beatApp.getBPM()

    def setVolume(self, volume):
        self.beatApp.setVolume(volume)
        self.observable.notifyAllObservers(BeatApplication.UPDATE_VOLUME)

    def getVolume(self):
        return self.beatApp.getVolume()

    def registerPowerObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observable.registerObserver(observer, BeatApplication.UPDATE_POWER)

    def registerBPMObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observable.registerObserver(observer, BeatApplication.UPDATE_BPM)

    def registerVolumeObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observable.registerObserver(observer, BeatApplication.UPDATE_VOLUME)


# The controller interface

class BeatControllerInterface(object):

    def turnBeatOn(self):
        raise Exception("BeatControllerInterface.turnBeatOn not implemented.")

    def turnBeatOff(self):
        raise Exception("BeatControllerInterface.turnBeatOff not implemented.")

    def increaseBPM(self):
        raise Exception("BeatControllerInterface.increaseBPM not implemented.")

    def decreaseBPM(self):
        raise Exception("BeatControllerInterface.decreaseBPM not implemented.")

    def increaseVolume(self):
        raise Exception("BeatControllerInterface.increaseVolume not implemented.")

    def decreaseVolume(self):
        raise Exception("BeatControllerInterface.decreaseVolume not implemented.")


# The View
# Adapt strategy pattern, delegate real actions to ControllerInterface.

class DJView(Observer):

    def __init__(self, controller):
        assert isinstance(controller, BeatControllerInterface)
        self.controller = controller

    def display(self, info):
        print "[DJView] {}".format(info)

    def update(self, subject, id):
        # Required by the BeatObserver interface
        assert isinstance(subject, BeatApplication)

        if id == BeatApplication.UPDATE_POWER:
            if subject.isTurnedOn():
                self.display("Power state: ON.")
                self.display("BPM: {}.".format(subject.getBPM()))
                self.display("Volume: {}.".format(subject.getVolume()))
            else:
                self.display("Power state: OFF.")
        elif id == BeatApplication.UPDATE_BPM:
            if subject.isTurnedOn():            
                self.display("BPM: {}.".format(subject.getBPM()))
        elif id == BeatApplication.UPDATE_VOLUME:
            if subject.isTurnedOn():
                self.display("Volume: {}.".format(subject.getVolume()))

    def run(self):
        if self.controller != None:
            self.display("Start rock and roll.")
            while True:
                input = raw_input("* Input command: ").lower()
                if input == "exit":
                    break
                elif input == "on":
                    self.controller.turnBeatOn()
                elif input == "off":
                    self.controller.turnBeatOff()
                elif input == "bpm+":
                    self.controller.increaseBPM()
                elif input == "bpm-":
                    self.controller.decreaseBPM()
                elif input == "volume+":
                    self.controller.increaseVolume()
                elif input == "volume-":
                    self.controller.decreaseVolume()
                else:
                    self.display("Unknown command.")
            self.display("See ya.")
        else:
            self.display("No controller, can not run.")


# The concrete controller

class BeatController(BeatControllerInterface):

    def __init__(self, beatModel):
        assert isinstance(beatModel, BeatModel)
        self.beatModel = beatModel

    def turnBeatOn(self):
        self.beatModel.turnOn()

    def turnBeatOff(self):
        self.beatModel.turnOff()

    def increaseBPM(self):
        bpm = self.beatModel.getBPM()
        self.beatModel.setBPM(bpm + 10)

    def decreaseBPM(self):
        bpm = self.beatModel.getBPM()
        self.beatModel.setBPM(bpm - 10)

    def increaseVolume(self):
        volume = self.beatModel.getVolume()
        self.beatModel.setVolume(volume + 1)

    def decreaseVolume(self):
        volume = self.beatModel.getVolume()
        self.beatModel.setVolume(volume - 1)


# Initialize the Model, View, Controller

def CreateBeat():
    model = BeatModel()
    controller = BeatController(model)
    view = DJView(controller)

    model.registerPowerObserver(view)
    model.registerBPMObserver(view)
    model.registerVolumeObserver(view)

    return (model, view, controller)


# Test
if __name__ == "__main__":
    model, view, controller = CreateBeat()
    view.run()