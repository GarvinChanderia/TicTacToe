v=[]
for i in range(3):
    l=[]
    for j in range(3):
        l.append("-")       
    v.append(l)
    print(l)

p1win=False
p2win=False
i=0
for i in range(9):

    if(i%2==0):
        print("P1 Enter Coordinates")
        x=int(input("Row no: "))
        y=int(input("Column no: "))
        if(v[x][y]!="O"):
            v[x][y]="X"
            i+=1
        else:
            print("Already in use")
        
    elif(i%2==1):
        print("P2 Enter Coordinates")
        x=int(input("Row no: "))
        y=int(input("Column no: "))
        if(v[x][y]!="X"):
            v[x][y]="O"
            i+=1
        else:
            print("Already in use")  

    if(v[0][0]=="X" and v[1][1]=="X" and v[2][2]=="X"):
        p1win=True
    if(v[0][2]=="X" and v[1][1]=="X" and v[2][0]=="X"):
        p1win=True
    for i in range(3):
        if(v[i][0]=="X" and v[i][1]=="X" and v[i][2]=="X"):
            p1win=True    
    for j in range(3):
        if(v[0][j]=="X" and v[1][j]=="X" and v[2][j]=="X"):
            p1win=True  
            
    if(v[0][0]=="O" and v[1][1]=="O" and v[2][2]=="O"):
        p2win=True
    if(v[0][2]=="O" and v[1][1]=="O" and v[2][0]=="O"):
        p2win=True
    for i in range(3):
        if(v[i][0]=="O" and v[i][1]=="O" and v[i][2]=="O"):
            p2win=True    
    for j in range(3):
        if(v[0][j]=="O" and v[1][j]=="O" and v[2][j]=="O"):
            p2win=True  
    if(p1win!=p2win):       
        break
    
    for i in range(3):
        print(v[i])    
if(p1win==True):
    print("P1 Wins")
elif(p2win==True):
    print("P2 Wins")
else:
    print("Tie")
for i in range(3):
        print(v[i])