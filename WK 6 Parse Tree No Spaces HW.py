#Matt Strayer
#Parse Tree implementation
#Evalutating Expressions with no spaces

from stack import Stack
from binaryTree import BinaryTree
import operator


def buildParseTree(fpexp):
    #creates an empty list and then iterates through the expression
    #appending items into fpList
    #checks to see if the item in the expression is a number and if the index
    #before is a number to group them together and append together in list
    fpList = [""]
    for i in fpexp.replace(" ",""):
        if i.isdigit() and fpList[-1].isdigit():
            fpList[-1] = fpList[-1] + i
        else:
            fpList.append(i)
    fpList.pop(0)
    
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fpList:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
        
    return eTree

def evaluate(parseTree):
    opers = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv }
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:   #if object exists, return True, if not - False
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
#can try expression with or without spaces and it will evaluate
#and print answer

pt = buildParseTree("((20+5)*(3+1))")
print(evaluate(pt))
