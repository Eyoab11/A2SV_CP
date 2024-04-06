# Selection sort 1

class Solution: 
    def select(self, arr, i):
        # code here 
        minimum_index = i
        for num in range(i + 1, len(arr)):
            if arr[minimum_index] > arr[num]:
                minimum_index = num
        return minimum_index

            
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minimum_index = self.select(arr,i)
            arr[minimum_index], arr[i] = arr[i], arr[minimum_index]
            
        
