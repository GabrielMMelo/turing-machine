import sys
from tm import Tm

try:
    input_file = sys.argv[1]
except:
    sys.exit("Erro de sintaxe: Informe um arquivo de entrada\n\nUso: python3 main.py <caminho-do-arquivo>")

tm = Tm(input_file)
while True:
    try:
        tm.compute()
    except KeyError:
        break