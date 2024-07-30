from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        # constructing graph
        edges = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for w in wordList:
                if w not in edges[word]:
                    match = 0
                    for i in range(len(word)):
                        if word[i] != w[i]:
                            match += 1
                        if match > 1:
                            break
                    
                    if match == 1:
                        edges[word].append(w)
                        edges[w].append(word)
            
        # print(edges)

        queua = deque()
        queua.append((beginWord, 1))
        visited = set()

        while len(queua) > 0:
            
            current, dist = queua.popleft()
            if current == endWord:
                return dist
            
            for neighbour in edges[current]: 
                if neighbour not in visited:
                    queua.append((neighbour, dist+1))
                    visited.add(neighbour)
        
        return 0


    def ladderLength2(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        # constructing graph
        # edges = defaultdict(list)
        # wordList.append(beginWord)

        # for word in wordList:
        #     for w in wordList:
        #         if w not in edges[word]:
        #             match = 0
        #             for i in range(len(word)):
        #                 if word[i] != w[i]:
        #                     match += 1
                    
        #             if match == 1:
        #                 edges[word].append(w)
        #                 edges[w].append(word)
            
        # print(edges)

        queua = deque()
        queua.append((beginWord, 1))
        visited = set()

        while len(queua) > 0:
            
            current, dist = queua.popleft()
            if current == endWord:
                return dist
            for word in wordList:
                if word not in visited:
                    match = 0
                    for i in range(len(word)):
                        if current[i] != word[i]:
                            match += 1
                        if match > 1:
                            break
                    if match == 1:
                        queua.append((word, dist+1))
                        visited.add(word)
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength2(beginWord, endWord, wordList))