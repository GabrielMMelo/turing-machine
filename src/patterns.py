FIRST_LINE = r'^\(\n$'
Q_LINE = r'^\s*{((?:q\d+,?\s?)*)},\n$'
E_LINE = r'^\s*{((?:\w+(?:, )?)+)},\n$'
r_LINE = r'^\s*{((?:\w+(?:,)?)+)},\n$'
FIRST_S_LINE = r'^\s*\{\n$'
LAST_S_LINE = r'^\s*\}\n$'
q0_LINE = r'^\s*{(q\d+)}\n$'
LAST_LINE = r'^\)\n$'

def create_S_pattern(Q, r):
    """Função que cria o padrão de transições em regex considerando os 
        estados e o alfabeto da fita.

    :param Q: Lista dos nomes dos estados da maquina de Turing
    :type Q: List
    :param r: Lista com o alfabeto da fita da maquina de Turing
    :type r: List

    :return: (*str*) Padrão em `regexp` para reconhecimento de transições no arquivo de entrada montado, dinâmicamente, de \
    acordo com os estados da máquina e o alfabeto da fita.
    """

    return r'^\s*\((' + '|'.join([i for i in Q]) + '), (' + '|'.join([str(i) for i in r]) + ')\) \-\> \((' + \
            '|'.join([i for i in Q]) + '), (' +'|'.join([str(i) for i in r]) + '), ([R|L])\)(,?)\n$'

def create_input_pattern(r):
    """Função que cria o padrão de entrada em regex considerando 
        alfabeto da fita.

    :param r: Lista com o alfabeto da fita da máquina de Turing
    :type r: List

    :return: (*str*) Padrão em `regexp` para reconhecimento da entrada da máquina de Turing no arquivo de entrada montado,\
            dinâmicamente, de acordo com o alfabeto da fita.
    """

    return r'^([' + '|'.join([str(i) for i in r]) + ']{2,})$'
