import sys
from .reader import Reader

class Tm():
    """Classe que representa uma máquina de turing determinística."""

    def __init__(self, filename):
        """
        :param filename: Nome do arquivo de entrada.
        :type filename: str
        """
        reader = Reader(filename)
        self.Q, self.S, self.q0, self.tape = reader.read_file()
        self.transitions = {}
        self.make_transitions()
        self.actual = self.q0
        self.position = 0
        
    def make_transitions(self):
        """Método que cria dicionário de dicionários para armazenamento das transições de cada estado.

        A estrutura é dada no seguinte formato abaixo: 
        
        - { `'estado_1'`: {`'simbolo_leitura_1'`: ('proximo_estado', 'simbolo_escrita', 'direcao'), ...}, ...}
        
        - {'q0': {'B': ('q1', '1', 'R'), ...}, 'q1': {'1', ...}, ... 'qn': { ...}} 
        """

        for state in self.Q:
            self.transitions[state] = {}
            for source, in_symbol, destination, out_symbol, direction, _ in self.S:
                if source == state:
                    self.transitions[state][in_symbol] = [destination, out_symbol, direction]

    def show_tape(self):
        """Método que imprime o estado atual e a configuração da fita."""
        print("".join([self.tape[:self.position], "{", self.actual, "}", \
                self.tape[self.position:]]))

    def compute(self):
        """Método que executa uma computacao na máquina de turing,
            alterando -*ou não*- o estado atual, escrevendo um símbolo e movendo
            a cabeça de leitura para esquerda ou direita.
        """
        self.show_tape()   
        destination, out_symbol, direction = self.get_transition()   
        self.write_actual(out_symbol)
        self.actual = destination
        if direction == 'R':
            self.move_right()
        else:
            self.move_left()

    def get_transition(self):
        """Método que retorna a transição que o estado atual irá realizar lendo o símbolo atual.
        
        :return: (*List*) Lista de ``str`` contendo uma transição no formato lista['``qi``', '``ri``', '``D``'], onde:

        - ``qi``: Estado destino;

        - ``ri``: Símbolo a ser escrito;

        - ``D``: Direção a mover a cabeça de leitura (*L* ou *R*)
        """

        return self.transitions[self.actual][self.read_actual()]

    def move_left(self):
        """Método que move a cabeça de leitura para esquerda."""
        try: 
            self.position -= 1
            if self.position == -1:
                raise Exception("Movimento inválido!")
        except Exception as error:
            sys.exit('Erro encontrado: ' + str(error))

    def move_right(self):
        """Método que move a cabeça de leitura para direita."""
        self.position += 1
        if self.position == len(self.tape):
            self.tape = "".join([self.tape, 'B'])

    def write_actual(self, value):
        """Método que realiza a escrita na posição onde a cabeça de leitura se encontra.
       
        :param value: Valor a ser escrito na posição atual
        :type value: str
        """
        input_list = list(self.tape)
        input_list[self.position] = value
        self.tape = "".join(input_list)

    def read_actual(self):
        """Método que retorna o símbolo da posição onde está a cabeça de leitura.
        
        :return: (*str*) Símbolo da fita na posição que a cabeça de leitura se encontra.
        """

        return self.tape[self.position]
