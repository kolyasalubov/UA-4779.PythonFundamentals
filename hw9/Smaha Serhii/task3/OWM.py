from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def get_weather(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')
    info = (
        f"City:        {city}\n"
        f"Status:      {w.detailed_status}\n"
        f"Temperature: {temp['temp']:.1f} \u00b0C\n"
        f"Humidity:    {w.humidity} %\n"
        f"Wind:        {w.wind()['speed']} m/s\n"
        f"Clouds:      {w.clouds} %"
    )
    return info


if __name__ == '__main__':
    print(get_weather('London,GB'))
