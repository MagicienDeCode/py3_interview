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

Time Limit Exceeded
from collections import deque,defaultdict
import copy
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # build graph
        graph = defaultdict(set)
        for w in wordList:
            if self.neighbor(beginWord,w):
                graph[beginWord].add(w)
                graph[w].add(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if self.neighbor(wordList[i],wordList[j]):
                    graph[wordList[i]].add(wordList[j])
                    graph[wordList[j]].add(wordList[i])
        # find all shortest paths
        dq = deque()
        visited = set()
        dq.append(endWord)
        visited.add(endWord)
        dic = defaultdict(list)
        dic[endWord].append([endWord])
        print(graph)
        while dq:
            to_remove = set()
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                if c == beginWord:
                    return dic[beginWord]
                for n in graph[c]:
                    if n not in visited:
                        if n not in to_remove:
                            dq.append(n)
                            to_remove.add(n)
                        for each in dic[c]:
                            each_copy = copy.deepcopy(each)
                            each_copy.insert(0,n)
                            dic[n].append(each_copy)
            visited.update(to_remove)
        return []

    def neighbor(self, w1:str, w2:str) -> bool:
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1

"""

# BFS + DFS
from collections import deque,defaultdict
import copy
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # build graph
        self.graph = defaultdict(set)
        for w in wordList:
            if self.neighbor(beginWord,w):
                self.graph[beginWord].add(w)
                self.graph[w].add(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if self.neighbor(wordList[i],wordList[j]):
                    self.graph[wordList[i]].add(wordList[j])
                    self.graph[wordList[j]].add(wordList[i])
        self.level_dic = {}
        level = 1
        dq = deque()
        visited = set()
        dq.append(beginWord)
        visited.add(beginWord)
        while dq:
            size = len(dq)
            for _ in range(size):
                c = dq.popleft()
                self.level_dic[c] = level
                if c == endWord:
                    break
                for n in self.graph[c]:
                    if n not in visited:
                        dq.append(n)
                        visited.add(n)
            level += 1
        self.res = []
        temp = deque()
        temp.append(endWord)

        def dfs(cur: str,temp: deque):
            if cur == beginWord:
                self.res.append(list(temp))
                return
            for n in self.graph[cur]:
                if n in self.level_dic and self.level_dic[cur] - self.level_dic[n] == 1:
                    temp.appendleft(n)
                    dfs(n,temp)
                    temp.popleft()
        dfs(endWord,temp)
        return self.res
        

    def neighbor(self, w1:str, w2:str) -> bool:
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1


# BFS + Memorization
from collections import deque,defaultdict
import copy
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # build graph
        self.graph = defaultdict(set)
        for w in wordList:
            if self.neighbor(beginWord,w):
                self.graph[beginWord].add(w)
                self.graph[w].add(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if self.neighbor(wordList[i],wordList[j]):
                    self.graph[wordList[i]].add(wordList[j])
                    self.graph[wordList[j]].add(wordList[i])
        # find all shortest paths
        begin_to_end = self.bfs(beginWord,endWord)
        end_to_begin = self.bfs(endWord,beginWord)
        for etb in end_to_begin:
            etb.reverse()
        # end_to_begin = self.bfsBack(beginWord,endWord)
        begin_to_end.extend(end_to_begin)
        unique_tuples = set(tuple(lst) for lst in begin_to_end)
        unique_lists = [list(t) for t in unique_tuples]
        return unique_lists
        
    def bfs(self, beginWord: str, endWord: str) -> List[List[str]]:
        dq = deque()
        dq2 = deque()
        visited = set()
        dq.append([beginWord])
        visited.add(beginWord)
        res = []
        flag = False
        while dq:
            level = set()
            size = len(dq)
            for _ in range(size):
                seq = dq.popleft()
                c = seq[-1]
                for n in self.graph[c]:
                    if n == endWord:
                        seq_copy = copy.deepcopy(seq)
                        seq_copy.append(n)
                        res.append(seq_copy)
                        flag = True
                        continue
                    if n not in visited:
                        visited.add(n)
                        level.add(n)
                        seq_copy = copy.deepcopy(seq)
                        seq_copy.append(n)
                        dq.append(seq_copy)
                    else:
                        if n in level:
                            seq_copy = copy.deepcopy(seq)
                            seq_copy.append(n)
                            dq2.append(seq_copy)
            if flag:
                break
        dic = defaultdict(list)
        for re in res:
            current = []
            for i in range(len(re)-1,-1,-1):
                dic[re[i]].append(copy.deepcopy(current))
                current.insert(0,re[i])
        while dq2:
            seq = dq2.pop()
            c = seq[-1]
            if len(dic[c]) > 0:
                for ans in dic[c]:
                    seq_copy = copy.deepcopy(seq)
                    seq_copy.extend(ans)
                    res.append(seq_copy)
        return res

    def neighbor(self, w1:str, w2:str) -> bool:
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1