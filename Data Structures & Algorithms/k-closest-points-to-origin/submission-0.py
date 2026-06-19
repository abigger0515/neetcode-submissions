class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dist = x**2 + y**2
            dists.append((dist, [x, y]))

        heapq.heapify(dists)
        res = []
        for _ in range(k):
            _, point = heapq.heappop(dists)
            res.append(point)

        return res 