from math import pow as M
from math import sqrt as N
from random import randint as R
from random import shuffle as S
from random import choice as C

result_1 = M(2,4)
print('Result_1 is', result_1)

result_2 = N(16)
print('result_2 is', result_2)

result_3 = R(0,100)
print('result_3 is', result_3)

names = ['Noah', 'Alex', 'Amy', 'Steve', 'Naomi', 'David', 'Sam', 'Brian']
print('Original names', names)

S(names)
print('Names after shuffle', names)

result_4 = C(names)
print('Chosen name is:', result_4)