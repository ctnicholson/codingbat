def max_end3(nums):
    # new = []
    # if nums[0] > nums[1] and nums[0] > nums[-1]:
    #     list1 = nums[0], nums[0], nums[0]
    #     new.extend(list1)
    # elif nums[1] > nums[0] and nums[1] > nums[-1]:
    #     list2 = nums[1], nums[1], nums[1]
    #     new.extend(list2)
    # elif nums[-1] > nums[0] and nums[-1] > nums[1]:
    #     list3 = nums[-1], nums[-1], nums[-1]
    #     new.extend(list3)
    # return new 
# This is wrong, this just returns the highest value 

    new = []
    if nums[0] > nums[-1]:
        list1 = nums[0], nums[0], nums[0]
        new.extend(list1)
    elif nums[-1] > nums[0] :
        list2 = nums[-1], nums[-1], nums[-1]
        new.extend(list2)
    elif nums[-1] == nums[0]:
        list3 = nums[0], nums[0], nums[0] 
        new.extend(list3)
    return new 
# other solution
    # m = max(nums[0], nums[2])
    # nums[0] = m
    # nums[1] = m 
    # nums[2] = m
    # return nums 

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))