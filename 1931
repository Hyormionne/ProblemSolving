import sys
input = sys.stdin.readline

def max_meetings(meeting_list):
    meeting_list.sort(key=lambda x: (x[1], x[0]))
    cnt = 0
    end = 0
    for s,e in meeting_list:
        if s >= end:
            cnt += 1
            end = e
            
    return cnt

M = int(input())
meetings = []
for _ in range(M):
    a, b = map(int, input().split())
    meetings.append((a, b))
    
print(max_meetings(meetings))
