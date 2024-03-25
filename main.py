def findDup(arr):
    # Find the duplicate number in the array
    # arr: List[int]
    # return: int
    list1 = []
    # Your code here
    for i in range(len(arr)):
        #compare the first element with the rest of the elements
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                list1.append(arr[i])
    return list1

#make a list with several duplicate numbers
arr = [1, 2, 6, 7, 8, 9, 1, 2, 3, 6, 7, 8, 9]
print(findDup(arr))


