numbers = []
iterate = 0 
gen = input('''What kind of list do you want to generate(Select the corresponding number): 
1: Fibonacci Sequence 
2: Geometric Sequence  
3: Square Numbers
4: Cube Numbers 
''')
iterate = input("How many numbers do you want to generate in the list: ")
def Fib(times , curr, prev):
  curr = 1
  numbers.append(curr)
  for i in range(times):
     curr, prev = curr + prev, curr
     numbers.append(curr)
def Geo(times):
    curr = 1
    for i in range(times):
        numbers.append(curr)
        curr *= 2
def Square(times):
    for i in range(times):
        numbers.append(i**2)
def Cube(times):
    for i in range(times):
        numbers.append(i**3)
if (int(gen) == 1):
    Fib(int(iterate), 1, 0)
elif(int(gen) == 2):
    Geo(int(iterate))
elif(int(gen) == 3):
    Square(int(iterate))
elif(int(gen) == 4):
    Cube(int(iterate))
else:
    print("That is not a valid input")
print (numbers)
