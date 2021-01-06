from bisect import bisect_left, bisect_right

n, x = map(int,input().split())
array = list(map(int,input().split()))

def count_by_range(array, left_value, right_value):
  index_left = bisect_left(array, left_value)
  index_right = bisect_right(array, right_value)
  return index_right - index_left

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)