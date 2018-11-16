FIRST_LINE = r'^\(\n$'
Q_LINE = r'^\s*{((?:q\d+,?\s?)*)},\n$'
E_LINE = r'^\s*{((?:\w+(?:, )?)+)},\n$'
r_LINE = r'^\s*{((?:\w+(?:,)?)+)},\n$'
FIRST_S_LINE = r'^\s*\{\n$'
S_LINE = r'^\s*\((q\d+), (\w+)\) \-\> \((q\d+), (\w+), ([R|L])\)(,?)\n$'
LAST_S_LINE = r'^\s*\}\n$'
q0_LINE = r'^\s*{(q\d+)}\n$'
LAST_LINE = r'^\)\n$'
INPUT_LINE = r'^$'

# Cria o padrao em regex considerando os estados e o anfabeto da fita
def create_S_pattern(Q, r):
    return r'^\s*\((' + '|'.join([i for i in Q]) + '), (' + '|'.join([str(i) for i in r]) + ')\) \-\> \((' + '|'.join([i for i in Q]) + '), (' +'|'.join([str(i) for i in r]) + '), ([R|L])\)(,?)\n$'

def create_input_pattern(r):
    return r'^([' + '|'.join([str(i) for i in r]) + ']{2,})$'
