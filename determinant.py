def det(A:list[list[int | float]]) -> int | float:
    if len(A) == 2 and len(A[0]) == 2 and len(A[1]) == 2:
        return (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])
    return sum([(A[0][i])*((-1)**i)*(det(minor(A,0,i))) for i in range(len(A))])



def minor(matrix: list[list[int | float]], i: int, j:int) -> list[list[int | float]]:
    new_matrix = []
    for ind in range(len(matrix)):
        if ind != i:
            new_matrix.append(matrix[ind].copy())
    for row in new_matrix:
        row.pop(j)
    return new_matrix


print(det([
    [1,3,2,-4],
    [0,1,2,-5],
    [2,7,6,-3],
    [-3,-10,-7,2]
]))
    
