from reader import Reader
import sys

class Tm():
    def __init__(self, filename):
       reader = Reader(filename)
       self.Q, self.E, self.r, self.S, self.q0, self.input = reader.read_file()
       self.actual = self.q0
       self.position = 0
       self.refresh_tape() 

    def __str__(self):
        return self.tape

    def refresh_tape(self):
        self.tape = "".join([self.input[:self.position], "{", self.actual, "}", self.input[self.position:len(self.input)]])

    def compute(self):
        # Lendo o próximo simbolo, vai para algum lugar?    
        pass        

    def move_left(self):
        try: 
            self.position -= 1
            if self.position < 0:
                raise Exception("Movimento inválido!")
            self.refresh_tape() 
        except Exception as error:
            print('Erro encontrado: ' + repr(error)) 
            sys.exit(1)

    def move_right(self):
        self.position += 1
        self.refresh_tape() 

    def get_next(self):
        return tape[tape.find('}')+1]

tm = Tm("entrada.txt")
tm.move_right()
tm.move_left()
print (tm.S)
