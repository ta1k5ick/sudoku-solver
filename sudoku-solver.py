'''
    Backtracking

    1. Choices
    2. Constraints
    3. Goal



'''


'''
Random idea

list, tuple object where list stores row, col and tuple stores possible choices

'''

'''_2dlist : list[list[int]] = [[0,0,5,0,6,2,0,0,3], \
                             [0,0,0,1,0,5,2,9,0], \
                             [9,0,0,3,7,0,6,0,0], \
                             [6,0,2,5,3,1,0,4,0], \
                             [0,3,0,0,0,9,0,0,2], \
                             [0,4,9,0,0,7,1,0,0], \
                             [1,0,0,4,0,6,3,0,8], \
                             [0,9,6,0,0,8,0,0,7], \
                             [2,8,4,0,0,0,0,0,1]] 
                             
                             Easy version
                             
                             '''


_2dlist : list[list[int]] = [[0,0,6,0,8,0,4,0,0], \
                             [0,0,7,0,0,1,0,8,0], \
                             [0,0,0,4,5,0,0,0,0], \
                             [3,0,0,2,0,5,1,0,0], \
                             [2,0,0,0,0,6,0,9,0], \
                             [5,0,0,0,0,0,0,4,0], \
                             [0,0,9,0,0,2,0,1,0], \
                             [6,0,0,0,0,8,0,0,3], \
                             [0,0,0,0,0,0,0,0,0]]
                             # Extreme

'''_2dlist : list[list[int]] = [[0,2,6,0,4,0,8,7,0], \
                             [0,0,0,7,0,6,0,0,9], \
                             [0,0,0,0,0,0,0,0,0], \
                             [0,0,0,0,0,0,0,0,0], \
                             [0,0,0,0,0,0,0,0,0], \
                             [0,0,0,0,0,0,0,0,0], \
                             [5,6,8,0,1,0,0,2,7], \
                             [0,0,0,0,0,0,0,0,5], \
                             [0,0,0,0,0,0,0,0,3]]'''

transform2lin = lambda a: a[0]*9+a[1]   
transform2list = lambda num: [int(num/9), int(num%9)]
changes = [True]

runs = 0

# Pseudocode
# changes made this traversal = True

# If changes made this traversal = False
    #Break
#Else
    # Traverse the sudoku

        #find next zero 
            # put every digit from 1 to 9 and validate_the_cell(row, col) the row, column and subgrid 
                # If validated, store it in a list as [[row,col].[choices]]

            # If choices length is 1, enter the choice in the sudoku using fill(row, col, rightDigit)
            # Set changes made this traversal = True 

        # if no zero found, sudoku solved
        # else if changes made this traversal is False 

    #If traversal ends with no changes made in traversal

def digitAt(checkindex) -> int:
    return _2dlist[checkindex[0]][checkindex[1]]

def fillCell(fillindex, filldigit):
    _2dlist[fillindex[0]][fillindex[1]] = filldigit

def getNextCell(curindex) -> list[int]:
    rtrn : list[int] = [0,0]

    if curindex[0] <= 8 :
        if curindex[1] < 8:
            rtrn[0] = curindex[0]
            rtrn[1] = curindex[1] + 1
            return rtrn
        elif curindex[1] == 8 and curindex[0] == 8:
            rtrn = [-1,-1] 
        else:    
            rtrn[1] = 0
            rtrn[0] = curindex[0] + 1
    else:
        print("#2 happened")
        rtrn = [-1,-1]
    return rtrn
    
def validate(curindex, digit) -> bool:
    if _2dlist[curindex[0]].count(digit) != 0:
        #print("row failure")
        return False;
    counter = 0
    for i in range(9):
        if _2dlist[i][curindex[1]] == digit:
            counter += 1
        if counter > 0:
            #print("col failure")
            return False;
    subgrid = [ [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
                [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
                [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
                [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
                [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
                [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
                [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
                [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
                [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]
    
    subgrindindex = 0
    for i in range(9):
        if subgrid[i].count(curindex) == 1:
            subgrindindex = i
    counter = 0
    for pos in subgrid[subgrindindex]:
        if _2dlist[pos[0]][pos[1]] == digit:
            counter += 1
    if counter > 0:
        #print("subgrid failure")
        return False

    return True
        
def solve(curindex):
    global runs
    runs+=1
    if curindex.count(-1) !=1:    
        if digitAt(curindex) == 0:
            validnums=0
            for i in range(1,10):
                if validate(curindex,i) == True:
                    validnums +=1
                    fillCell(curindex,i)
                    solve(getNextCell(curindex))
                    if isSolved():
                        return    
                    fillCell(curindex,0)
                else:
                    pass
        else:
            solve(getNextCell(curindex))
            
    else: 
        return

def show():
    for i in _2dlist:
        print(i)
    print()
    print("-----------------------------------------------")
    print()


def traverse() -> None:
    if changes[0] == True:
        changes[0] = False
        decisions = {}
        for i in range(81):
            decisions[i]=[]
        for counter in range(81):    
            cur_index = transform2list(counter)
            zero_or_not = digitAt(cur_index) == 0
            if(zero_or_not == True):
                for i in range(1,10):
                    if validate(cur_index,i) == True:
                        decisions[counter].append(i)
                if len(decisions[counter]) == 1:
                    fillCell(cur_index,decisions[counter][0])
                    changes[0] = True
    else:
        print("Here? ")

   

                
def isSolved() -> bool:
    zcount = 0
    for counter in range(81):  
            cur_index = transform2list(counter)
            zero_or_not = digitAt(cur_index) == 0
            if(zero_or_not == True):
                zcount += 1
    if zcount == 0:
        return True
    return False

def main():
    global runs
    if(changes[0] == False):
        pass
        print("#1 happened! ")
    else:
        while(changes[0] == True):
            traverse()
            
    if isSolved():
        pass
    else:
        show()
        print("With recursion")
        solve([0,0])


    show()
    print(f'{runs} runs')


if __name__ == '__main__':
    main()