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
    
    def shortest(self, word:str) -> str:
        current = self.root
        s = ""
        for c in word:
            if not current.get(c):
                return ""
            s += c
            current = current.get(c)
            if current.isEnd:
                return s
        return s


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        res = ""
        for s in sentence.split(" "):
            rep = trie.shortest(s)
            if len(rep) != 0:
                res += rep + " "
            else:
                res += s + " "
        return res[:-1]