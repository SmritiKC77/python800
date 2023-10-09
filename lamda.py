# jun function ko name hudaina teslai anonymous function vanxa or lambda function vanxa
# dunders lai magic method vanxa
import random
random.seed(0)
signal = [random.randint(1,25) for i in range(10)]
print(signal)

# labda function is used with map(lambda_function,list) and filter(lambda_function,list)
# Syntax: lambda argument: Expression
odd = filter(lambda x : x %2 == 1, signal) # x chai lambda function ko argument ho
even = filter(lambda x : x %2 == 0, signal)
print(f"The odd numbers are:{list(odd)}")
print(f"The even numbers are:{list(even)}")

squares = map(lambda x : x**2 ,signal)
print(f"The squares are :{list(squares)}")