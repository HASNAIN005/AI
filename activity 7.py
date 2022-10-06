i=5
ran =0
count=0
while ran!=100:
  n=int(input("ENTER YOUR NUMBER : "))
  if n>i:
    print(" too far ")
  elif n<i:
    print(" too close ")
  elif n==i:
    print(" matched ")
    
    ran=100

  count=count+1

  
print(" your no of trials are : " , count )
