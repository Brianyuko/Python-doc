from player import Player

class Sorting(Player):
    
    def partition(arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[1][high]     # pivot 
    
        for j in range(low , high): 
            # If current element is smaller than the pivot 
            if   arr[1][j] < pivot: 
                # increment index of smaller element 
                i = i+1 
                arr[0][i],  arr[0][j] = arr[0][j],arr[0][i]
                arr[1][i],arr[1][j] = arr[1][j],arr[1][i]

        arr[0][i+1],arr[0][high] = arr[0][high],arr[0][i+1]
        arr[1][i+1],arr[1][high] = arr[1][high],arr[1][i+1] 
        return ( i+1 )
    
    def quick_sort(arr,low,high):
        if low < high: 
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = Sorting.partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition
            Sorting.quick_sort(arr, low, pi-1) 
            Sorting.quick_sort(arr, pi+1, high)
            