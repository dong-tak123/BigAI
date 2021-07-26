# -*- coding: utf-8 -*-
"""백준 2312 (수 복원하기)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qq5d_g4ftVVrH3bKml8vZiim4MOplLiT

#기억하자

**딕셔너리 항 추가**

- (딕셔너리명)[키값] = 넣고싶은 값

- 결과 : 딕셔너리 = {"키값" : "넣고싶은 값"}
"""

#최대 양의 정수 1000000까지의 소수인지의 TF를 저장..
max = 1000000
prime = [False, False] + [True] * (max-1)
for i in range(2,int(max**0.5) + 1):
    if prime[i]:
        for j in range(2*i, max+1, i):
            prime[j] = False

#테스트케이스 받자..
T = int(input())

for _ in range(T):
    N = int(input())
    dividor = {}
    
    #딕셔너리에 이제 다 약수의 정보가 남아있음
    for i in range(2, N+1):
        if prime[i] and N % i == 0:
            dividor[i] = 0
            while (N % i == 0):
                dividor[i] += 1
                N = N / i
    
    #이제 출력
    for key in dividor:
        print(f"{key} {dividor[key]}")

# 사실 prime을 dp로 만들 이유도 없다..
# 약수별로 카운트를 올리면서 바로바로 출력하면 된다..

T = int(input())

for _ in range(T):
    N = int(input())

    #얘를 그냥 나눠가면서 약수마다 출력해주면됨..
    for i in range(2, N+1):
        cnt = 0
        if N % i == 0:
            while (N%i == 0):
                cnt+=1
                N = N / i
            print(f"{i} {cnt}")
        elif N == 1:
            break