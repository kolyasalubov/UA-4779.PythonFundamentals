import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

HEIGHT = 350
WIDTH = 450


def get_weather(entry):
    location = entry.get()
    if not location:
        label.config(text="Please enter a location!", bg="gold")
        return

    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(location)
        w = observation.weather

        temp_data = w.temperature('celsius')
        wind_data = w.wind()

        weather_info = (
            f"Status: {w.detailed_status.capitalize()}\n"
            f"Temperature: {temp_data['temp']:.1f}°C\n"
            f"Feels like: {temp_data.get('feels_like', 'N/A')}°C\n"
            f"Min/Max: {temp_data['temp_min']:.1f}°C / {temp_data['temp_max']:.1f}°C\n"
            f"Humidity: {w.humidity}%\n"
            f"Wind speed: {wind_data.get('speed', 'N/A')} m/s\n"
            f"Clouds: {w.clouds}%\n"
            f"Rain: {w.rain if w.rain else 'No rain'}"
        )

        label.config(text=weather_info, bg="light yellow", anchor='w', justify='left')

    except Exception as e:
        label.config(text=f"Error: location not found!\n'{location}'", bg="tomato")


root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.insert(0, "London,GB")  # placeholder

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 11), bg='gold', anchor='w', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()