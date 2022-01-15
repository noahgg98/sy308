
    
#function to complete assignment
def combine(l1, l2):
    newList = list()
    diff = len(l1) - len(l2)
    
    #add padding to shorter list if needed
    if diff < 0:
        [l1.append(0) for i in range(0, -1*diff)]
    elif diff > 0:
        [l2.append(0) for i in range(0, diff)]
        
        
    #create final list
    for x, y in zip(l1, l2):
        newList.append(x+y)
        
    return newList
    
if __name__=='__main__':
    
    #test 1
    print("Here is test 1: [1,1,1,1,2] [1,2,3,4]")
    print(combine([1,1,1,1,2],[1,2,3,4]))
    
    #test 2
    print("Here is test 2: [1,3,5] [4,4,4,4,4]")
    print(combine([1,3,5], [4,4,4,4,4]))
    
    #test3
    print("Here is test 3: [1,2,3] [4,5,6]")
    print(combine([1,2,3], [4,5,6]))

