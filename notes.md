# Advanced Python

What does advanced Python consist of? This course aims to answer that question and allow you to grow your Python and general programming skills through a series of exercises and 'lectures' that are no more than 20-30 minutes in length each.

## Overview and Clarifications

This course will cover several important concepts that can relate to programmers of any language, but it will do so using Python 3.1x (as of this writing in March 2024).

While some of these might seem simple, it is important to remember that programming concepts are generally simple but can get very complex as you add additional puzzle pieces to the mix. If you get stuck, try answering these questions:

* Do I understand the root issue, prompt, problem, etc. here?
* Can this issue be broken down into smaller pieces?
* Do I want to solve this linearly, funtionally, or programmatically?

Answering these can often help you look at the problem through a different lens, and in turn help you to solve the problem. Programming comes down to answering a complex series of yes/no questions to arrive at the desired result. If your prompt still has pieces that can be broken into smaller pieces, try to figure that out first before you start writing code. It can be helpful to write down your thoughts in comments before you start, with each comment being a reminder of what your next line(s) of code might be.

## Agenda

Each night covers an important topic, and each week wraps up with an exercise that encapsulates each of those topics. Building your code solutions is the only way that you will get better at writing code-- there is no substitute for placing fingers on keyboards and giving it a shot. Everyone will make mistakes, including you. Don't get discoraged, and if you need to, reach out to one of the many Python communities that are out on the web. The Python community is known for being open and helpful, so take advantage of that.

Flow control

* recap `if`, `elif`, `else`
* logical operators `and`, `or`, `not`
* truthy and falsey values

Advanced flow control

* nested conditionals
* `pass`, `continue`, `break`

Advanced loops

* list comprehensions
* generator expressions for memory efficiency
* `zip()` for parallels
* `enumerate() `for index-value pairs

## Night 1 Lesson

Python uses `if`, `elif` (else if), and `else` statements to control the flow of your program based on certain conditions.

 ***if statement:** Executes a block of code if a specified condition is true.

```
age = 18
if age >= 18:
  print("You are eligible to vote.")
```

 ***elif statement:** Provides an alternative condition to check if the original `if` condition is false. You can chain multiple `elif` statements.

```
grade = 85
if grade >= 90:
  print("Excellent!")
elif grade >= 80:
  print("Great job!")
```

 ***else statement:** Executes a block of code if none of the previous conditions are true (optional).

```
weather = "sunny"
if weather == "rainy":
  print("Bring an umbrella!")
else:
  print("Enjoy the weather!")
```

***Logical Operators**

Logical operators combine conditional statements to create more complex expressions.

***and:** Returns `True` only if both conditions are `True`.

```
age = 25
has_job = True

if age >= 18 and has_job:
  print("Eligible for a loan.")
```

***or:** Returns `True` if at least one condition is `True`.

```
is_morning = True
is_evening = False

if is_morning or is_evening:
  print("Time for coffee!")
```

***not:** Reverses the logical value of a condition.

```
is_member = False

if not is_member:
  print("Please sign up for membership.")
```

***Truthy and Falsey Values**

In Python, certain values are considered "truthy" while others are considered "falsey". These truth values determine how your code behaves in conditional statements.

***Truthy:** Values that evaluate to `True` in a conditional statement. These include non-zero numbers, non-empty strings, lists, dictionaries, and True itself.
***Falsey:** Values that evaluate to `False` in a conditional statement. These include 0, empty strings, `None`, and False itself.

Here's an example:

```
x = 0
if x:  # This will evaluate to False because 0 is a falsey value
  print("x is truthy")
else:
  print("x is falsey")
```

Understanding truthy and falsey values is crucial for writing concise conditional logic.

**Key Points:**

* Use `if`, `elif`, and `else` statements to make decisions based on conditions.
* Combine conditions using logical operators (`and`, `or`, `not`).
* Remember truthy and falsey values when evaluating conditions in your code.

### Night 1 Exercises

1. **Prime Number Checker:** Write a program that asks the user for a positive integer. Use a `while` loop to iterate through potential divisors (from 2 to the square root of the number). Inside the loop, use an `if` statement to check if the number is divisible by any number other than 1 and itself. If it is, the number is not prime. Finally, use another `if` statement outside the loop to determine if the number is prime and print an appropriate message. (Hint: You can use the modulo operator `%` to check divisibility)
2. **Text Analyzer:**  Write a program that reads a sentence from the user. Use a `for` loop to iterate through each character in the sentence. Inside the loop, use a combination of `if` statements to count the number of vowels, consonants, uppercase letters, lowercase letters, digits, and whitespace characters. Print a summary of the character counts.
3. **Password Validator:**  Write a program that simulates a password validator. Ask the user for a password. The password must meet the following criteria:

   * Be at least 8 characters long (use an `if` statement to check length)
   * Contain at least one uppercase letter, one lowercase letter, and one digit (use nested `if` statements to check each criteria)

   If the password meets all the criteria, print a message indicating a strong password. Otherwise, print specific messages indicating which criteria are not met. (Hint: You can use string methods like `isupper()`, `islower()`, and `isdigit()` to check character types)
4. **Number Guessing Game:** Write a program that plays a simple guessing game. Generate a random number between 1 and 100 (use the `random` module). Ask the user to guess the number. Use a `while` loop to keep asking for guesses until the user guesses the correct number. Inside the loop, use `if` statements to provide feedback to the user (e.g., "Higher", "Lower", "Correct!").
5. **Student Grade Analyzer:** Write a program that reads grades (integers between 0 and 100) from the user until they enter -1 (sentinel value). Use a `while` loop to keep reading grades. Inside the loop, use a combination of `if` statements to calculate the total number of students, the average grade, the number of students with A's (grades 90-100), B's (grades 80-89), and so on.  After the loop exits (when -1 is entered), print a summary of the grade analysis.

## Solutions
