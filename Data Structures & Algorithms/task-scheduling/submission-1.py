class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = Counter(tasks)
        max_heap = [-f for f in freq_count.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1
            if max_heap:
                # pop the current task and append to cooldown 
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq:
                    cooldown.append((freq, time+n))

            if cooldown and cooldown[0][1]==time:
                freq, _ = cooldown.popleft()
                heapq.heappush(max_heap, freq)

        return time 
                