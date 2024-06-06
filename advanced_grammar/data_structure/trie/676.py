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

    def magicSearch(self, word:str, start:int, magic:bool, current:'PrefixTree') -> bool:
        for i in range(start,len(word)):
            if magic:
                res = False
                for d in range(26):
                    next_c = chr(97+d)
                    if current.get(next_c) != None:
                        next_m = True if next_c == word[i] else False
                        res |= self.magicSearch(word,i+1,next_m,current.get(next_c))
                return res
            else:
                if not current.get(word[i]):
                    return False
                current = current.get(word[i])
        if magic:
            return False
        return current.isEnd

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            self.trie.insert(d)

    def search(self, searchWord: str) -> bool:
        return self.trie.magicSearch(searchWord,0,True,self.trie.root)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)