"""
Isai Medel Rios
10/23/2019
"""

def mergeSort(alist):  #implementing the sorting function
    
    if len(alist)>1:  #if the list has more an one item, it starts the splitting process
        mid = len(alist)//2  #finds the middle item in order to split the list in two halves
        lefthalf = alist[:mid]  #creates a new list named lefthalf that contains the first half of the list it's splitting
        righthalf = alist[mid:]  #creates a new list named righthalf that contains the second half of the list it's splitting

        mergeSort(lefthalf)  #repeats the splitting process in order to get a list of one item for lefthalf
        mergeSort(righthalf)  #repeats the splitting process in order to get a list of one item for righthalf

        i=0  #implementing counter i for lefthalf
        j=0  #implementing counter j for righthalf
        k=0  #implementing counter k to return new value to the corresponding position in original list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:  #compares to find the smallest of the two halves
                alist[k]=lefthalf[i]  #returns lefthalf[i] to the corresponding position k in original list if lefthalf is smaller
                i=i+1
            else:
                alist[k]=righthalf[j]  
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    

alist =  [12, 200, 45, 1, 57, 23]
mergeSort(alist)
print(alist)
