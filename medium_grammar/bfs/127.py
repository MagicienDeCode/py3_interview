from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        w_set = set(wordList)
        if endWord not in w_set:
            return 0
        dq = deque()
        dq.append(beginWord)
        level = 1
        while dq:
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                if c == endWord:
                    return level
                for i in range(len(c)):
                    c_arr = [ci for ci in c]
                    for j in range(ord('a'),ord('z')+1):
                        c_arr[i] = chr(j)
                        next_s = "".join(c_arr)
                        if next_s in w_set:
                            dq.append(next_s)
                            w_set.remove(next_s)
                    
            level += 1
        return 0
        