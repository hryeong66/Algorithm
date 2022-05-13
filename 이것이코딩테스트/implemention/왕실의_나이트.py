
# 8X8
# 나이트 이동방식 => (수평 두칸, 수직 한칸) (수직 두칸, 수평 한칸)

def sol(start):
    y,x = start[0], start[1]
    y = ord(y) - 97
    x = int(x) - 1
    print(f"x,y = {x}, {y}")

    steps = [(-2,-1), (2, -1), (-2, 1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1,2) ]

    dx = [-2,+2,-2,+2,-1,-1,+1,+1]
    dy = [-1,-1,+1,+1,-2,+2,-2,+2]
    result = 0
    nx, ny = 0,0

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx <= 8 and ny <= 8: 
            result += 1
            print(nx, ny)
    print(result)

    
