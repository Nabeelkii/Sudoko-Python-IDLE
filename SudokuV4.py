#Game
#Complete checking of solution
import random;
gameactive=True



ValuesDisplay=[]  #Option Values that are never changed
Values=[]         #Option Values that are used for input
Values1=["A","B","C","D","E","F","G","H","I"]
Values2=["1","2","3","4","5","6","7","8","9"]
Values3=[]        #List with raw numbers


for i in range(9):
    for j in range(9):
        Values.append(Values1[i]+Values2[j])
        ValuesDisplay.append(Values1[i]+Values2[j])



for i in range(81):
    Values3.append(0)


def Game():   
    while gameactive:
        Mainloop()
        
    
        
def Calculate():
    global gameactive
    win=False
    Checkvalue=[1,2,3,4,5,6,7,8,9]
    A=[];B=[];C=[];D=[];E=[];F=[];G=[];H=[];I=[];
    J=[];K=[];L=[];M=[];N=[];O=[];P=[];Q=[];R=[];
    B1=[];B2=[];B3=[];B4=[];B5=[];B6=[];B7=[];B8=[];B9=[];
    Masterlist=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,B1,B2,B3,B4,B5,B6,B7,B8,B9]
    for i in range(9):
        A.append(Values3[i])
        B.append(Values3[i+9])
        C.append(Values3[i+9*2])
        D.append(Values3[i+9*3])
        E.append(Values3[i+9*4])
        F.append(Values3[i+9*5])
        G.append(Values3[i+9*6])
        H.append(Values3[i+9*7])
        I.append(Values3[i+9*8])
        J.append(Values3[i*9])
        K.append(Values3[i*9+1])
        L.append(Values3[i*9+2])
        M.append(Values3[i*9+3])
        N.append(Values3[i*9+4])
        O.append(Values3[i*9+5])
        P.append(Values3[i*9+6])
        Q.append(Values3[i*9+7])
        R.append(Values3[i*9+8])

    B1=[A[0],A[1],A[2],B[0],B[1],B[2],C[0],C[1],C[2]]
    B2=[A[3],A[4],A[5],B[3],B[4],B[5],C[3],C[4],C[5]]
    B3=[A[6],A[7],A[8],B[6],B[7],B[8],C[6],C[7],C[8]]
    B4=[D[0],D[1],D[2],E[0],E[1],E[2],F[0],F[1],F[2]]
    B5=[D[3],D[4],D[5],E[3],E[4],E[5],F[3],F[4],F[5]]
    B6=[D[6],D[7],D[8],E[6],E[7],E[8],F[6],F[7],F[8]]
    B7=[G[0],G[1],G[2],H[0],H[1],H[2],I[0],I[1],I[2]]
    B8=[G[3],G[4],G[5],H[3],H[4],H[5],I[3],I[4],I[5]]
    B9=[G[6],G[7],G[8],H[6],H[7],H[8],I[6],I[7],I[8]]

    for i in range(len(Masterlist)):
        for j in range(9):
            if(Checkvalue[j] in Masterlist[i]):
                Masterlist[i].remove(Checkvalue[j])

    for i in range(len(Masterlist)):
        if(len(Masterlist[i])==0):
            win=True
        else:
            win=False

    
    if(win):
        print("YOU WIN")
        gameactive=False
    else:
        print("YOU FAILED")
        gameactive=False
       
    

def Showtable():
    global Values3
    global Values
    for i in range(9):
        print('')
        for j in range(9):
            print(str(Values3[j+9*i])+" ",end='')
    print('')
    
    for i in range(9):
        print('')
        for j in range(9):
            print(str(ValuesDisplay[j+9*i]) + " ",end='')
    print('')

   
    

def ShowValue():
    print("Welcome to the game")
    print("Below are the options to select points in the table")
    print("Type 'end' to end the game")


def Insert(x,y):
    global Values
    global Values3
    for i in range(81):
        if(x==Values[i]):
            Values3[i]=y

def ChangeDisplayValue(x):
    global Values
    for i in range(81):
        if(x==Values[i]):
            Values[i]='J'
    

def Checkoptions(x):
    Checked=False
    Inputs=[]
    Splits=[' ','=',',']
    j=0
    for i in range(len(x)):
        Inputs.append(x[i])
        i=i-j
        if(Inputs[i] in Splits):
            Inputs.remove(Inputs[i])
            j=j+1
    if(len(Inputs)<3):
        Checked=False
        print("Invalid option")
        Mainloop()
    elif(Inputs[0] in Values1 and Inputs[1] in Values2 and Inputs[2] in Values2):
        Insert(Inputs[0]+Inputs[1],Inputs[2])
        Checked=True
        Mainloop()
    if(Checked==False):
        print("Invalid option")
        Mainloop()
        

def Mainloop():
    Showtable()
    print("Pick an option, followed by a number")
    while gameactive==True:
        choice1=input()
        if(choice1=='end'):
            Calculate()
            return           
        else:
            Checkoptions(choice1)

def Randomize(R0):
    List1=['C3','A4','B7','F2','E5','D9','H1','I6','G8']
    List2=['A2','B5','C9','I1','G4','H8','E3','F6','D7']
    List3=['D3','E6','F8','I2','G5','H9','C1','B4','A7']
    List4=['C2','E1','H3','A6','D4','I5','B8','F7','G9']
    List5=['B3','D1','H2','C8','F9','I7','A5','E4','G6']
    List6=['C4','D5','H6','A9','E7','I8','B2','F1','G3']
    List7=['E2','A3','B6','G1','F5','C7','H4','I9','D8']
    List8=['G2','D6','B9','I4','H7','E8','A1','C5','F3']
    List9=['I3','F4','A8','H5','G7','E9','D2','B1','C6']
    List0=[List1,List2,List3,List4,List5,List6,List7,List8,List9]
    Numbers=[0,1,2,3,4,5,6,7,8]
    #R0=random.randint(5,7)
    print('Numbers generated:' + str(R0*9))
    for i in range(1,10):
        random.shuffle(Numbers)
        R1=random.randint(0,9-i)
        x=Numbers[R1]
        Numbers.remove(x)
        for j in range(0,R0):
            Insert(List0[x][j],i)
            #ChangeDisplayValue(List0[x][j]) #Remove ability to pick option
            
            
            
def MainMenu():
    print("Please Select Difficulty:")
    print("Easy")
    print("Medium")
    print("Hard")
    Selection=input()
    if(Selection=="Easy"):
        Randomize(7)
    elif(Selection=="Medium"):
        Randomize(6)
    elif(Selection=="Hard"):
        Randomize(5)
    elif(Selection=="Complete"):
        Randomize(9)
    elif(Selection=="Impossible"):
        Randomize(0)
        
    
            
ShowValue()
MainMenu()  
Game()

  

        

        
    

                 

    

