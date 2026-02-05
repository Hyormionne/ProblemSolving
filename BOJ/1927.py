import sys
input = sys.stdin.readline

import heapq

def min_heap(n, num_list):
    heap = []
    for i in range(n):
        if num_list[i] > 0:
            heapq.heappush(heap, num_list[i])
        else:
            if len(heap) == 0:
                print(0)
            else:
                min_val = heapq.heappop(heap)
                print(min_val)
                
N = int(input())
nums = [int(input()) for _ in range(N)]
                
min_heap(N, nums)
