"""
Time Limit Exceeded
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        w_set = set(wordList)
        if endWord not in w_set:
            return []
        dq = deque()
        dq.append((beginWord,beginWord))
        flag = False
        res = []
        while dq:
            size = len(dq)
            to_remove = set()
            for _ in range(size):
                c,seq = dq.popleft()
                if c == endWord:
                    flag = True
                    res.append(seq.split(','))
                if flag:
                    continue
                for i in range(len(c)):
                    c_arr = [ci for ci in c]
                    for j in range(ord('a'),ord('z')+1):
                        c_arr[i] = chr(j)
                        next_s = "".join(c_arr)
                        if next_s in w_set:
                            to_remove.add(next_s)
                            dq.append((next_s,seq+','+next_s))
            if flag:
                break
            w_set.difference_update(to_remove)
        return res
"""