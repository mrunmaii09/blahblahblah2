def solve(board,row,n):
    if row==n:
        print_board(board,n)
        print()
        return
    for col in range(n):
        if is_safe(board,col,row,n):
            board[row][col]=1
            solve(board,row+1,n)
            board[row][col]=0
def is_safe(board,col,row,n):
    for i in range(row):
        if board[i][col]==1:
            return False
    
    i,j = row,col
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    i,j = row,col
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True

def print_board(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
def main():
    n = int(input("enter the no of queens:"))
    board=[[0 for j in range(n)] for i in range(n)]
    solve(board,0,n)
if __name__ == "__main__":
    main()
                
