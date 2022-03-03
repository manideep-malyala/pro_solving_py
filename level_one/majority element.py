def majorityElement(self, A, N):
    count = 0
    mE = 0
    for curr_ele in A:
        if count == 0:
           mE = curr_ele
            
        if mE == curr_ele:
           count+=1
        else:
           count-=1
                
     count = 0
     for eElem in A:
         if eElem == mE:
            count+=1
        
     mC = N//2
     return mE if count>mC else -1
