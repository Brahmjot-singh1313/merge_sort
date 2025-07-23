# function to merge sort the list.
def merge_sort(list3):
        # the function will work when the len of the entered array id longer than 1.
        if len(list3) > 1:
                # finding the midle of the array / list.
                mid = len(list3) // 2
                
                # creating two separate array's / lists.
                list1 = list3[:mid]
                list2 = list3[mid:]

                # calling the merge function recoversively to further devide the two created array's / lists to separate array's till their length is 1.
                merge_sort(list1)
                merge_sort(list2)

                # initialize three variables with value  of 0 to map the array from 0th index.
                i = j = k = 0

                # create a while loop which goes from the 0th index of the array to it's mid for both list's.
                while i < len(list1) and j < len(list2):
                        if list1[i] < list2[j]:
                                list3[k] = list1[i]
                                i += 1
                        else:
                                list3[k] = list2[j]
                                j += 1
                        k += 1
                        
                # creating a while loop for a case where the len of left array is larger than the right.
                while i < len(list1):
                        list3[k] = list1[i]
                        i += 1
                        k += 1

                # creating a while loop for a cse where the len of right array is larger than left.
                while j < len(list2):
                        list3[k] = list2[j]
                        j += 1
                        k += 1
        return list3

# calling the function.
print(merge_sort([10, 5, 7, 4, 2, 1, 0, 9, 8, 6, 3]))
