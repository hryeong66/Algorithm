# 행에서 카드를 한장 뽑을 때, 행에서는 가장 작은 수지만, 가장 작은 수 중 큰수 뽑기

"""
정렬로만으로 풀 수 있을 것 같음
2차원 배열을 각각 정렬

"""

#n, m = map(int, input().split())

def sol(n,m, cards):
    sorted_list = []
    for list in cards:
        sorted_list.append(sorted(list))
    sorted_list.sort(key=lambda x: x[0])
    return sorted_list[-1][0]

# 예시를 본 후 개선
def sol2(n,m, cards):
    result = 0
    for list in cards:
        min_value = min(list)
        result = max(result, min_value)
    return result


metrix = [[3,1,2], [4,1,4,], [2,2,2]]
print(sol(3,3, metrix))

metrix = [[7,3,1,8], [3,3,3,4]]
print(sol2(2,4, metrix))


# 예시 1
n,m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


