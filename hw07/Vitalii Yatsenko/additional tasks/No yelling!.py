def filter_words(st):
    res = st.split()
    l = ' '.join(res)
    s = l.replace(' .', '.')
    return s.capitalize()
print(filter_words(' This    will    not    pass .'))