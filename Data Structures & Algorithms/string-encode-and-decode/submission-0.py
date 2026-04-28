class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet", "code", "qwertyuiop"] -> "4#neet4#code10#qwertyuiop" 
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # "4#neet4#code10#qwertyuiop" -> ["neet", "code", "qwertyuiop"]
        res, i = [], 0

        while i < len(s):
            j = i
            # get number
            while s[j] != "#":
                j += 1 
            # get word
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            res.append(s[word_start: word_end])

            i = word_end

        return res