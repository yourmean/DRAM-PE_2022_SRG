import heapq

def solution(n, works):
    
    if sum(works) <= n:
        return 0
    
    hq = []
    for i in works:
        heapq.heappush(hq, -i)
    
    while n:
        max_work = heapq.heappop(hq) + 1
        n -= 1
        heapq.heappush(hq, max_work)
        
    answer = sum([i ** 2 for i in hq])
    
    return answer
