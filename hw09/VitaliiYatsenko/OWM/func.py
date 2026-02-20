from Tk_OWM import entry_field
from OWM import owm
from OWM import mgr

def get_weather():
    coord = entry_field.get() #data from field
    observation = mgr.weather_at_place(coord)
    w = observation.weather
    print(w.detailed_status)


    
