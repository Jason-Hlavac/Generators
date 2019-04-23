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
if (gen == 1):
    Fib(iterate, 1, 0)
elif(gen == 2):
    Geo(iterate)
elif(gen == 3):
    Square(iterate)
elif(gen == 4):
    Cube(iterate)
else:
    print("That is not a valid input")
print (numbers)
