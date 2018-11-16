from reader import Reader
class Mt():
    def __init__(self):
       reader = Reader("entrada.txt")
       reader.read_from_file()
       '''
       self.Q = Q
       self.E = E
       self.r = r
       self.S = S
       self.q0 = q0
       '''

Q = ['q0', 'q1', 'q2', 'q3', 'q4']
E = ['1']
r = ['1', 'B']
S = ['(q0, B) -> (q1, B, R)',
     '(q1, 1) -> (q1, 1, R)',
     '(q1, B) -> (q2, 1, R)',
     '(q2, 1) -> (q2, 1, R)',
     '(q2, B) -> (q3, B, L)',
     '(q3, 1) -> (q4, B, L)',
     '(q4, 1) -> (q5, B, L)',
     '(q5, 1) -> (q5, 1, L)']
q0 = 'q0'

input = 'B1111B11B'
mt = Mt()

