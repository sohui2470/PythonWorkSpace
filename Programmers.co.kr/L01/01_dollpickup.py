# def solution(board, moves):
#     blanket = []
#     answer = 0
#     for m in moves:
#         for j in range(len(board)):
#             if (board[j][m-1] == 0):
#                 floor = j+1
#         if floor < len(board):
#             blanket.append(board[floor][m-1])
#             for b in range(len(blanket)-1):
#                 if blanket[b] == blanket[b+1]:
#                     answer += 2
#                     blanket.pop()
#                     blanket.pop()
#             board[floor][m-1] = 0
#     return answer

def solution(board, moves):
    answer = 0
    blanket = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                blanket.append(board[i][j-1])
                board[i][j-1] = 0
                for k in range(len(blanket)-1):
                    if blanket[k] == blanket [k+1]:
                        answer += 2
                        blanket.pop()
                        blanket.pop()
                break
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))