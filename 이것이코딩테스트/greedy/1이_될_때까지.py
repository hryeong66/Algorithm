
# N이 1이 될때까지, k로 나누어 떨어지면 k로 나누고 아니라면 빼기 1

def sol(value, num):
    count = 0
    count += value % num
    value -= count
    print(count)
    while(value != 1):
        value /= num
        count += 1
    print(count)

sol(29, 5)
