from typing import Optional

class PrefixTree:
    def __init__(self):
        self.links = [None]*26
        self.isEnd = False
    
    def get(self,c:str) -> Optional['PrefixTree']:
        return self.links[ord(c)-97]
    
    def add(self,c:str,pt:'PrefixTree'):
        self.links[ord(c)-97] = pt

class Trie:
    def __init__(self):
        self.root = PrefixTree()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if not current.get(c):
                current.add(c,PrefixTree())
            current = current.get(c)
        current.isEnd = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if not current.get(c):
                return False
            current = current.get(c)
        return current.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if not current.get(c):
                return False
            current = current.get(c)
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = ""
        for i in range(26):
            if trie.root.links[i] and trie.root.links[i].isEnd:
                next_res = self.dfs(trie.root.links[i],i)
                if len(next_res) > len(res): res = next_res
        return res

    def dfs(self,pt: Optional['PrefixTree'],c:int)->str:
        res = ""
        for i in range(26):
            if pt.links[i] and pt.links[i].isEnd:
                next_res = self.dfs(pt.links[i],i)
                if len(next_res) > len(res): res = next_res
        return chr(97+c) + res 