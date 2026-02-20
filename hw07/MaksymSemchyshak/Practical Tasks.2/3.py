# III. No yelling!


def filter_words(st):
    words = st.split()

    cleaned_text = ' '.join(words)

    return cleaned_text.capitalize()

input_str = "WOW this is REALLY          amazing"
result = filter_words(input_str)

print(result)