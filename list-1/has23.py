def has23(nums):
  #return "2" in nums or "3" in nums #this does not work
    return 2 in nums or 3 in nums
#why does the first one not work
print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))