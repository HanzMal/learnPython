# built-in functions like print()
name = input('What is your name? ') # User types "Kolade" and presses Enter  
print('Hello', name)

# own custom function
def hello():
    print('Hello World')
# Notice the indentation before print('Hello World'). The level of indentation defines a "code block" in Python, which is a group of statements that belong together.
hello()

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)