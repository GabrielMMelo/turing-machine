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

    # Funcao que printa o estado atual e a cabeca de leitura na fita
    def refresh_tape(self):
        print(self.input[:self.position] + "{" + self.actual + "}" + self.input[self.position:])

    # Funcao que executa a maquina de turing, movendo a cabeca de leitura 
    def compute(self):
        # Lendo o próximo simbolo, vai para algum lugar?
        self.refresh_tape()   
        transition = self.get_transition()   
        self.write_actual(transition[1])
        self.actual = transition[0]
        if transition[2] == 'R':
            self.move_right()
        else:
            self.move_left()

    # Funcao que pega a transicao que o estado atual ira realizar
    def get_transition(self):
        return self.transitions[self.actual][self.read_actual()]

    # Funcao que move a cabeca de leitura para esquerda
    def move_left(self):
        try: 
            self.position -= 1
            if self.position < 0:
                raise Exception("Movimento inválido!")
        except Exception as error:
            print('Erro encontrado: ' + repr(error)) 
            sys.exit(1)

    # Funcao que move a cabeca de leitura para direita
    def move_right(self):
        self.position += 1

    # Funcao que faz a escrita no local aonde esta a cabeca de leitura
    def write_actual(self, value):
        input_list = list(self.input)
        input_list[self.position] = value
        self.input = "".join(input_list)

    # Funcao que faz a leitura no local aonde esta a cabeca de leitura
    def read_actual(self):
        return self.input[self.position]

tm = Tm("entrada.txt")
while True:
    try:
        tm.compute()
    except KeyError:
        break