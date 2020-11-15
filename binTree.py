#-*-coding:utf8-*-

class binTree:
    def __init__(self,leftNode=None,rightNode=None,data=None):
        self.leftNode=leftNode
        self.rightNode=rightNode
        self.data=data
        
root=binTree()
def createBinTree(bTree):
    bTree.data=input("Please enter data,* for have not this child:\n")
    if(bTree.data=="*"):
        return
    bTree.rightNode=binTree()
    bTree.leftNode=binTree()
    createBinTree(bTree.leftNode)
    createBinTree(bTree.rightNode)

#中序遍历
def inOrderTraversal(binTree):
    if(binTree):
       inOrderTraversal(binTree.leftNode)
       if(binTree.data!="*"):
           print(binTree.data)
       inOrderTraversal(binTree.rightNode)
#前序遍历
def preorderTraversal(binTree):
    if(binTree):
       if(binTree.data!="*"):
           print(binTree.data)
       preorderTraversal(binTree.leftNode)
       preorderTraversal(binTree.rightNode)
#后序遍历
def postorderTraversal(binTree):
    if(binTree):
       postorderTraversal(binTree.leftNode)
       postorderTraversal(binTree.rightNode)
       if(binTree.data!="*"):
           print(binTree.data)
if __name__=='__main__':
    createBinTree(root)
    print("----中序遍历----")
    inOrderTraversal(root)
    print("----前序遍历----")
    preorderTraversal(root)
    print("----后序遍历----")
    postorderTraversal(root)
