n = int(input())
schedule = []
for _ in range(n):
    T, P = map(int, input().split())
    schedule.append([T, P])

'''
day-off = n+1 = 7
schedule->  0   1   2   3   4   5   6   ..  n+1
            3   5   1   1   2   4   2   
            10  20  10  20  15  40  200
'''

