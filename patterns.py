from typing import List

FIRST_LINE = r'^\(\n$'
Q_LINE = r'^\s*{((?:q\d+,?\s?)*)},\n$'
E_LINE = r'^\s*{((?:\w+(?:, )?)+)},\n$'
r_LINE = r'^\s*{((?:\w+(?:,)?)+)},\n$'
FIRST_S_LINE = r'^\s*\{\n$'
LAST_S_LINE = r'^\s*\}\n$'
q0_LINE = r'^\s*{(q\d+)}\n$'
LAST_LINE = r'^\)\n$'

def create_S_pattern(Q: List[str], r: List[str]) -> str:
    """Funcao que cria o padrao de transicoes em regex considerando os 
        estados e o alfabeto da fita
    """

    return r'^\s*\((' + '|'.join([i for i in Q]) + '), (' + '|'.join([str(i) for i in r]) + ')\) \-\> \((' + '|'.join([i for i in Q]) + '), (' +'|'.join([str(i) for i in r]) + '), ([R|L])\)(,?)\n$'

def create_input_pattern(r: List[str]) -> str:
    """Funcao que cria o padrao de entrada em regex considerando 
        alfabeto da fita
    """

    return r'^([' + '|'.join([str(i) for i in r]) + ']{2,})$'
