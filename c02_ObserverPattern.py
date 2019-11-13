
# The Subject interface

class Subject(object):
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer, updateImmediately = True):
        assert isinstance(observer, Observer)
        if not observer in self.observers:
            self.observers.append(observer)

            if updateImmediately:
                observer.update(self)

    def unregisterObserver(self, observer):
        assert isinstance(observer, Observer)
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self):
        # Assert observer has an Update(Subject) methods.
        for observer in self.observers:
            observer.update(self)

# The Observer interface
    
class Observer(object):
    def update(self, subject):
        assert isinstance(subject, Subject)
        # Actual this has a problem: the real subject is a subclass of Subject, 
        # But in Subject we can't define the real pull methods to obtain the needed info.


# The weather data demo

class WeatherData(Subject):

    def __init__(self):
        super(WeatherData, self).__init__()
        self.temperature = "\"uninitialized\""
        self.humidity = "\"uninitialized\""
        self.pressure = "\"uninitialized\""

    def SetMeasurement(self, temperature, humidity, pressure):
        print "[WeatherData] set measurement, temperature: {}, humidity: {}, pressure: {}.".format(temperature, humidity, pressure)
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notifyObservers()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

    
class Display(object):
    def display(self):
        pass

class TemperatureDisplay(Observer, Display):

    def __init__(self):
        self.temperature = "uninitialized"

    def display(self):
        print "[TemperatureDisplay] current temperature: {} degrees.".format(self.temperature)

    def update(self, subject):
        assert isinstance(subject, WeatherData)
        self.temperature = subject.getTemperature()
        self.display()

class HumidityDisplay(Observer, Display):
    def __init__(self):
        self.humidity = "uninitialized"

    def display(self):
        print "[HumidityDisplay] current humidity: {}%.".format(self.humidity)

    def update(self, subject):
        assert isinstance(subject, WeatherData)
        self.humidity = subject.getHumidity()
        self.display()

class PressureDisplay(Observer, Display):
    def __init__(self):
        self.pressure = "uninitialized"

    def display(self):
        print "[PressureDisplay] current pressure: {}.".format(self.pressure)

    def update(self, subject):
        assert isinstance(subject, WeatherData)
        self.pressure = subject.getPressure()
        self.display()

    
# Test

weatherData = WeatherData()

temperatureDisplay = TemperatureDisplay()
weatherData.registerObserver(temperatureDisplay)

humidityDisplay = HumidityDisplay()
weatherData.registerObserver(humidityDisplay)

pressureDisplay = PressureDisplay()
weatherData.registerObserver(pressureDisplay)

print ""
weatherData.SetMeasurement(temperature = 100.0, humidity = 23.5, pressure = 10.5)

print ""
weatherData.SetMeasurement(temperature = 50.0, humidity = 50.3, pressure = 2.3)

print ""
weatherData.SetMeasurement(temperature = 15.0, humidity = 76.2, pressure = 0.7)
