# -*- coding: utf-8 -*-
"""백준 1002번(터렛)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WdMs4a3mIGOXusAg1f9xn6m9qUk0ObfV

KEY IDEA

(x1,y1)을 중심으로 하고 반지름이 r1인 원과

(x2,y2)를 중심으로 하고 반지름이 r2인 원의 교점을 구하는 코드..

얘는 readline()안써도 시간초과 안뜸..
"""

'''
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
'''

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    
    if (x1==x2) and (y1==y2) and (r1==r2):
        print(-1)
    elif (distance > r1+r2) or (distance < abs(r1-r2)):
        print(0)
    elif (distance < r1+r2) and (distance > abs(r1-r2)):
        print(2)
    elif (distance == abs(r1-r2)) or (distance == r1+r2):
        print(1)

