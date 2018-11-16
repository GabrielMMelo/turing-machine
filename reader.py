import re as regex
import constant as const
import sys

class Reader():
    def __init__(self, filename):
        self.file = filename
        self.line_counter = 0

    # Valida, linha por linha, o arquivo de entrada e retorna as estruturas que compoem 
    # a maquina de turing + a entrada
    def read_file(self):
        with open(self.file) as file:
            self.check_line(self.readline(file), const.FIRST_LINE)
            Q = self.remove_blank(self.check_line(self.readline(file), const.Q_LINE))
            E = self.remove_blank(self.check_line(self.readline(file), const.E_LINE))
            r = self.remove_blank(self.check_line(self.readline(file), const.r_LINE))
            self.check_line(self.readline(file), const.FIRST_S_LINE)
            S = []
            S_pattern = const.create_S_pattern(Q,r)
            while(True):
                S.append(self.check_line(self.readline(file), S_pattern))
                # Se nao for a ultima transicao
                if not ',' in S[-1][-1]:
                    break
            self.check_line(self.readline(file), const.LAST_S_LINE)
            q0 = self.check_line(self.readline(file), const.q0_LINE)
            self.check_line(self.readline(file), const.LAST_LINE)
            input = self.check_line(self.readline(file), const.create_input_pattern(r))
            
        return Q, E, r, S, q0[0], input[0]

    # "sobrescrita" do metodo de ler linhas para incrementar o contador e auxiliar
    # na legibilidade da mensagem de erro
    def readline(self, file):
        self.line_counter += 1
        return file.readline()
    
    # Remove espacos em branco e gera uma lista com dos valores separados por virgula
    def remove_blank(self, line):
        return line[0].replace(' ','').split(',')

    # Valida linha do arquivo de entrada reconhecendo padroes em regex, montados em 
    # `constant.py'
    def check_line(self, line, expected):
        try:
            match = regex.match(expected, line)
            if not match:
                raise Exception('Formato de arquivo inválido')
        except Exception as error:
                print('Erro encontrado: ' + repr(error) + ". Linha " + str(self.line_counter) + \
                        " do arquivo " + self.file)
                sys.exit(1)
        return match.groups()
