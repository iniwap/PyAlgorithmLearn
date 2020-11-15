#-*-coding:utf8-*-

class binSortTree:
    def __init__(self,leftNode=None,rightNode=None,data=None):
        self.leftNode=leftNode
        self.rightNode=rightNode
        self.data=data

inputData=[1,5,7,6,9,8,3,4,2]

def insertBinSortTree(bsTree,data):
    if(bsTree.data==None):
        bsTree.data=data
        return
    if(data<bsTree.data):
        if(bsTree.leftNode==None):
            bsTree.leftNode=binSortTree()
        insertBinSortTree(bsTree.leftNode,data)
    else:
        if(bsTree.rightNode==None):
            bsTree.rightNode=binSortTree()
        insertBinSortTree(bsTree.rightNode,data)
def createBinSortTree(tree):
    for data in inputData:
        insertBinSortTree(tree,data)
#中序遍历即可输出排序后的结果，稳定时间复杂度O(nlog2(n))
def inOrderTraversal(binTree):
    if(binTree):
       inOrderTraversal(binTree.leftNode)
       if(binTree.data):
           print(binTree.data)
       inOrderTraversal(binTree.rightNode)

if __name__=='__main__':
    root=binSortTree()
    createBinSortTree(root)
    print("----二叉排序树----")
    inOrderTraversal(root)
