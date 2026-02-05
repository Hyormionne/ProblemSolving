import sys
input = sys.stdin.readline
            
def primes3(n):
    prime = [i for i in range(2, n) if prime_check[i]]
    
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            n3 = n - prime[i] - prime[j]
            if n3 < prime[j]:
                continue
            if n3 >= 2 and prime_check[n3]:
                return [prime[i], prime[j], n3]
    return 0


T = int(input())
K_list = [int(input()) for _ in range(T)]
maxK = max(K_list)

prime_check = [True] * (maxK + 1)
prime_check[0] = prime_check[1] = False

for i in range(2, int(maxK ** 0.5) + 1):
    if prime_check[i]:
        for j in range(i * i, maxK + 1, i):
            prime_check[j] = False

for K in K_list:
    ans = primes3(K)
    if ans == 0:
        print(0)
    else:
        ans.sort()
        print(*ans)
