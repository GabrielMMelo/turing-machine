import re as regex
import constant as const
import sys

class Reader():
    def __init__(self, filename):
        self.file = filename

    def read_from_file(self):
        with open(self.file) as file:
            self.check_line(file.readline(), const.FIRST_LINE)
            self.check_line(file.readline(), const.Q_LINE)
            self.check_line(file.readline(), const.E_LINE)
            self.check_line(file.readline(), const.r_LINE)
            file.readline()
            self.check_line(file.readline(), const.S_LINE)

    def check_line(self, line, expected):
        try:
            if not regex.match(expected, line):
                raise Exception('Formato de arquivo inválido')
        except Exception as error:
                print('Erro encontrado: ' + repr(error))
                sys.exit(1)
