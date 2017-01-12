# AI - ULTIMATE TIC-TAC-TOE
#SAURABH VASHISTH     201401040
#VENKAT PARTHASARATHY 201401180

import sys
import random
import signal
import copy

################################## MY FUNCTIONS ####################################

def get_empty_out(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		new_blal = []
		all_blal = [0,1,2,3,4,5,6,7,8]
		for i in all_blal:
			if block_stat[i]=='-':
				new_blal.append(i)

		for idb in new_blal:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))
	return cells

def determine_blocks(mv, blk):
	blocks_allowed = []
        if mv[0]==-1 and mv[1]==-1:
            blocks_allowed=[0,1,2,3,4,5,6,7,8]
        elif mv[0] % 3 == 0:
            if mv[1] % 3 == 0:
		blocks_allowed = [1,3]
            elif mv[1] % 3 == 1:
		blocks_allowed = [0,2]
            elif mv[1] % 3 == 2:
		blocks_allowed = [1,5]
        elif mv[0]%3==1:
            if mv[1] % 3 == 0:
		blocks_allowed = [0,6]
            elif mv[1] % 3 == 1:
		blocks_allowed = [4]
            elif mv[1] % 3 == 2:
		blocks_allowed = [2,8]
        elif mv[0]%3==2:
            if mv[1] % 3 == 0:
		blocks_allowed = [3,7]
            elif mv[1] % 3 == 1:
		blocks_allowed = [6,8]
            elif mv[1] % 3 == 2:
		blocks_allowed = [5,7]
	else:
		sys.exit(1)
	final = []
	for i in blocks_allowed:
		if blk[i] == '-':
			final.append(i)
	return final

def updateBlocksStatus(my_board,my_blocks,l_block):
    t=0
    for i in range(3):
        for j in range(3):
            if checkBoardFor(my_board,i,j,'x'):
                my_blocks[i][j]='x'
            elif checkBoardFor(my_board,i,j,'o'):
                my_blocks[i][j]='o'
            elif checkBoardFor(my_board,i,j,'D'):
                my_blocks[i][j]='D'
            else:
                my_blocks[i][j]='-'
            l_block[i*3+j]=my_blocks[i][j]


def checkBoardFor(arr,i,j,c):
    count=0
    if(c=='D'):
        for l in range(3):
            for m in range(3):
                if(arr[i*3+l][j*3+m]!='-'):
                    count+=1
        if count==9:
            return 1
        else:
            return 0
    
    count=0
    for l in range(3):
        count=0
        for m in range(3):
            if arr[i*3+l][j*3+m]==c:
                count+=1
        if(count==3):
            return 1

    for l in range(3):
        count=0
        for m in range(3):
            if arr[i*3+m][j*3+l]==c:
                count+=1
        if(count==3):
            return 1

    count=0
    for l in range(3):
        if arr[i*3+l][j*3+l]==c:
            count+=1
    if count==3:
        return 1

    count=0
    for l in range(3):
        if arr[i*3+2-l][j*3+l]==c:
            count+=1
    if count==3:
        return 1
    return 0

def counOfWins(arr,i,j,c):
    ret=0
    count=0
    for l in range(3):
        count=0
        for m in range(3):
            if arr[i*3+l][j*3+m]==c:
                count+=1
        if(count==3):
            ret+=1

    for l in range(3):
        count=0
        for m in range(3):
            if arr[i*3+m][j*3+l]==c:
                count+=1
        if(count==3):
            ret+=1

    count=0
    for l in range(3):
        if arr[i*3+l][j*3+l]==c:
            count+=1
    if count==3:
        ret+=1

    count=0
    for l in range(3):
        if arr[i*3+2-l][j*3+l]==c:
            count+=1
    if count==3:
        ret+=1
    return ret

