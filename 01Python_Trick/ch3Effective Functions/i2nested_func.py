def speak(text):
    def whisper(t):
        return t.lower() + '...'

    return '#' + whisper(text) + '#'

print(speak('Hello world'))


def get_speak_func(volume): 
    def whisper(text):
        return text.lower() + '...' 
    def yell(text):
        return text.upper() + '!!!'

    if volume > 0.5:
        return yell 
    else:
        return whisper

print(get_speak_func(1))
print(get_speak_func(0.1))
speak_func = get_speak_func(0.7)
print(speak_func('hello'))

