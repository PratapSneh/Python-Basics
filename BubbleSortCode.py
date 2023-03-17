#Sorting of list
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

##Sorting the list of Tupples in Increasing Order by the Last Element in Each Tuple

tpl_list= [(2,5) , (1,2), (2,3), (4,4), (2,1)]

def last(n):
    return n[-1]

def sort(tupples):
    return sorted(tupples, key = last)

print('List of tupple before sorting: \n', tpl_list)
print('List of tupple after sorting: \n ', sort(tpl_list))
