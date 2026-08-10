import math

def distance_py(X: list[list[float]]) -> list[list[float]]:
    '''
    Computes the Euclidean distance using 'explicit' Python loops.
    Input: X which is a list of lists(A matrix) of N rows and d columns
    Output: D which is a list of lists of N rows and N columns.
    '''
    d = []
    for i in range(len(X)):
        d_i = []
        for j in range(len(X)):
            d_ij = 0
            for k in range(len(X[i])):
                d_ij += (X[i][k] - X[j][k])**2
            d_ij = math.sqrt(d_ij)
            d_i.append(d_ij)
        d.append(d_i)
    return d



N = int(input("Enter the number of input rows: "))

d = int(input("Enter the number of input columns: "))

# Give the input matrix X with N rows and d columns. Just for checking the working of code.
X = []
for i in range(N):
    x_ij = []
    for j in range(d):
        x = int(input(f"Enter the value of x{i+1}{j+1} element: "))
        x_ij.append(x)
    X.append(x_ij)
print(X)

D = distance_py(X)
print(D)


