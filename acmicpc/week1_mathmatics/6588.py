import sys
import math
input = sys.stdin.readline

MAX_NUM = 1000000

prime_list = list(range(MAX_NUM + 1))
for i in range(2, int(math.sqrt(MAX_NUM)) + 1):
    if prime_list[i]:
        # i 가 소수일 경우 i+i(즉, i*2부터) i의 합(i * n)에 대하여 0으로 바꿔준다.
        prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

# filter(None, list) -> list 안에 있는 (0, False, None) 값 제거
prime_list = list(filter(None, prime_list[2:]))
# "in" 사용 시, set 함수의 경우 시간복잡도 O(1), list의 경우 O(n)
prime_set = set(prime_list)

# :=(바다코끼리 연산자/Walrus operator, Python 3.8부터 지원) 값을 할당함과 동시에 반환, 여기서는 0 입력 시 False가 되므로 종료 
while num := int(input()):
    for set_num in prime_list:
        ans = num - set_num
        if ans in prime_set:
            print("{} = {} + {}".format(num, set_num, ans))
            break
    
    else:
        print("Goldbach's conjecture is wrong.")
