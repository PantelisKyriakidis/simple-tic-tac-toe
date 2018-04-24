def show(matrix):
    for i in range (3):
        for j in range (3):
            print (matrix[i][j] + " | ",end="")
        print("\n")


def win(matrix):
    x_diag1=0
    x_diag2 =0
    o_diag1=0
    o_diag2 =0
    for i in range (3):
        x_row=0
        x_col=0
        o_row=0
        o_col=0        
        for j in range (3):
            if i==j:
                if matrix[i][j]=='X':                               #checking diagonal 1
                    x_diag1+=1
                    if x_diag1==3 : return 'X'
                elif matrix[i][j]=='O':
                    o_diag1+=1
                    if o_diag1==3 : return 'O'                      #--
                                             
            if (i==1 and j==1) or (i==0 and j==2) or (i==2 and j==0):      #checking diagonal 2
                if matrix[i][j]=='X':
                    x_diag2+=1
                    if x_diag2==3 : return 'X'
                elif matrix[i][j]=='O':
                    o_diag2+=1
                    if o_diag2==3 : return 'O'                      #--
                    
            if matrix[i][j]=='X' :          #checking i row
                x_row+=1;
                if x_row==3 : return 'X'
            elif matrix [i][j]=='O':
                o_row+=1;
                if o_row==3 : return 'O'    #--

            if matrix[j][i]=='X' :          #checking i column 
                x_col+=1;
                if x_col==3 : return 'X'
            elif matrix[j][i]=='O':
                o_col+=1;
                if o_row==3 : return 'O'    #--
    return 'none'
            

matrix= [["-" for x in range (3)]for y in range (3)]


print("hello users \nwhat are your names?? <3 ")

p1=input("player1: ")
while (True):
    p1c=input("X or O? : ")
    if(p1c == 'X') or (p1c == 'O'): break

p2=input("player2: ")
if p1c=='X' : p2c='O'
else: p2c='X'
print("Soo Mr " + p2 + " it seems that you are stuck with " + p2c + "s. \n\n\n")

print("Let the Game BEGINN!!! \n\n\n\n")
#Game Loop    
depth=0
while (True):
    show(matrix)
    print(p1 +"\nwhat is your move?")
    line=int(input('line: '))
    column=int(input('column: '))
    matrix[line-1][column-1]=p1c
    depth +=1
    
    winner=win(matrix)
    if depth==9:
        print("IT'S A FUCKING DRAW. YOU ARE LOSERS BOTH OF YOU")
        break
    
    if winner=='none':
        show(matrix)
        print(p2 +"\nwhat is your move?")
        line=int(input('line: '))
        column=int(input('column: '))
        matrix[line-1][column-1]=p2c
        depth+=1
        
        winner=win(matrix)
        
                
    if winner != 'none':
        if(p1c=='X'):
            if winner=='X':
                print(p1+ " is the WINNER\n"+p2+" SUCKS")
            else:
                print(p2+ " is the WINNER\n"+p1+" SUCKS")
        break

    
    

    


    
