""" Activity 1 """
"""
list1 = [ ]
n = int(input(" Enter the LENGHT OF THE LIST1 : " ))
for i in range(0 , n ):
  num = int (input(" Enter the numbers : " ))
  list1.append(num)


list2 = []
m = int (input( " Enter the lenght of the list2 : " ))

for i in range (0 , m):
               
                num1 = int (input(" Enter the numbers : " ))
                list2.append(num1)


list3 = list1 + list2 
print(list3)



 " Activity 2 "
n = input (" Enter the string : " )

def ispalindrome(n):
  return n == n[::-1]

 
ans = ispalindrome(n)
if ans :
  print(" Yes ")
else:
  print( " No ")
  
  

" Activity 3 "

arr1 = []
rows , col = 2,2
for i in range (rows):
  cols = []
  for j in range (col):
      n = int (input(" Enetr elements in matrix " ))
      cols.append(n)
  arr1.append (cols)




arr2 = []
rows , col = 2,2
for i in range (rows):
  cols = []
  for j in range (col):
      n = int (input(" Enetr elements in matrix " ))
      cols.append(n)
  arr2.append (cols)


arr3 = []
for i in range (2):
  arr3.append([])
  for j in range (2):
    arr3[i].append(0)
    for k in range (2):
      arr3[i][j]+= arr1[i][k]*arr2[k][j]
      
  


print (arr3)
 
              
 """

" Activity 4 "
mmh=[]
daa = []
n = int (input(" How many corners does polygon have : " ))
for i in range (0,n):
  mmh.append([])
  
  
  
  
  for j in range(2):
    ca = int (input(" Enter coordinates : " ))
    
    daa.append(ca)
    mmh.append(daa)
    daa.clear()
    


print (mmh)
    





























                
             










