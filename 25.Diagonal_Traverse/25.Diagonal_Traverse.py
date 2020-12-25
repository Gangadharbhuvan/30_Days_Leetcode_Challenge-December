'''
    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.


'''


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        levels = defaultdict(list)
        for i, j in product(range(m), range(n)):
            levels[i+j].append(matrix[i][j])
                
        out = []
        for lev in range(m + n):
            out += levels[lev][::lev%2*2-1]   
        return out