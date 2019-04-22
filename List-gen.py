numbers = []
def Fib(times , curr, prev):
  curr = 1
  numbers.append(curr)
  for i in range(times):
     curr, prev = curr + prev, curr
     numbers.append(curr)
Fib(1000, 1, 0)
print(numbers)
