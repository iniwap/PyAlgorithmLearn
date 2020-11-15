#-*-coding:utf8-*-

'''
step0,初始输入
inputData=[1,5,3,7]
inputData.sort()

step1,n个权值看成n棵树的森林，每棵树仅一个节点
forest=[Huffmantree(None,None,i)for i in inputData]

step2,在森林中选出两个根结点的权值最小的树合并，作为一棵新树的左、右子树，
且新树的根结点权值为其左、右子树根结点权值之和
newTree=Huffmantree(forest[0],forest[1],forest[0].data+forest[1].data)

step3,从森林中删除选取的两棵树，并将新树加入森林
del(forest[:2])
for nodeIndex in range(len(forest)):
    if forest[nodeIndex].data>=newTree.data:
        forest.insert(nodeIndex,newTree)
    elif nodeIndex==len(forest)-1:
        forest.append(newTree)  
step4,重复step2,step3,直到最后一棵树
递归实现
'''
class Huffmantree:
    def __init__(self,leftNode,rightNode,data):
        self.leftNode=leftNode
        self.rightNode=rightNode
        self.data=data
        
inputData=[1,5,3,7]
inputData.sort()

forest=[Huffmantree(None,None,i)for i in inputData]

def loopStep2Step3():

    newTree=Huffmantree(forest[0],forest[1],forest[0].data+forest[1].data)

    del(forest[:2])
    if(len(forest)==0):
        forest.append(newTree)
        return
    for nodeIndex in range(len(forest)):
        if forest[nodeIndex].data>=newTree.data:
            forest.insert(nodeIndex,newTree)
            break
        elif nodeIndex==len(forest)-1:
            forest.append(newTree)
    loopStep2Step3()
#中序遍历
def inOrderTraversal(binTree):
    if(binTree):
       inOrderTraversal(binTree.leftNode)
       print(binTree.data)
       inOrderTraversal(binTree.rightNode)
if __name__=='__main__':
    loopStep2Step3()
    print("----中序遍历----")
    inOrderTraversal(forest[0])
