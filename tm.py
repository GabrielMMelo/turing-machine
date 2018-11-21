from reader import Reader
import sys

class Tm():
    def __init__(self, filename):
       reader = Reader(filename)
       self.Q, self.E, self.r, self.S, self.q0, self.input = reader.read_file()
       self.transitions = {}
       for state in self.Q:
           self.transitions[state] = {}
           for trans in self.S:
               if trans[0] == state:
                   self.transitions[state][trans[1]] = trans[2:len(trans)-1]
       self.actual = self.q0
       self.position = 0
       self.refresh_tape() 

    def __str__(self):
        return self.tape

    def refresh_tape(self):
        self.tape = "".join([self.input[:self.position], "{", self.actual, "}", self.input[self.position:len(self.input)]])

    def compute(self):
        # Lendo o próximo simbolo, vai para algum lugar?    
        transition = self.get_transition()   
        self.write_next(transition[1])
        self.actual = transition[0]
        if transition[2] == 'R':
            self.move_right()
        else:
            self.move_left()

    def get_transition(self):
        return self.transitions[self.actual][self.get_next()]

    def move_left(self):
        try: 
            self.position -= 1
            if self.position < 0:
                raise Exception("Movimento inválido!")
            self.refresh_tape() 
        except Exception as error:
            print('Erro encontrado: ' + repr(error)) 
            sys.exit(1)

    def write_next(self, value):
        tape_list = list(self.tape)
        tape_list[self.tape.find('}')+1] = value
        self.tape = "".join(tape_list)

    def move_right(self):
        self.position += 1
        self.refresh_tape() 

    def get_next(self):
        return self.tape[self.tape.find('}')+1]

tm = Tm("entrada.txt")
while True:
    print(tm)
    print("position ", tm.position)
    tm.compute()
