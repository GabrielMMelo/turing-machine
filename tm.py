from reader import Reader
class Tm():
    def __init__(self, filename):
       reader = Reader(filename)
       self.Q, self.E, self.r, self.S, self.q0, self.input = reader.read_file()
       self.actual = '{' + self.q0 + '}'
       self.tape = self.actual + self.input

    def compute(self):
        pass        

    def __str__(self):
        return self.tape

tm = Tm("entrada.txt")
print (tm)
