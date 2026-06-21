class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-n for n in count.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1]==time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

        return time 
