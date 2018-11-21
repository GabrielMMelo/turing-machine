from reader import Reader
import sys

class Tm():
    def __init__(self, filename):
       reader = Reader(filename)
       self.Q, self.E, self.r, self.S, self.q0, self.input = reader.read_file()
       self.transitions = {}
       # Dicionario de dicionarios para armazenamento das transições de cada estado.
       # { 'vertice_1': {'simbolo_leitura_1': ('proximo_estado', 'simbolo_escrita', 'direcao'), ...}, ...}
       # {'q0': {'B': ('q1', '1', 'R'), ...}, 'q1': {'1', ...}, ... 'qn': { ...}} 
       for state in self.Q:
           self.transitions[state] = {}
           for source, in_symbol, destination, out_symbol, direction, _ in self.S:
               if source == state:
                   self.transitions[state][in_symbol] = [destination, out_symbol, direction]
       self.actual = self.q0
       self.position = 0

    # Funcao que printa o estado atual e a cabeca de leitura na fita
    def show_tape(self):
        print("".join([self.input[:self.position], "{", self.actual, "}", self.input[self.position:]]))

    # Funcao que executa a maquina de turing, movendo a cabeca de leitura 
    def compute(self):
        self.show_tape()   
        destination, out_symbol, direction = self.get_transition()   
        self.write_actual(out_symbol)
        self.actual = destination
        if direction == 'R':
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
        if self.position == len(self.input):
            self.input = "".join([self.input, 'B'])

    # Funcao que faz a escrita no local aonde esta a cabeca de leitura
    def write_actual(self, value):
        input_list = list(self.input)
        input_list[self.position] = value
        self.input = "".join(input_list)

    # Funcao que faz a leitura no local aonde esta a cabeca de leitura
    def read_actual(self):
        return self.input[self.position]

# TODO: receber arquivo como argumento
tm = Tm("entrada.txt")
while True:
    try:
        tm.compute()
    except KeyError:
        break