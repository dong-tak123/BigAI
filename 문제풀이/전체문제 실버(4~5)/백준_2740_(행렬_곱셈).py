# -*- coding: utf-8 -*-
"""백준 2740 (행렬 곱셈)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yKXSHnXS39Uzl-XOi09JJedD1ShG8WIU

**문제**

- N*M 크기의 행렬 A
- M*K 크기의 행렬 B
- 두 개의 행렬을 곱하는 프로그램을 구현하라
"""

# KEY POINT!!
# 곱하기로만 표현하면 값이 변할때 같이 바뀌어 버린다..

a = [[0]*3]*4
a[0][0] = 4
print(a)

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

#이렇게 해줘야 값이 안바뀜..
C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for c in C:
    for a in c:
        print(a, end = " ")
    print()

import numpy as np

N,M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

C = (np.array(A)).dot(np.array(B))

for c in C:
    for a in c:
        print(a, end = " ")
    print()

