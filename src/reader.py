#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re as regex
from .patterns import * 

class Reader():
    """Classe para leitura e validação do arquivo de entrada."""

    def __init__(self, filename):
        """
        :param filename: Nome do arquivo de entrada.
        :type filename: str
        """
        self.file = filename
        self.line_counter = 0

    def read_file(self):
        """Valida, linha por linha, o arquivo de entrada e retorna as estruturas que compõem 
            a máquina de Turing mais a entrada.
        """

        self.check_line(self.file.readline(), FIRST_LINE)
        Q = self.remove_blank(self.check_line(self.file.readline(), Q_LINE))
        E = self.remove_blank(self.check_line(self.file.readline(), E_LINE))
        r = self.remove_blank(self.check_line(self.file.readline(), r_LINE))
        self.check_line(self.file.readline(), FIRST_S_LINE)
        S = []
        S_pattern = create_S_pattern(Q,r)
        while(True):
            line = self.file.readline()
            # Se nao for a ultima transicao do arquivo
            if not line.find('}') == -1:
                break
            else:
                S.append(self.check_line(line, S_pattern))
            
        q0 = self.check_line(self.file.readline(), q0_LINE)
        self.check_line(self.file.readline(), LAST_LINE)
        input = self.check_line(self.file.readline(), create_input_pattern(r))
            
        return Q, S, q0[0], input[0]
    
    def remove_blank(self, line):
        """Remove espaços em branco e gera uma lista com dos valores separados por vírgula.
       
        :param line: Linha do arquivo de entrada
        :type line: str
        """

        return line[0].replace(' ','').split(',')

    def check_line(self, line, expected):
        """Valida linha do arquivo de entrada reconhecendo padrões em regex, montados no módulo ``patterns``

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
                        + " do arquivo ")
