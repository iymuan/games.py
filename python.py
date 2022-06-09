from ast import Return
from operator import truediv
import random
my_list = ['R', 'P', 'S']
my_list2 = ['R', 'P', 'S', 'A', 'B', 'C']
player = input('choose a letter within R P S:',)
CPU = random.choice(my_list2)
print('CPU PLAYED ',CPU)
print('YOU PLAYED ',player)

for my_list in my_list:
    if my_list == player and CPU !=my_list :
        print('you win')
        print('cpu lose')
    elif my_list == '':
        print('box empty')

    elif my_list != player and my_list ==CPU :
        print('cpu win')
        print('you lost')
    if my_list != player and my_list != CPU :
        print('you two lost')

# print(my_lis)