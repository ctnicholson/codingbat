def middle_way(a, b):
  new = []
  new.append(a[1])
  new.append(b[1])
  return new 
# other method
#  return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))