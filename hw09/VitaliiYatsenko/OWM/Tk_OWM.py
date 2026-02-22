import tkinter as tk
from tkinter import font
from OWM import mgr

HEIGHT = 550
WIDTH = 750


root = tk.Tk()


def clear(event):
    if entry_field.get() == "Enter loacation as example(Kyiv)":
        entry_field.delete(0, tk.END)


def get_weather():
    try:
        coord = entry_field.get()
        observation = mgr.weather_at_place(coord)
        w = observation.weather
        label.config(text=f'Location:{coord}\n{w.detailed_status.title()}\n Temp: {round(w.temperature('celsius')['temp'])}°C')
    except:
        label.config(text='Oops, the specified coordinates were not found.')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



entry_field = tk.Entry(frame, font="TkSmallCaptionsFont")
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.insert(0,"Enter loacation as example(Kyiv)")

entry_field.bind("<FocusIn>", clear)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text='', font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()