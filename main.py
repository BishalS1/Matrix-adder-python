

def getmat(row,column):
  matrix=[]
  for i in range(row):
    submatc = []
    for j in range(column):
      element = int(input(f"enter matrix of position {i+1}x{j+1}:"))
      submatc.append(element)

    matrix.append(submatc)

  return matrix




def addmat(row,column,matA,matB):
  addedmat = []
  for i in range(rows):
    addedrows=[]
    for j in range(column):
      element = matA[i][j]+matB[i][j]
      addedrows.append(element)

    addedmat.append(addedrows)

  return addedmat
  

  
rows = int(input("Enter no. of rows:"))
columns = int(input("Enter no. of column:"))

print("For matrix A")
A=getmat(rows,columns)
print("for matrix B")
B=getmat(rows,columns)
print("adding matrix")
result = addmat(rows,columns,A,B)

print("result matrix=",result)
