import math as E
import random as R

result_1 = E.pow(2,4)
print('Result_1 is', result_1)

result_2 = E.sqrt(16)
print('result_2 is', result_2)

result_3 = R.randint(0,100)
print('result_3 is', result_3)

names = ['Noah', 'Alex', 'Amy', 'Steve', 'Naomi', 'David', 'Sam', 'Brian']
print('Original names', names)

R.shuffle(names)
print('Names after shuffle', names)

result_4 = R.choice(names)
print('Chosen name is:', result_4)