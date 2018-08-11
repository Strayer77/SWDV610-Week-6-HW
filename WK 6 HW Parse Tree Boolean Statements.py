#Matt Strayer

from stack import Stack
from binaryTree import BinaryTree
import operator


def buildParseTree(fpexp):
    fpList = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fpList:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['and', 'or', 'not', ')']: #added boolean operators
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['and', 'or', 'not']: #added boolean operators
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
    #Modified by adding boolean operators 
    opers = {'and' : operator.and_, 'or' : operator.or_, 'not' : operator.not_ }
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:   #if object exists, return True, if not - False
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
    

pt = buildParseTree(" ( 3 or 4 ) and ( 6 or 7 ) ")
pt.postorder()
print(evaluate(pt))
