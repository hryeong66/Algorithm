
# 크기 N이 주어지면 N*N 
# R, L, U, D 문자열이 주어지고
# 해당 위치로 이동한 좌표 출력

# 문자열 split, Counter로 R L U D 얼만큼 나왔는지 계산
# 해당 값들 만큼 좌표에 계산

from collections import Counter

def sol(n, point_str):
    point_list = point_str.split()
    point_dict = {"R": 1, "L": -1, "U": -1, "D": 1}
    current = [0,0]
    for item in point_list:
        if item == "D" and current[0] < n-1: current[0] += 1
        elif item == "U" and current[0] > 0: current[0] -= 1
        elif item == "L" and current[1] > 0: current[1] -= 1
        elif item == "R" and current[1] < n-1: current[1] += 1
        
    current[0] += 1
    current[1] += 1
    print(current)        

sol(5, "R R R U D D")

def solution(n, point_str):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    x, y = 1,1
    move_types = ['L', 'R', 'U', 'D']
    point_list = point_str.split()
    for item in point_list:
        for i in range(len(move_types)):
            if item == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    
    print(x, y)
    
        
solution(5, "R R R U D D")


