def find3Numbers(arr, n, sum):
    arr.sort()
 
    for i in range(0, n-2):
     
        l = i + 1
        r = n-1
        
        while (l < r):
         
            if( arr[i] + arr[l] + arr[r] == sum):
                print("Triplet is", A[i], ', ', A[l], ', ', A[r]);
                return True
             
            elif (arr[i] + arr[l] + arr[r] < sum):
                l += 1
            else: 
                r -= 1
 
    return False
 
# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
 
find3Numbers(A, arr_size, sum)