days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def day_of_week(number):
    if number not in days:
        raise ValueError('Number out of range 1-7')
    else:
        return days[number]


def process_input():
    try:
        day = int(input("Enter day of the week: "))
        print(day_of_week(day))
    except ValueError as e:
        print(e)


process_input()
