import sys
from typing import NoReturn, List
from reader import Reader

class Tm():
    """Classe que representa uma maquina de turing deterministica"""

    def __init__(self, filename: str) -> None:
        reader = Reader(filename)
        self.Q, self.S, self.q0, self.tape = reader.read_file()
        self.transitions = {}
        self.make_transitions()
        self.actual = self.q0
        self.position = 0
        
    def make_transitions(self):
        """Metodo que cria dicionario de dicionarios para armazenamento das transições de cada estado.

        A estrutura é dada no seguinte formato: 
        { 'vertice_1': {'simbolo_leitura_1': ('proximo_estado', 'simbolo_escrita', 'direcao'), ...}, ...}
        {'q0': {'B': ('q1', '1', 'R'), ...}, 'q1': {'1', ...}, ... 'qn': { ...}} 
        """

        for state in self.Q:
            self.transitions[state] = {}
            for source, in_symbol, destination, out_symbol, direction, _ in self.S:
                if source == state:
                    self.transitions[state][in_symbol] = [destination, out_symbol, direction]

    def show_tape(self) -> NoReturn:
        """Metodo que imprime o estado atual e a configuracao da fita"""
        print("".join([self.tape[:self.position], "{", self.actual, "}", \
                self.tape[self.position:]]))

    def compute(self) -> NoReturn:
        """Metodo que executa realiza uma computacao na maquina de turing,
            alterando (ou nao) o estado atual, escrevendo um simbolo e movendo
            a cabeca de leitura
        """
        self.show_tape()   
        destination, out_symbol, direction = self.get_transition()   
        self.write_actual(out_symbol)
        self.actual = destination
        if direction == 'R':
            self.move_right()
        else:
            self.move_left()

    def get_transition(self) -> List[str]:
        """Metodo que retorna a transicao que o estado atual ira realizar"""
        return self.transitions[self.actual][self.read_actual()]

    def move_left(self) -> NoReturn:
        """Metodo que move a cabeca de leitura para esquerda"""
        try: 
            self.position -= 1
            if self.position == -1:
                raise Exception("Movimento inválido!")
        except Exception as error:
            sys.exit('Erro encontrado: ' + str(error))

    def move_right(self) -> NoReturn:
        """Metodo que move a cabeca de leitura para direita"""
        self.position += 1
        if self.position == len(self.tape):
            self.tape = "".join([self.tape, 'B'])

    def write_actual(self, value: str) -> NoReturn:
        """Metodo que realiza a escrita na posicao onde a cabeca de leitura se encontra"""
        input_list = list(self.tape)
        input_list[self.position] = value
        self.tape = "".join(input_list)

    def read_actual(self) -> str:
        """Metodo que faz a leitura no local aonde esta a cabeca de leitura"""
        return self.tape[self.position]