from reader import Reader
import sys

class Tm():
    def __init__(self, filename):
       reader = Reader(filename)
       self.Q, self.E, self.r, self.S, self.q0, self.input = reader.read_file()
       self.actual = self.q0
       self.position = 0
       self.refresh_tape() 

    def refresh_tape(self):
        self.tape = self.input[:self.position] + "{" + self.actual + "}" + self.input[self.position:len(self.input)]

    def compute(self):
        pass        

    def moveLeft(self):
        try: 
            self.position -= 1
            if self.position < 0:
                raise Exception("Movimento inválido!")
            self.refresh_tape() 
        except Exception as error:
            print('Erro encontrado: ' + repr(error)) 
            sys.exit(1)

    def moveRight(self):
        self.position += 1
        self.refresh_tape() 

    def __str__(self):
        return self.tape

tm = Tm("entrada.txt")
tm.moveRight()
tm.moveLeft()
print (tm)