def count2s(arr,c):
    cc='o'
    if cc==c:
        cc='x'
    i=0
    j=0
    VALUE_2=0
    VALUE_1=0
    li=[]
    for l in range(3):
        countc=countx=counts=0
        ll=[]
        for m in range(3):
            if arr[i*3+l][j*3+m]==c:
                countc+=1
            elif arr[i*3+l][j*3+m]==cc:       ################# change this character to opponent variable
                countx+=1
            elif arr[i*3+l][j*3+m]=='-':
                counts+=1
                ll.append((l,m))
        if(countc==2 and counts==1):
            li=li+ll
        if(countc==1 and counts==2):
            VALUE_1+=1

    li.sort()
    if len(li)>0:
        VALUE_2=max(VALUE_2,1)
    for k in range(len(li)-1):
        if li[k]!=li[k+1]:
            VALUE_2+=1

    li=[]
    for l in range(3):
        countc=countx=counts=0
        ll=[]
        for m in range(3):
            if arr[i*3+m][j*3+l]==c:
                countc+=1
            elif arr[i*3+m][j*3+l]==cc:
                countx+=1
            elif arr[i*3+m][j*3+l]=='-':
                counts+=1
                ll.append((l,m))
        if(countc==2 and counts==1):
            li=li+ll
        if(countc==1 and counts==2):
            VALUE_1+=1

    li.sort()
    if len(li)>0:
        VALUE_2=max(VALUE_2,1)
    for k in range(len(li)-1):
        if li[k]!=li[k+1]:
            VALUE_2+=1

    li=[]
    countc=countx=counts=0
    ll=[]
    for l in range(3):
        if arr[i*3+l][j*3+l]==c:
            countc+=1
        elif arr[i*3+l][j*3+l]==cc:
            countx+=1
        elif arr[i*3+l][j*3+l]:
            counts+=1
            ll.append((l,l))
    if(countc==2 and counts==1):
        li=li+ll
    if(countc==1 and counts==2):
        VALUE_1+=1

    li.sort()
    if len(li)>0:
        VALUE_2=max(VALUE_2,1)

    for k in range(len(li)-1):
        if li[k]!=li[k+1]:
            VALUE_2+=1


    li=[]
    countc=countx=counts=0
    ll=[]
    for l in range(3):
        if arr[i*3+2-l][j*3+l]==c:
            countc+=1
        elif arr[i*3+2-l][j*3+l]==cc:
            countx+=1
        elif arr[i*3+2-l][j*3+l]=='-':
            counts+=1
            ll.append((2-l,l))
    if(countc==2 and counts==1):
        li=li+ll
    if(countc==1 and counts==2):
        VALUE_1+=1

    li.sort()
    if len(li)>0:
        VALUE_2=max(VALUE_2,1)

    for k in range(len(li)-1):
        if li[k]!=li[k+1]:
            VALUE_2+=1

    return (VALUE_2,VALUE_1)


