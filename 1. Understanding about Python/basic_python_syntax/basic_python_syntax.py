print("파이썬에 대한 이해")

# 루프 1
total = 0
for i in range(1,10+1):
    total += i
print(total)

# 루프 2
## python 내장함수 sum, abs, min, max, round, pow, divmod, eval - import math 없이 사용가능
total = sum(i for i in range(1,10+1))
print(total)

# 루프 3
## iterable generateor인 range가 sum 메서드 안에 들어갔으므로, sum은 알아서 iterable 객체를 돌며 그 값을 더한다
sum  = sum(range(1,10+1))