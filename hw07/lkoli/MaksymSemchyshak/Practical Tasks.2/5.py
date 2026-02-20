# V. Reversing Words in a String

def reverse(st):
     words = st.split(' ')

     reverse = words[::-1]

     return ' '.join(reverse)

print(reverse('Hello word'))