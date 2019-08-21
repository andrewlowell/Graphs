from util import Stack

islands = [
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1],
  [0, 0, 1, 0, 0],
  [1, 0, 1, 0, 0],
  [1, 1, 0, 0, 0]
]

# loop through each coordinate in the island map and find each "1" value
# 

visited = []
unvisited = []

for y in range(len(islands)):
  for x in range(len(islands[y])):
    if islands[y][x] == 1:
      unvisited.append((y, x))

found_islands = 0

while len(unvisited) > 0:
  s = Stack()
  first_new = unvisited.pop()
  s.push(first_new)

  while s.size() > 0:
    current = s.pop()
    visited.append(current)
    if current[2] == 0:
      if islands[current[0]+1][current[1]] == 1:
        s.push(islands[current[0]+1][current[1]])
      if islands[current[0]-1][current[1]] == 1:
        s.push(islands[current[0]-1][current[1]])
      if islands[current[0]][current[1]+1] == 1:
        s.push(islands[current[0]][current[1]+1])
      if islands[current[0]][current[1]-1] == 1:
        s.push(islands[current[0]][current[1]-1])

  found_islands += 1

print(found_islands)


