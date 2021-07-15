import os, sys
dirName = os.getcwd()
sys.stdin = open(dirName + "\\input.txt", 'r')


N = int(input())
K = int(input())
applePoint = []
for i in range(K):
    applePoint.append(list(map(int,input().split())))
L = int(input())

movement = []
for i in range(L):
    movement.append(input().split())

snakeMap = [[0 for x in range(N)] for x in range(N)]

for i in range(K):
    snakeMap[applePoint[i][0]][applePoint[i][1]] = 1

snake_head = [0, 0]
snake_tail = [0, 0]

snakeMap[snake_head[0]][snake_head[1]] = 2
timeCount = 1

allDirection = [
    [0, 1],     # Right
    [-1, 0],     # Up
    [0, -1],    # Left
    [1, 0]     # Down
]
direction = allDirection[0]
direction.append(0)     # Direction Index Number

print(snakeMap)
print(applePoint)
print(movement)


for x, c in movement:
    if (snake_head[0] >= N) or (snake_head[1] >= N) or (snake_head[0] < 0) or (snake_head[1] < 0):
        break
    
    for i in range(int(x)):
        snake_head[0] += direction[0]
        snake_head[1] += direction[1]
        if (snake_head[0] >= N) or (snake_head[1] >= N) or (snake_head[0] < 0) or (snake_head[1] < 0):
            break

        if snakeMap[snake_head[0]][snake_head[1]] == 1:
            snakeMap[snake_head[0]][snake_head[1]] = 0
        elif snakeMap[snake_head[0]][snake_head[1]] == 2:
            break
        else:
            snakeMap[snake_head[0]][snake_head[1]] = 0
            snake_tail[0] += direction[0]
            snake_tail[1] += direction[1]
        
        snakeMap[snake_head[0]][snake_head[1]] = 2
        timeCount += 1
        
    if c == "L":
        if direction[2] == 3:
            direction = allDirection[0]
            direction.append(0)
        else:
            direction[2] += 1
            direction[0] = allDirection[direction[2]][0] 
            direction[1] = allDirection[direction[2]][1]
    else:
        if direction[2] == 0:
            direction = allDirection[3]
            direction.append(3)
        else:
            direction[2] -= 1
            direction[0] = allDirection[direction[2]][0] 
            direction[1] = allDirection[direction[2]][1]

print(timeCount)