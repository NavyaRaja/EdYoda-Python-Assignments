def get_rear(sub):
    return sub[-2]
 
test_list = ["great","hello","hiyo","abc"]
 
print("The original list is : " + str(test_list))
 
test_list.sort(key = get_rear)
 
print("Sorted List : " + str(test_list))