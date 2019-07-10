class Solution(object):
    def leastInterval(self, tasks, n):
        statisticInfo={ c:0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        for t in tasks:
            statisticInfo[t]+=1

        maxNumber=max(statisticInfo.values())

        numberMaxNumber=0

        numberKeys=0
        for s in statisticInfo.values():
            if s >0:
                numberKeys+=1
            if s==maxNumber:
                numberMaxNumber+=1
        if len(tasks) > (n + 1) * (maxNumber - 1) + numberMaxNumber:
            #print(len(tasks))
            return len(tasks)
        else:
            #print((n + 1) * (maxNumber - 1) + numberMaxNumber)
            return (n + 1) * (maxNumber - 1) + numberMaxNumber

sln=Solution()
assert 13==sln.leastInterval(["A","A","A","A","B","B","B","B","B","C"],2)
assert 11==sln.leastInterval(["A","A","A","A","B","B","B","B","C"],2)
assert 20==sln.leastInterval(["A","A","A","A","B","B","B","B","C"],5)
assert 29==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],6)
assert 25==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],5)
assert 21==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],4)
assert 17==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],3)
assert 13==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],2)
assert 13==sln.leastInterval(["A","A","A","A","B","B","B","B","C","C","C","C","C"],1)
assert 11==sln.leastInterval(["A","A","A","A","A","A","B","C","C"],1)
assert 16==sln.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)