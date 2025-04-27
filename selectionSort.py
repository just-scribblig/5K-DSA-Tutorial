class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            temp = i
            for j in range(i+1, n):
                if arr[j] < arr[temp]:
                    temp = j
            if temp != i:
                arr[i], arr[temp] = arr[temp], arr[i]
        return arr
