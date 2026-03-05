import tkinter as tk
from tkinter import font
from myOWM import raw_weather

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def get_weather (location: str):
    def wind_direction (deg: int) -> str:
        w_directions = ('North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West')
        index = round((deg+ 22.5) /45)%8
        return w_directions[index]
    
    raw = raw_weather(location)
    text_weather = (f"The weather for {location} is: \n  "
                    f"Sky: {raw['dstat'].capitalize()} \n"
                    f"Temperature: {raw['temp']['temp']} °C \n"
                    f"Feels like: {raw['temp']['feels_like']} °C \n"
                    f"Wind speed: {raw['wind']['speed']} m/s," 
                    f" direction: {wind_direction(raw['wind']['deg'])}" 
    )
    label.config(text=text_weather)                  


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get())
)
                   
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

