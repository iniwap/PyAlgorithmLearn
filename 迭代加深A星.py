import copy,time
start=time.clock()
find=0
INF=20
Sg=[0,1,2,3,4,5,6,7,8]
So=[0,4,6,1,3,2,5,7,8]
def fx(depth,node):
    hx=0
    for i in range(9):
        if node[i]!=8:
            hx+=abs(node[i]//3-i//3)+abs(node[i]%3-i%3)
    f_x=hx+depth
    return f_x
def expand(node):
    s1=[]
    s2=[]
    s3=[]
    s4=[]
    snode=[]
    ij=node.index(8)
    if ij//3>0:
        Ntemp1=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp1[ij//3][ij%3]=Ntemp1[ij//3-1][ij%3]
        Ntemp1[ij//3-1][ij%3]=8 
        for i in range(3):
            for j in range(3):
                s1.append(Ntemp1[i][j])
        if len(s1)!=0 and s1!=node:
            snode.append(s1)
    if ij//3<2:
        Ntemp2=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp2[ij//3][ij%3]=Ntemp2[ij//3+1][ij%3]
        Ntemp2[ij//3+1][ij%3]=8      
        for i in range(3):
            for j in range(3):
                s2.append(Ntemp2[i][j])
        if len(s2)!=0 and s2!=node:
            snode.append(s2)
    if ij%3>0:
        Ntemp3=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp3[ij//3][ij%3]=Ntemp3[ij//3][ij%3-1]
        Ntemp3[ij//3][ij%3-1]=8 
        for i in range(3):
             for j in range(3):
                s3.append(Ntemp3[i][j])
        if len(s3)!=0 and s3!=node:
            snode.append(s3)
    if ij%3<2:
        Ntemp4=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp4[ij//3][ij%3]=Ntemp4[ij//3][ij%3+1]
        Ntemp4[ij//3][ij%3+1]=8      
        for i in range(3):
             for j in range(3):
                s4.append(Ntemp4[i][j])
        if len(s4)!=0 and s4!=node:
            snode.append(s4)
    return snode
def IDAStar(root):
    bound=fx(0,root)
    while bound<INF and find==0:
        bound=IDA(0,root,bound)
def IDA(depth,node,bound):
    global find
    if node==Sg:
        find=1
        print(depth)
        return INF
    else:
        fn=INF
        for successor in expand(node):
            f=fx(depth+1,successor)
            if f<=bound:
                fn=min(fn,IDA(depth+1,successor,bound))
            else:
                fn=min(fn,f)
        return fn
IDAStar(So)
end=time.clock()
print end-start