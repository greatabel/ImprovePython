from mycolor import show

class Statement:

    def header_string(self):
        pass

    def each_rental_string(self):
        pass

    def footer_string(self):
        pass

    def go(self):
        self.header_string()
        self.each_rental_string()
        self.footer_string()

class HtmlStatement(Statement):

    def header_string(self):
        print("<head> hello </head>")

    def each_rental_string(self):
        print("<br/>test<br/><hr>")

    def footer_string(self):
        print("<p> You owe it </p><br/>")

class TextStatement(Statement):

    def header_string(self):
        print( "Hello")

    def each_rental_string(self):
        print( "\t test \t")

    def footer_string(self):
        print( "You owe it")

h = Statement()
if 'want to html state':
    h = HtmlStatement()

h.go()
if 'wanto to text state':
    h = TextStatement()
h.go()
