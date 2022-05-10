#가장 큰수, 그 다음 큰수를 M번, K번까지 연속해서 더할 수 있음

"""
1. 배열을 돌면서 first, second 큰 수를 찾음
2. first 값부터 반복, k번까지, 그러고 second,다시 k번
"""


def sol(m, k, input):
    input.sort()
    first, second = input[-1], input[-2]
    count = 0
    warnning = k
    result = 0
    while(count < m):
        if warnning == 0:
            result += second
            warnning = k
            count += 1
        else:
            result += first*k
            warnning -= k
            count += k
        print(result, k, count)
    return result

print(sol(8,3,[2,4,5,4,6]))


#예시 1
def solusion(n,m,k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    result = 0

    while(True):
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    return result
    

# 예시 2
def solusion2(n,m,k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    result = 0

    #가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k+1)) * k
    count += m % (k+1)
    result += count * first
    result += (m-count) * second
    return result