lst = [5,7,2,6,4,8,10,45,12,93, 13, 1]

def bubblsort(array):
    #accessing each element
    for i in range(len(array)):
        #comparing each element
        for j in range(0, len(array)-i-1):
            #compare
            if array[j]> array[j+1]:
                #Swaping element
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            
print('List before sorting', lst)
bubblsort(lst)
print('List after sorting', lst)
