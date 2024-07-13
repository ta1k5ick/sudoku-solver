
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

_2dlist : list[list[int]] = [[5,3,0,0,7,0,0,0,0], \
                             [6,0,0,0,0,0,0,0,0], \
                             [0,9,8,1,9,5,0,6,0], \
                             [8,0,0,0,6,0,0,0,3], \
                             [4,0,0,8,0,3,0,0,1], \
                             [7,0,0,0,2,0,0,0,6], \
                             [0,6,0,0,0,0,0,0,0], \
                             [0,0,0,4,1,9,0,0,5], \
                             [0,0,0,0,8,0,0,7,9]] \
                             





# Pseudocode
# changes made this traversal = True

# If changes made this traversal = False
    #Break
#Else
    # Traverse the sudoku

        #find next zero 
            # put every digit from 1 to 9 and validate_the_cell(row, col) the row, column and subgrid 
                # If validated, store it in object as '[row, col], (choices)' object

            # If choices length is 1, enter the choice in the sudoku using fill(row, col, rightDigit)
            # Set changes made this traversal = True 

        # if no zero found, sudoku solved
        # else if changes made this traversal is False 

    #If traversal ends with no changes made in traversal

def main():
    pass


if __name__ == '__main__':
    main()