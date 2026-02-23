from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city): 
    observation = mgr.weather_at_place(city)
    w = observation.weather
    
    status = w.detailed_status         
    speed_wind = w.wind()['speed']                  
    humidity = w.humidity                
    temperature = w.temperature('celsius')['temp']
    
    final_text = f"Status: {status}\nTemp: {temperature}°C\nWind: {speed_wind} m/s\nHumidity: {humidity}%"
    
    return final_text