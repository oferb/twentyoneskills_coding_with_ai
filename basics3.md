# Python Functions

A function is a reusable block of code that performs a specific task. Instead of writing the same code over and over, you write it once inside a function and call it whenever you need it.

---

## 1. Defining and Calling a Function

```python
def greet():
    print("Hello, world!")

greet()   # Hello, world!
greet()   # Hello, world!
greet()   # Hello, world!
```

- `def` — keyword that starts a function definition
- `greet` — the name you choose for your function
- `()` — parentheses (where parameters go)
- `:` — marks the start of the function body
- The indented lines are the function body

---

## 2. Parameters and Arguments

Parameters let you pass information into a function:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
```

### Multiple parameters

```python
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)    # 3 + 5 = 8
add(10, 20)  # 10 + 20 = 30
```

### Default values

You can give parameters a default value — if no argument is provided, the default is used:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!
```

### Keyword arguments

You can pass arguments by name for clarity:

```python
def describe_pet(name, animal="dog", age=1):
    print(f"{name} is a {animal}, {age} years old")

describe_pet("Rex")                          # Rex is a dog, 1 years old
describe_pet("Whiskers", animal="cat", age=3)  # Whiskers is a cat, 3 years old
describe_pet(age=5, name="Polly", animal="parrot")  # order doesn't matter
```

---

## 3. Return Values

Functions can send a result back using `return`:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

Without `return`, a function returns `None` by default:

```python
def greet(name):
    print(f"Hello, {name}!")

x = greet("Alice")   # Hello, Alice!
print(x)             # None
```

### Returning multiple values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([4, 7, 1, 9, 3])
print(f"Min: {lowest}, Max: {highest}")   # Min: 1, Max: 9
```

---

## 4. Scope — Where Variables Live

Variables created inside a function only exist inside that function:

```python
def my_function():
    secret = "hidden"
    print(secret)

my_function()     # hidden
print(secret)     # ERROR! secret doesn't exist out here
```

Variables outside a function are accessible inside (but can't be changed without `global`):

```python
name = "Alice"

def greet():
    print(f"Hello, {name}")   # Can read 'name'

greet()   # Hello, Alice
```

---

## 5. Practical Examples

### Calculate area of a rectangle

```python
def rectangle_area(width, height):
    return width * height

area = rectangle_area(5, 3)
print(f"Area: {area}")   # Area: 15
```

### Check if a number is even

```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
```

### Temperature converter

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(100))  # 212.0
print(fahrenheit_to_celsius(72))   # 22.22...
```

### Count vowels in a string

```python
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))   # 3
print(count_vowels("Python"))        # 1
```

### Factorial (a function calling itself — recursion)

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)
```

---

## 6. *args and **kwargs (Flexible Arguments)

### *args — accept any number of positional arguments

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))         # 6
print(total(10, 20, 30, 40))  # 100
```

### **kwargs — accept any number of keyword arguments

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Tel Aviv")
# name: Alice
# age: 25
# city: Tel Aviv
```

---

## 7. Lambda Functions (One-Liners)

For simple, short functions you can use `lambda`:

```python
double = lambda x: x * 2
print(double(5))   # 10

add = lambda a, b: a + b
print(add(3, 4))   # 7
```

Lambdas are often used with built-in functions like `sorted`:

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

by_grade = sorted(students, key=lambda s: s[1])
print(by_grade)   # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

---

## Quick Summary

| Concept | Example | Purpose |
|---------|---------|---------|
| `def` | `def greet():` | Define a function |
| Parameters | `def add(a, b):` | Accept input |
| `return` | `return a + b` | Send back a result |
| Default values | `def f(x=10):` | Optional parameters |
| `*args` | `def f(*args):` | Variable number of arguments |
| `**kwargs` | `def f(**kwargs):` | Variable keyword arguments |
| `lambda` | `lambda x: x * 2` | Quick one-line function |

---

## Key Takeaways

1. Functions help you **organize** code and **avoid repetition**
2. Use **parameters** to make functions flexible
3. Use **return** to get results back from a function
4. Keep functions **small** — each should do one thing well
5. Give functions **descriptive names** (verbs are good: `calculate_total`, `is_valid`, `get_user`)
