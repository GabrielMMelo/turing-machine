#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.tm import Tm

if __name__ == "__main__":
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
