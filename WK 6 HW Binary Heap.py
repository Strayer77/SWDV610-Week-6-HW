#Matt Strayer
#contains solutions for questions 1 and 2 for Week 6 - Forest for the Trees
#see main method below for implementation of Binary Heap class
#and binary heap trees resulting from inserting into list one item at
#a time vs. the buildHeap method 

import random

class BinaryHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    #returns heapList    
    def getheapList(self):
        return self.heapList
    
    #returns currentSize
    def getcurrentSize(self):
        return self.currentSize
        
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
                
            i = i // 2
 
 
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
 
 
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1





def randNumListGenerator():
    
    randNumList = []
    for i in range(20):
        randNumList.append(random.randint(1,100))
        
    return randNumList


def main():
    randNumList = randNumListGenerator()
    
    binHeapTree = BinaryHeap()
    
    #this appends items from randNumList into binHeapTree using
    #the insert method from the Binary Heap Class
    for i in randNumList:
        binHeapTree.insert(i)
        
    #prints result from using this method
    print("The following list is a result of inserting the items from the randNumList one at a time: ")
    print(binHeapTree.getheapList())   #created a function within the
                                       #binary heap class to return heaplist
 
    #this takes the randNumList and uses it as a parameter for the buildHeap
    #method
    binHeapTree.buildHeap(randNumList)
    buildHeapMethod = binHeapTree.getheapList()
    
    print()
    #prints result of buildHeap method
    print("This is the result using the buildHeap method: ")
    print(buildHeapMethod)

main()
    
    
    
    