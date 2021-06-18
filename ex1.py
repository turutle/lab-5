# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:03:45 2021

@author: dsd
"""

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        sys.exit(1)
        
    # Найти искомую сумму.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)