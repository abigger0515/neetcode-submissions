class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. get count of each num, {num: cnt}
        # 2. cnt map array [[cnt, num], [cnt, num], ...] sort
        # 3. pop

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        cnt_num = []
        for n, cnt in cnt.items():
            cnt_num.append([cnt, n])
        cnt_num = sorted(cnt_num)
        print(cnt_num)
        
        res = []
        while len(res) < k:
            res.append(cnt_num.pop()[1])

        return res