print("Lets do Property with getters and setters!")
class Circle:
    def __init__(self, radious):
        self._radious = radious

    @property
    def radious(self):
        return self._radious

    @radious.setter
    def radious(self, radious):
        if not isinstance(radious, int | float) or radious <= 0:
            raise Exception('Invalid number for radious, enter positive number!')
        self._radious = radious

circle_1 = Circle(10)
# this will result into error
# circle_1.radious = 0

print("Lets do Lambda!")
# Python code to use filter() with lambda()
lis = [5, 7, 22, 9, 54, 6, 77, 2, 73, 66]

final_li = list(filter(lambda x: (x%2 != 0) , lis))
print(final_li)
# Python code to use map() with lambda()
# to double each item in a list
li = [5, 7, 25, 97, 82, 19, 45, 23, 73, 57]

final_li = list(map(lambda x: x*2, li))
print(final_li)
# Try to write a lambda code that adds 12 to any number passed in the function as an argument.
# Also, use the lambda function to multiply one argument ‘a’ with another argument ‘b’.
add_12 =  lambda x: x +12
print(add_12(10))

mul_a_b =  lambda a, b: a * b
print(mul_a_b(10, 2))

print('decorators')
def decorators(function):
    def closure():
        print('this is before the function call')
        function()
        print('this is after the function call')

    return closure

@decorators
def greet():
    print('Hello World!')
greet()

print('generators')
nums = [num for num in [1, 2, 3, 4, 5] if num % 2 != 0]
print(nums)
def generator_yield(num):
    while num > 0:
        yield num
        num -= 1

numbers = generator_yield(5)
for num in numbers:
    print(num)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


fib = fibonacci_numbers(5)
for i in fib:
    print(i)
