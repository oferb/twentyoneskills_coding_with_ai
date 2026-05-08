# Python Control Structures

Control structures let you control the **flow** of your program — deciding which code runs, and how many times.

---

## 1. Conditional Statements (if / elif / else)

These let your program make decisions.

### Basic if

```python
age = 18

if age >= 18:
    print("You are an adult")
```

The indented code only runs if the condition is `True`.

### if / else

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### if / elif / else

Use `elif` (short for "else if") to check multiple conditions:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python checks each condition from top to bottom and runs the **first** one that is `True`.

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Logical Operators

Combine multiple conditions:

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

temperature = 35

if temperature < 0 or temperature > 40:
    print("Extreme weather!")

is_raining = False

if not is_raining:
    print("No umbrella needed")
```

| Operator | Meaning |
|----------|---------|
| `and` | Both must be True |
| `or` | At least one must be True |
| `not` | Flips True to False (and vice versa) |

---

## 2. Loops

Loops let you repeat code multiple times.

### for loop

Use `for` when you know what you're iterating over:

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
```

#### range() — loop a specific number of times

```python
# Print 0 to 4
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# Print 2 to 6
for i in range(2, 7):
    print(i)
# 2, 3, 4, 5, 6

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8
```

#### Looping through a string

```python
for letter in "Hello":
    print(letter)
# H, e, l, l, o
```

### while loop

Use `while` when you want to repeat **until** a condition becomes `False`:

```python
count = 0

while count < 5:
    print(count)
    count += 1
# 0, 1, 2, 3, 4
```

**Be careful!** If the condition never becomes `False`, you get an infinite loop. Always make sure something changes inside the loop.

#### Example: user input loop

```python
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
```

---

## 3. Loop Control: break, continue, pass

### break — exit the loop immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# 0, 1, 2, 3, 4
```

### continue — skip to the next iteration

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
# 0, 1, 2, 4, 5  (skips 3)
```

### pass — do nothing (placeholder)

```python
for i in range(5):
    if i == 3:
        pass  # TODO: handle this case later
    print(i)
# 0, 1, 2, 3, 4
```

---

## 4. Nested Structures

You can put control structures inside each other:

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

```python
numbers = [12, 5, 23, 8, 17, 3]

for num in numbers:
    if num > 10:
        print(f"{num} is big")
    else:
        print(f"{num} is small")
```

---

## 5. Practical Examples

### FizzBuzz (classic exercise)

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Sum of numbers

```python
total = 0

for i in range(1, 11):
    total += i

print(f"Sum of 1-10 is {total}")  # 55
```

### Find the first even number

```python
numbers = [7, 3, 9, 4, 11, 2]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
# First even number: 4
```

---

## Quick Summary

| Structure | Purpose |
|-----------|---------|
| `if / elif / else` | Make decisions |
| `for` loop | Repeat for each item in a sequence |
| `while` loop | Repeat until a condition is False |
| `break` | Exit a loop early |
| `continue` | Skip current iteration |
| `pass` | Do nothing (placeholder) |
