# Python Variables and Data Types

## Variables

A variable is like a labeled box where you store a value. You create one by choosing a name and using `=` to assign a value:

```python
name = "Alice"
age = 25
height = 1.72
```

You don't need to declare the type — Python figures it out automatically from the value you assign.

**Naming rules:**
- Must start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Case-sensitive (`Age` and `age` are different variables)

---

## Basic Data Types

### 1. Integers (`int`) — whole numbers

```python
age = 25
score = -10
year = 2026
```

### 2. Floats (`float`) — decimal numbers

```python
height = 1.72
temperature = -3.5
price = 9.99
```

### 3. Strings (`str`) — text

```python
name = "Alice"
greeting = 'Hello, world!'
message = "I'm learning Python"
```

You can use either single quotes `'...'` or double quotes `"..."`.

### 4. Booleans (`bool`) — True or False

```python
is_student = True
has_license = False
```

### 5. None — represents "no value"

```python
result = None
```

---

## Checking the Type

Use `type()` to see what type a variable is:

```python
age = 25
print(type(age))       # <class 'int'>

name = "Alice"
print(type(name))      # <class 'str'>

height = 1.72
print(type(height))    # <class 'float'>

is_student = True
print(type(is_student))  # <class 'bool'>
```

---

## Variables Can Change

You can reassign a variable to a new value (even a different type):

```python
x = 10
print(x)    # 10

x = "hello"
print(x)    # hello
```

---

## Basic Operations

```python
# Math with numbers
a = 10
b = 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3  (integer division, rounds down)
print(a % b)    # 1  (remainder)

# Combining strings (concatenation)
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World

# Mixing strings and numbers (use f-strings)
name = "Alice"
age = 25
print(f"{name} is {age} years old")   # Alice is 25 years old
```

---

## Quick Summary

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole number |
| `float` | `3.14` | Decimal number |
| `str` | `"hello"` | Text |
| `bool` | `True` / `False` | Yes/No value |
| `None` | `None` | Empty/no value |
