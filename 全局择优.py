import copy
n=0
Sg=[0,1,2,3,4,5,6,7,8]
So=[4, 5, 2, 8, 6, 7, 0, 1, 3,0,0]
OPEN=[]
CLOSED=[]
OPEN.append(So)
def h(x):
    hx=0
    x=copy.deepcopy(x[:9])
    for i in range(9):
        if x[i]!=Sg[i]:
            hx+=1
    return hx
def P(x):
    if x==1:
        return None
    else:
        P0.append(x)
        return P(CLOSED[x-1][9])
while 1:
    s1=[]
    s2=[]
    s3=[]
    s4=[]
    if len(OPEN)==0:
        print ('fail')
        break
    else:
        temp=OPEN[0]
        N=copy.deepcopy(OPEN[0])
        del(OPEN[0])
        if temp[9]>100:
            break
        CLOSED.append(temp)  
        N=N[:9]
        if N==Sg:
            print('OK')
            Path=copy.deepcopy(CLOSED)
            P0=[]
            P0.append(len(CLOSED))
            P(Path.pop().pop())
            for i in P0[1:]:
                    print (CLOSED[i-1][:9])
            break
        else:
            n+=1
            ij=N.index(8)
            if ij//3>0:
                Ntemp1=copy.deepcopy([N[0:3],N[3:6],N[6:9]])
                Ntemp1[ij//3][ij%3]=Ntemp1[ij//3-1][ij%3]
                Ntemp1[ij//3-1][ij%3]=8 
                for i in range(3):
                    for j in range(3):
                        s1.append(Ntemp1[i][j])
                s1.append(n)
                s1.append(h(s1))
            if ij//3<2:
                Ntemp2=copy.deepcopy([N[0:3],N[3:6],N[6:9]])
                Ntemp2[ij//3][ij%3]=Ntemp2[ij//3+1][ij%3]
                Ntemp2[ij//3+1][ij%3]=8                
                for i in range(3):
                    for j in range(3):
                        s2.append(Ntemp2[i][j])
                s2.append(n)
                s2.append(h(s2))
            if ij%3>0:
                Ntemp3=copy.deepcopy([N[0:3],N[3:6],N[6:9]])
                Ntemp3[ij//3][ij%3]=Ntemp3[ij//3][ij%3-1]
                Ntemp3[ij//3][ij%3-1]=8                
                for i in range(3):
                    for j in range(3):
                        s3.append(Ntemp3[i][j])
                s3.append(n)
                s3.append(h(s3))
            if ij%3<2:
                Ntemp4=copy.deepcopy([N[0:3],N[3:6],N[6:9]])
                Ntemp4[ij//3][ij%3]=Ntemp4[ij//3][ij%3+1]
                Ntemp4[ij//3][ij%3+1]=8                
                for i in range(3):
                    for j in range(3):
                        s4.append(Ntemp4[i][j])
                s4.append(n)
                s4.append(h(s4))
            if len(s1)!=0 and s1[:9] not in [i[0:9] for i in CLOSED]:
                s=copy.deepcopy(s1)
                OPEN.append(s)
            if len(s2)!=0 and s2[:9] not in [i[0:9] for i in CLOSED]:
                s=copy.deepcopy(s2)
                OPEN.append(s)
            if len(s3)!=0 and s3[:9] not in [i[0:9] for i in CLOSED]:
                s=copy.deepcopy(s3)
                OPEN.append(s)
            if len(s4)!=0 and s4[:9] not in [i[0:9] for i in CLOSED]:
                s=copy.deepcopy(s4)
                OPEN.append(s)      
            for i in range(len(OPEN)-1):
              for j in range(len(OPEN)-i-1):
                if OPEN[j][10]>=OPEN[j+1][10]:
                  OPEN[j],OPEN[j+1]=OPEN[j+1],OPEN[j]
            if len(OPEN)>5:
                OPEN=copy.deepcopy(OPEN[:5])