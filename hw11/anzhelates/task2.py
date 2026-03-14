days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

def check_input(us_input):
    us_input = int(us_input)
    if us_input not in days:
        raise ValueError("the number must be between 1 and 7")
    return days[us_input]
    
    # or:
    # days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # return days[us_input - 1]

try:
    user_input = input("Enter a number from 1 to 7: ")
    print(check_input(user_input))
except ValueError as e:
    print(f"Error: {e}")