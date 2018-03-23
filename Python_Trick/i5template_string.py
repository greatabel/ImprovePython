from string import Template

name = 'bob'
errno = 123434
t = Template('Hey, $name!')
print(t.substitute(name=name))

teml_string = "Hey $name, ther is $error error!"
t = Template(teml_string).substitute(name=name, error=hex(errno))
print(t)