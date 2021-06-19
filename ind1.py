# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:37:18 2021

@author: dsd
"""

import sys

#Task №4

if __name__ == '__main__':
    # Ввести список одной строкой.
    Arr = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(Arr) != 10:
        print("Неверный размер списка", file=sys.stderr)
        sys.exit(1)
        
    # Найти искомую сумму
    s = 0
    for item in Arr:
        if item < 0:
            s += item
    print(s)