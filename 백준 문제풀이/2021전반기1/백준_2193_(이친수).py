# -*- coding: utf-8 -*-
"""백준 2193 (이친수)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F73vwhB7aXvnZ4XEffAPnowTbrK40lVz

길이 1 (1)

    - 1

길이 2 (1)

    - 10

길이 3 (2)

    - 100, 101

길이 4 (3)

    - 1000, 1001, 1010

길이 5 (5)

    - 10000, 10001, 10010, 10100, 10101

--> 피보나치..
"""

N = int(input())

a,b= 0,1

for _ in range(N-1):
    a, b = b, a+b

print(b)

