# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 00:08:41 2021

@author: dsd
"""

import sys

#Task №3

if __name__ == '__main__':
    # Ввести список одной строкой.
    Arr = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(Arr) != 10:
        print("Неверный размер списка", file=sys.stderr)
        sys.exit(1)
        
    # Найти искомое произведение
    mult = 1
    for item in range(0, 10, 2):
            mult *= Arr[item]
    print(f"Произведение: {mult}")
    
    # Найти сумму между первым и последним нулём
    start = end = Arr.index(0)
    sum = 0
    it = 9
    while it >= 0:
        if Arr[it] == 0:
            end = it
            break
        it -= 1
    for item in range(start, end):
        sum += Arr[item]
    print(f"Сумма: {sum}")
    
    # Получить список со сначала положительными элементами
    Arr.sort()
    Arr.reverse()
    print(Arr)
    