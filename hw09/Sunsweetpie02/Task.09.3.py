import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    if not city:
        label['text'] = "Enter the name of the city:"
        return

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        status = f"Condition: {w.detailed_status}\n"
        temp = w.temperature('celsius')
        temperature = f"Temperature: {temp['temp']}°C (min: {temp['temp_min']}°C, max: {temp['temp_max']}°C)\n"
        humidity = f"humidity: {w.humidity}%\n"
        wind = w.wind()
        wind_text = f"Wind: {wind.get('speed',0)} m/s, Angle: {wind.get('deg',0)}°\n"
        clouds = f"Clouds: {w.clouds}%\n"
        rain = f"Rain: {w.rain if w.rain else 'No'}\n"
        
        label['text'] = status + temperature + humidity + wind_text + clouds + rain
    except Exception as e:
        label['text'] = f"Unable to retrieve information about '{city}'"

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()


