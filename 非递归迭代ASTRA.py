import copy,time
start=time.clock()
INF=100
path=[]
solution=[]
Sg=[0,1,2,3,4,5,6,7,8]
So=[3,5,0,8,7,4,2,1,6,0]
def fx(node):
    hx=0
    for i in range(9):
        if node[i]!=8:
            hx+=abs(node[i]//3-i//3)+abs(node[i]%3-i%3)
    f_x=hx+node[9]
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
        s1.append(node[9]+1)
        if s1[:9]!=node[:9]:
            snode.append(s1)
    if ij//3<2:
        Ntemp2=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp2[ij//3][ij%3]=Ntemp2[ij//3+1][ij%3]
        Ntemp2[ij//3+1][ij%3]=8              
        for i in range(3):
            for j in range(3):
                s2.append(Ntemp2[i][j])
        s2.append(node[9]+1)
        if s2[:9]!=node[:9]:
            snode.append(s2)
    if ij%3>0:
        Ntemp3=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp3[ij//3][ij%3]=Ntemp3[ij//3][ij%3-1]
        Ntemp3[ij//3][ij%3-1]=8 
        for i in range(3):
             for j in range(3):
                s3.append(Ntemp3[i][j])
        s3.append(node[9]+1)
        if s3[:9]!=node[:9]:
            snode.append(s3)
    if ij%3<2:
        Ntemp4=copy.deepcopy([node[0:3],node[3:6],node[6:9]])
        Ntemp4[ij//3][ij%3]=Ntemp4[ij//3][ij%3+1]
        Ntemp4[ij//3][ij%3+1]=8      
        for i in range(3):
             for j in range(3):
                s4.append(Ntemp4[i][j])
        s4.append(node[9]+1)
        if s4[:9]!=node[:9]:
            snode.append(s4)
    return snode
def IDAStar(root):
    repeat=1
    bound=fx(root)
    solution.append(So)
    while repeat:
        path.append(root)
        next_bound=INF
        while len(path)!=0:
            node=path.pop()
            if node[:9]==Sg:
                print('OK')
                repeat=0
                break
            else:
                for successor in expand(node):
                    if fx(successor)<=bound:
                        path.append(successor)
                        #if node[9]<=successor[9]:
                         #   solution.append(successor)       
                    else:
                        next_bound=min(next_bound,fx(successor))
        if len(path)==0 and next_bound==INF:
            print('fail')
            break
        if len(path)==0 and next_bound!=INF:
            bound=next_bound
IDAStar(So)
end=time.clock()
print(end-start)
print(len(path))
#for i in solution:
 #   print(solution.pop())