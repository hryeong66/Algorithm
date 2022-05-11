
# 0시 00분 00초 ~ N시 59분 59초
# 3이 하나라고 토함되는 모든 경우의 수 
# ex 00시 02분 03초

# 각자리에서 3이 들어갈 수 있는 기준
# 시가 3의 배수가 아닐때 
# 3*분~ -> 10*6*10
# *3분 -> 6*6*10
# 00분 3* -> 6*10*10
# 00분 *3 -> 6*10*6
# 
# 00시, 00분, 00초 -> N이 23시까지 가능
# 모든 경우의 수 24*60*60 => 86400
# O(n) -> 총 경우의 수 86400 *2  => 다 돌면서 계산해도 괜춘

def sol(num):
    per_time = 6*10*6*10 - 5*9*5*9 #1시간 당 3이 없는 분,초
    #시간 중에 3의 배수인 시가 들어가면 안됌, 3,6,9,12~~
    num -= (num // 3)
    num += 1
    print(num)
    print(num * per_time)

sol(5)
    
def solution(num):
    count = 0
    for i in range(int(num)+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)

solution("5")

