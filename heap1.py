def solution(scoville, k):
    import heapq
    answer = 0
    heap = sorted(scoville)
    while heap[0] <= k:
        answer += 1
        a = heapq.heappop(heap)
        if not heap:
            return -1
        b = heapq.heappop(heap)
        sum = a + (b * 2)
        heapq.heappush(heap, sum)

    return answer

scoville = [1, 2, 3, 9, 10, 12]	
k = 7

print(solution(scoville, k))