def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!!!'

    if volume > 0.5:
        return yell
    else:
        return whisper

r = get_speak_func('hello world', 0.7)()
print(r)


def make_adder(n): 
    def add(x):
        return x + n 
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4), plus_5(4))