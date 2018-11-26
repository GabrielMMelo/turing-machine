import sys
import re as regex
from typing import Tuple, List
from .patterns import * 

class Reader():
    """Classe para leitura e validacao do arquivo de entrada."""

    def __init__(self, filename: str) -> None:
        """
        :param filename: Nome do arquivo de entrada.
        :type filename: str
        """
        self.file = filename
        self.line_counter = 0

    def read_file(self) -> Tuple[List[str], List[List[str]], str, str]:
        """Valida, linha por linha, o arquivo de entrada e retorna as estruturas que compoem 
            a maquina de turing mais a entrada.
        """

        with open(self.file) as file:
            self.check_line(self.readline(file), FIRST_LINE)
            Q = self.remove_blank(self.check_line(self.readline(file), Q_LINE))
            E = self.remove_blank(self.check_line(self.readline(file), E_LINE))
            r = self.remove_blank(self.check_line(self.readline(file), r_LINE))
            self.check_line(self.readline(file), FIRST_S_LINE)
            S = []
            S_pattern = create_S_pattern(Q,r)
            while(True):
                S.append(self.check_line(self.readline(file), S_pattern))
                # Se nao for a ultima transicao do arquivo
                if not ',' in S[-1][-1]:
                    break
            self.check_line(self.readline(file), LAST_S_LINE)
            q0 = self.check_line(self.readline(file), q0_LINE)
            self.check_line(self.readline(file), LAST_LINE)
            input = self.check_line(self.readline(file), create_input_pattern(r))
            
        return Q, S, q0[0], input[0]

    def readline(self, file) -> str:
        """*'Sobrescrita'* do metodo de ler linhas para incrementar o contador e auxiliar
            na legibilidade da mensagem de erro.

        :param file: Objeto ``file`` do arquivo de entrada
        :type file: file
        """

        self.line_counter += 1
        return file.readline()
    
    def remove_blank(self, line: str) -> str:
        """Remove espacos em branco e gera uma lista com dos valores separados por virgula.
       
        :param line: Linha do arquivo de entrada
        :type line: str
        """

        return line[0].replace(' ','').split(',')

    def check_line(self, line: str, expected: str) -> str:
        """Valida linha do arquivo de entrada reconhecendo padroes em regex, montados no modulo 
        ``patterns``

        :param line: Linha do arquivo de entrada
        :type line: str

        :param expected: Padrão regexp esperado para uma determinada linha do arquivo de entrada
        :type expected: str
        """

        try:
            match = regex.match(expected, line)
            if not match:
                raise Exception('Formato de arquivo inválido')
            return match.groups()
        except Exception as error:
                sys.exit('Erro encontrado: ' + str(error) + ".\n\nLinha " + str(self.line_counter) \
                        + " do arquivo " + self.file)
