#-*-coding:utf8-*-


inputData=[5,7,2,4,6,3,9,8,1]
#上升操作
def swimNode(i):
    while(i>1):
        j=int(i/2)
        if(inputData[i]>inputData[j]):
            inputData[i],inputData[j]=inputData[j],inputData[i]
            i=j
        else:
            break
#下降操作
def sinkNode(i,n):
    while(i<=int(n/2)):
        j=2*i
        if(j+1<=n)and(inputData[j+1]>inputData[j]):
            j+=1
        if(inputData[j]>inputData[i]):
            inputData[i],inputData[j]=inputData[j],inputData[i]
            i=j
        else:
            break
#创建二叉堆
def createBinHeap(arrayLen):
    for i in range(int((arrayLen-1)/2),-1,-1):
        sinkNode(i,arrayLen-1)
#二叉堆排序
def binHeapSort(arrayLen):
    for i in range(arrayLen-1,0,-1):
        inputData[0],inputData[i]=inputData[i],inputData[0]
        sinkNode(0,i-1)
if __name__=='__main__':
    createBinHeap(len(inputData))
    print (inputData)
    binHeapSort(len(inputData))
    print (inputData)