def utility75(arr,block_board,computer):
    opponent='x'
    if 'x'==computer:
        opponent='o'
    ANS=0
    
    if(block_board[1][1]==computer):
        ANS+=60
    if(block_board[1][1]==opponent):
        ANS-=60
    
    VALUE1=0 #NO OF BLOCKS
    WIN_BLOCK_VALUE=40 #40   #80
    FINAL_WIN=1e8
    BLOCK_WIN_2=100  #220
    BLOCK_WIN_1=40 #100

    ANS+=FINAL_WIN*counOfWins(block_board,0,0,computer)
    ANS+=-(FINAL_WIN)*counOfWins(block_board,0,0,opponent)

    (COUNT_2,COUNT_1)=count2s(block_board,computer)
    (XCOUNT_2,XCOUNT_1)=count2s(block_board,opponent)

    ANS+=COUNT_2*BLOCK_WIN_2
    ANS-=(XCOUNT_2)*BLOCK_WIN_2*0.75  

    ANS+=COUNT_1*BLOCK_WIN_1   
    ANS-=(XCOUNT_1)*BLOCK_WIN_1*0.75

    ONE_CELL_VALUE=10
    TWO_CELL_VALUE=15

    X_LOCK=20

    GAP_VALUE2=10
    GAP_VALUE=5 
    for i in range(3):
        for j in range(3):

            if block_board[i][j]==computer:
                VALUE1+=WIN_BLOCK_VALUE
            elif block_board[i][j]==opponent:
                VALUE1-=WIN_BLOCK_VALUE


            ##########################################
            
            VALUE_2=0
            VALUE_1=0
            for l in range(3):
                countc=countx=counts=0
                for m in range(3):
                    if arr[i*3+l][j*3+m]==computer:
                        countc+=1
                    elif arr[i*3+l][j*3+m]==opponent:     
                        countx+=1
                    elif arr[i*3+l][j*3+m]=='-':
                        counts+=1
                if(countc==2 and counts==1):
                    VALUE_2+=2#li=li+ll
                elif(countc==2):
                    VALUE_2+=1
                if(countc==1 and counts==2):
                    VALUE_1+=2
                elif(countc==1 and counts==1):
                    VALUE_1+=1
                if(countx==2 and countc==1):
                    VALUE_2+=2
                elif(countx==2 and counts==1):
                    ANS-=40

            
            for l in range(3):
                countc=countx=counts=0
                for m in range(3):
                    if arr[i*3+m][j*3+l]==computer:
                        countc+=1
                    elif arr[i*3+m][j*3+l]==opponent:
                        countx+=1
                    elif arr[i*3+m][j*3+l]=='-':
                        counts+=1
                if(countc==2 and counts==1):
                    VALUE_2+=2#li=li+ll
                elif(countc==2):
                    VALUE_2+=1
                if(countc==1 and counts==2):
                    VALUE_1+=2
                elif(countc==1 and counts==1):
                    VALUE_1+=1
                if(countx==2 and countc==1):
                    VALUE_2+=2
                elif(countx==2 and counts==1):
                    ANS-=40


            countc=countx=counts=0
            for l in range(3):
                if arr[i*3+l][j*3+l]==computer:
                    countc+=1
                elif arr[i*3+l][j*3+l]==opponent:
                    countx+=1
                elif arr[i*3+l][j*3+l]:
                    counts+=1
            if(countc==2 and counts==1):
                VALUE_2+=2#li=li+ll
            elif(countc==2):
                VALUE_2+=1
            if(countc==1 and counts==2):
                VALUE_1+=2
            elif(countc==1 and counts==1):
                VALUE_1+=1
            if(countx==2 and countc==1):
                VALUE_2+=2
            elif(countx==2 and counts==1):
                ANS-=40

            countc=countx=counts=0
            for l in range(3):
                if arr[i*3+2-l][j*3+l]==computer:
                    countc+=1
                elif arr[i*3+2-l][j*3+l]==opponent:
                    countx+=1
                elif arr[i*3+2-l][j*3+l]=='-':
                    counts+=1
            if(countc==2 and counts==1):
                VALUE_2+=2#li=li+ll
            elif(countc==2):
                VALUE_2+=1
            if(countc==1 and counts==2):
                VALUE_1+=2
            elif(countc==1 and counts==1):
                VALUE_1+=1
            if(countx==2 and countc==1):
                VALUE_2+=2
            elif(countx==2 and counts==1):
                ANS-=40

            
            ANS+=VALUE_1*ONE_CELL_VALUE
            ANS+=VALUE_2*TWO_CELL_VALUE
            
            ##############################################################################
    
                                    # ONE BLOCK GAP
            

            if(arr[i*3][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3][j*3]==computer and arr[i*3][j*3+2]==computer):
                ANS+=GAP_VALUE

            if(arr[i*3+2][j*3+2]==computer and arr[i*3][j*3+2]==computer and arr[i*3+1][j*3+2]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3+2][j*3+2]==computer and arr[i*3][j*3+2]==computer):
                ANS+=GAP_VALUE

            
            if(arr[i*3][j*3]==computer and arr[i*3+2][j*3]==computer and arr[i*3+1][j*3]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3][j*3]==computer and arr[i*3+2][j*3]==computer):
                ANS+=GAP_VALUE

            if(arr[i*3+2][j*3]==computer and arr[i*3+2][j*3+2]==computer and arr[i*3+2][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3+2][j*3]==computer and arr[i*3+2][j*3+2]==computer):
                ANS+=GAP_VALUE
            

            if(arr[i*3][j*3]==computer and arr[i*3+2][j*3+2]==computer and arr[i*3+1][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3][j*3]==computer and arr[i*3+2][j*3+2]==computer):
                ANS+=GAP_VALUE
            

            if(arr[i*3+2][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3+1][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3+2][j*3]==computer and arr[i*3][j*3+2]==computer):
                ANS+=GAP_VALUE

           
            if(arr[i*3+1][j*3]==computer and arr[i*3+1][j*3+2]==computer and arr[i*3+1][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3+1][j*3]==computer and arr[i*3+1][j*3+2]==computer):
                ANS+=GAP_VALUE


  
            if(arr[i*3][j*3+1]==computer and arr[i*3+2][j*3+1]==computer and arr[i*3+1][j*3+1]=='-'):
                ANS+=GAP_VALUE2
            elif(arr[i*3][j*3+1]==computer and arr[i*3+2][j*3+1]==computer):
                ANS+=GAP_VALUE

           

            ########################################################################

                                        # X-LOCK-CENTER

            t_count=0
            if(arr[i*3][j*3]==computer and arr[i*3+2][j*3]==computer and arr[i*3+1][j*3+1]==computer):
                if(arr[i*3+1][j*3]=='-'):
                    t_count+=1
                if(arr[i*3][j*3+2]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3+2]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK

            t_count=0
            if(arr[i*3][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3+1][j*3+1]==computer):
                if(arr[i*3][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3+2]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK

            
            t_count=0
            if(arr[i*3+2][j*3+2]==computer and arr[i*3][j*3+2]==computer and arr[i*3+1][j*3+1]==computer):
                if(arr[i*3+1][j*3+2]=='-'):
                    t_count+=1
                if(arr[i*3][j*3]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK


            t_count=0
            if(arr[i*3+2][j*3+2]==computer and arr[i*3+2][j*3]==computer and arr[i*3+1][j*3+1]==computer):
                if(arr[i*3+2][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3][j*3]=='-'):
                    t_count+=1
                if(arr[i*3][j*3+2]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK

                                    #CENTER
            ################################################################################## 
                                    
                                    #X-LOCK-CORNERS

            t_count=0
            if(arr[i*3][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3+2][j*3]==computer):
                if(arr[i*3+1][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3+1][j*3]=='-'):
                    t_count+=1
                if(arr[i*3][j*3+1]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK

           
            t_count=0
            if(arr[i*3][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3+2][j*3+2]==computer):
                if(arr[i*3+1][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3+1][j*3+2]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK


            t_count=0
            if(arr[i*3+2][j*3]==computer and arr[i*3][j*3+2]==computer and arr[i*3+2][j*3+2]==computer):
                if(arr[i*3+1][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3+1][j*3+2]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3+1]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK


            t_count=0
            if(arr[i*3+2][j*3]==computer and arr[i*3][j*3]==computer and arr[i*3+2][j*3+2]==computer):
                if(arr[i*3+1][j*3+1]=='-'):
                    t_count+=1
                if(arr[i*3+1][j*3]=='-'):
                    t_count+=1
                if(arr[i*3+2][j*3+1]=='-'):
                    t_count+=1
                if(t_count>=2):
                    ANS+=X_LOCK

            ######################################################################################### 


    ANS+=VALUE1
    return ANS


def minimax75(my_board,my_block,my_l_block,PLY_LIMIT,ply,my_turn,mv,ALPHA,BETA,computer):
    flag=0
    if my_turn&1:      ###character change  declare flag1 and flag2 such that you know whos move is next
        flag='o'
    else:
        flag='x'    
    
    if BETA<=ALPHA:
        if flag==computer:
            return (-1,-1,1e17)     ##change to 1e10
        else:
            return (-1,-1,-1e17)   ##change to -1e10
    

    allow_blk = determine_blocks(mv, my_l_block)
    allow_cell = get_empty_out(my_board, allow_blk,my_l_block)

    if flag==computer:
        temp_value=-1e15
    else:
        temp_value=1e15

    temp_a=-10
    temp_b=-10
    
    if len(allow_cell)==0:
        return (mv[0],mv[1],utility75(my_board,my_block,computer))
  
    if ply==PLY_LIMIT:
        for cell in allow_cell:
            my_board[cell[0]][cell[1]]=flag
            updateBlocksStatus(my_board,my_block,my_l_block)                        
            t=utility75(my_board,my_block,computer)
            if flag==computer:
                if temp_value<t:
                    temp_a=cell[0]
                    temp_b=cell[1]
                    temp_value=t
            else:
                if temp_value>t:
                    temp_a=cell[0]
                    temp_b=cell[1]
                    temp_value=t
            my_board[cell[0]][cell[1]]='-'
            updateBlocksStatus(my_board,my_block,my_l_block)
        return(temp_a,temp_b,temp_value)

    temp_a=-1
    temp_b=-1
    

    for cell in allow_cell:
        my_board[cell[0]][cell[1]]=flag
        updateBlocksStatus(my_board,my_block,my_l_block)                        
        (a,b,c)=minimax75(my_board,my_block,my_l_block,PLY_LIMIT,ply+1,my_turn+1,(cell[0],cell[1]),ALPHA,BETA,computer)
        if(flag==computer):
            if(temp_value<c):
                temp_a= cell[0]
                temp_b= cell[1]
                temp_value=c
                ALPHA=max(ALPHA,temp_value)
        else:
            if(temp_value>c):
                temp_a=cell[0]
                temp_b=cell[1]
                temp_value=c
                BETA=min(BETA,temp_value)
                      
        my_board[cell[0]][cell[1]]='-'
        updateBlocksStatus(my_board,my_block,my_l_block)
    return (temp_a,temp_b,temp_value)

def makemove75(board,l_block,mv,my_turn,computer):   #####  
    PLY_LIMIT=4
    new_block=[]
    new_board=copy.deepcopy(board)
    t=0
    for i in range(3):
        t_li=[]
        for j in range(3):
            t_li.append(l_block[t])
            t+=1
        new_block.append(t_li)
    new_l_block=copy.deepcopy(l_block)
    new_turn=my_turn
    
    allow_blk = determine_blocks(mv, l_block)
    allow_cell = get_empty_out(board, allow_blk,l_block)
    if(len(allow_cell)>36):
        PLY_LIMIT=3
    
    ALPHA=-1e10
    BETA=1e10
    a,b,val = minimax75(new_board,new_block,new_l_block,PLY_LIMIT,1,new_turn,mv,ALPHA,BETA,computer)
    return (a,b)

class Player75:
	
	def __init__(self):

                self.Board = []
                for i in range(9):
                    board_row=[]
                    for j in range(9):
                        board_row.append('-')
                    self.Board.append(board_row)
                
                self.Blocks=[]
                for i in range(3):
                    block_row=[]
                    for j in range(9):
                        block_row.append('-')
                    self.Blocks.append(block_row)
        

	def move(self,temp_board,temp_block,old_move,flag):
                if flag=='x':
                    turn=0
                else:
                    turn =1

                (a,b)=makemove75(temp_board,temp_block,old_move,turn,flag)
                return (a,b)

