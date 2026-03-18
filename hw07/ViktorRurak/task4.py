def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


def distance(x1, y1, x2, y2):
  return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


def filter_words(st):
    st = st.lower()
    st = ' '.join(st.split())
    return st.capitalize()

print(filter_words("FKJDj  PADJF           DPDJFJSPOf   dsfsd"))

print(greet("Johe"))
print(greet("Johnny"))

print(distance(10,10, 20, 20))

