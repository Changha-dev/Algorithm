#현재 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0

for step in steps:
  next_row = step[0] + row
  next_column = step[1] + column

  if 0 < next_row < 9 and 0 < next_column < 9:
    result += 1

print(result)


