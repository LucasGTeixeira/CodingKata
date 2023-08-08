'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

'''
ideia inciail (transformar lista em numero -> ler ao contrário e criar string 
depois converter para somar e adicionar na lsita ao contrario
'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1_string = ''
l2_string = ''

for i in range(len(l1) - 1, -1, -1):
    l1_string += str(l1[i])

for j in range(len(l2)-1, -1, -1):
    l2_string += str(l2[j])

resultado = int(l1_string) + int(l2_string)

print(f'{l1_string} + {l2_string} = {resultado}')

