'''
    Backtracking

    1. Choices
    2. Constraints
    3. Goal



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
                             
                             #Easy version
                             '''
                             


'''_2dlist : list[list[int]] = [[0,0,6,0,8,0,4,0,0], \
                             [0,0,7,0,0,1,0,8,0], \
                             [0,0,0,4,5,0,0,0,0], \
                             [3,0,0,2,0,5,1,0,0], \
                             [2,0,0,0,0,6,0,9,0], \
                             [5,0,0,0,0,0,0,4,0], \
                             [0,0,9,0,0,2,0,1,0], \
                             [6,0,0,0,0,8,0,0,3], \
                             [0,0,0,0,0,0,0,0,0]]
                             # Extreme
'''

_2dlist : list[list[int]] = [[0,2,6,0,4,0,8,7,0], \
                             [0,0,0,7,0,6,5,3,9], \
                             [0,0,0,0,0,0,0,0,0], \
                             [6,4,3,9,5,2,7,1,8], \
                             [2,0,0,0,0,0,0,0,0], \
                             [0,0,0,0,0,0,0,0,0], \
                             [5,6,8,0,1,0,0,2,7], \
                             [3,9,2,6,7,8,1,4,5], \
                             [0,0,0,0,0,0,6,8,3]]
#This has a solution with first digit as 3 and 9

transform2lin = lambda a: a[0]*9+a[1]   
transform2list = lambda num: [int(num/9), int(num%9)]
changes : list[bool] = [True]
runs : int = 0
solutions: int = 0 

def digitAt(checkindex) -> int:
    return _2dlist[checkindex[0]][checkindex[1]]

def fillCell(fillindex, filldigit):
    _2dlist[fillindex[0]][fillindex[1]] = filldigit

    
def possible(curindex, digit) -> bool:

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
    
    subgridindex = 0
    for i in range(9):
        if subgrid[i].count(curindex) == 1:
            subgridindex = i
    counter = 0
    for pos in subgrid[subgridindex]:
        if _2dlist[pos[0]][pos[1]] == digit:
            counter += 1
    if counter > 0:
        #print("subgrid failure")
        return False

    return True

def puzzleValid() -> bool:
    grid : list[list[int]] = [[0 for i in range(9)] for j in range(9)]
    subgrid = [ [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
                [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
                [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
                [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
                [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
                [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
                [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
                [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
                [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]
    for i in range(9):
        for j in range(9):
            ind = [i,j]
            grid[i][j] = _2dlist[i][j]
            for digit in range(1,10):
                if grid[ind[0]].count(digit) > 1:
                    #print("row failure")
                    return False;
                counter = 0
                for c in range(9):
                    if grid[c][ind[1]] == digit:
                        counter += 1
                if counter > 1:
                    #print("col failure")
                    return False;
                
    
                subgridindex = 0
                for c in range(9):
                    if subgrid[c].count(ind) == 1:
                        subgridindex = i
                counter = 0
                for pos in subgrid[subgridindex]:
                    if grid[pos[0]][pos[1]] == digit:
                        counter += 1
                    if counter > 1:
                        #print("subgrid failure")
                        return False

    return True    
                

def solve():
    global solutions
    global runs
    runs+=1
    for i in range(9):
        for j in range(9):
            if _2dlist[i][j] ==0:
                ind = [i,j]
                for k in range(1,10):
                    if possible(ind,k):
                        _2dlist[i][j] = k
                        solve()
                        _2dlist[i][j] = 0
                return
    show()
    solutions+=1
    input("more?")
    
    
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
                    if possible(cur_index,i) == True:
                        decisions[counter].append(i)
                if len(decisions[counter]) == 1:
                    fillCell(cur_index,decisions[counter][0])
                    changes[0] = True
    else:
        pass

   

                
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
    if puzzleValid():
        if(changes[0] == False):
            pass
        else:
            while(changes[0] == True):
                traverse()
                
        if isSolved():
            pass
        else:
            show()
            print("With recursion")
            solve()
        print(f'{solutions} solutions')
        print(f'{runs} runs')
    else:
        print("|-----------------|")
        print("|Puzzle is invalid|")
        print("|-----------------|")

if __name__ == '__main__':
    main()