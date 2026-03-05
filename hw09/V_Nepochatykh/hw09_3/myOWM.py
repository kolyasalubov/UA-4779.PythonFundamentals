from pyowm import OWM
from tkowm_config import KEY

owm = OWM(KEY)
mgr = owm.weather_manager()


def raw_weather (location: str) -> dict:

    observation = mgr.weather_at_place(location)
    w = observation.weather
    weather_dict = {}
    weather_dict.update({'dstat': w.detailed_status})         # 'clouds'
    weather_dict.update({'wind': w.wind()})                  # {'speed': 4.6, 'deg': 330}
    weather_dict.update({'humidity': w.humidity})                # 87
    weather_dict.update({'temp': w.temperature('celsius')})  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    weather_dict.update({'rain': w.rain})                    # {}
    weather_dict.update({'heatind': w.heat_index})              # None
    weather_dict.update({'clouds': w.clouds})                  # 75
    return weather_dict
#print (raw_weather('Lviv'))



