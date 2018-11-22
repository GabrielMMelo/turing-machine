from tm import Tm
import sys

if len(sys.argv) <= 1:
	print("Erro: Informe um arquivo de entrada\n\nUso: python3 main.py <caminho-do-arquivo>")
	sys.exit()

input_file = sys.argv[1]

tm = Tm(input_file)
while True:
    try:
        tm.compute()
    except KeyError:
        break