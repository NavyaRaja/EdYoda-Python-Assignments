def find_len(list1):
    length = len(list1)
    list1.sort()
    print([list1[length-1],list1[0],list1[length-2],list1[1],list1[length-3],list1[2]])
list1=[1,2,3,4,5,6]
Largest = find_len(list1)