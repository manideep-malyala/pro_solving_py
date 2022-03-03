# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1/?page=1&category[]=Arrays&sortBy=submissions

def duplicates(self, arr, n): 
    model = { x:0 for x in range(n)}
    for ele in arr:
        model[ele] = model.get(ele, 0)+1
    res = []
    for key in model:
        if model[key]>1:
           res.append(key)  
    return res if len(res)>0 else [-1]
  
