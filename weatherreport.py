

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
        elif readings['precipitation'] >= 60 and readings['windSpeedKMPH'] < 50:
            weather = "Rainy Day"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)  # This will fail if bug exists


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    def high_precip_stub():
        return {
            'temperatureInC': 51,
            'precipitation': 70,  # >60
            'humidity': 26,
            'windSpeedKMPH': 40   # <50
        }
    weather = report(high_precip_stub)
    print(weather)
    # Strengthened assert: should predict rain, now matches 'Rainy Day'
    assert("rain" in weather.lower())


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
