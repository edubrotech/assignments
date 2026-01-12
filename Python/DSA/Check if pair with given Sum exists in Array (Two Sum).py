def checkPair(arrayValue,sizeArrayValue,x):
    for i in range(0,sizeArrayValue-1):
        for j in (i+1,sizeArrayValue):
            if(arrayValue[i]+arrayValue[j]==x):
                return True
    return False
    
    
    
    
    


arrayValue=[-1,0,-2,2,1,-21,3]
x=-2
if(checkPair(arrayValue,x)):
    print("Yes");
else:
    print('No');

