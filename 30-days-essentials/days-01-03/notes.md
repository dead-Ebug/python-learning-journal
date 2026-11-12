#Python Fundamentals: Days 1 to 3 Master Notes

---

## Day 1: Introduction to Python & The Print Function

* **What is Python?**  
  * A high-level, interpreted programming language famous for its clean readability and simplicity.  
  * Widely used across web development, data analysis, artificial intelligence, and cybersecurity automation.  
  * Python executes code **line by line**, making it exceptionally beginner-friendly.

* **The `print()` Function**  
  * **Analogy:** Think of `print()` like a vending machine button. You press it, pass it a snack (data), and it pushes it out onto your terminal screen.  
  * **Code Example:**  
    ```python
    # This is a simple Python program that prints a message
    print("Hello, World!")
    ```

---

## Day 2: Variables and Data Types

* **What is a Variable?**  
  * **Analogy:** A labeled storage box in your room. You place data inside the box, write a label on it, and use that label whenever you need to find or modify the data later.  
  * **Dynamic Typing:** Python variables are dynamically typed, meaning the data type stored inside them can change during runtime.

* **Core Data Types in Python:**  
  * **Strings (Text):** Words or sentences wrapped in quotes.  
    * *Example:* `name = "John"` 

  * **Integers (Whole Numbers):** Positive or negative whole numbers without decimals.  
    * *Example:* `age = 30`  

  * **Floats (Decimal Numbers):** Numbers containing a fractional part or decimal point.  
    * *Example:* `height = 6.1`  

  * **Lists (Ordered Collections):** Mutable (changeable) lists of items enclosed in square brackets `[]`.  
    * *Example:* `fruits = ["apple", "banana", "cherry"]` 

  * **Tuples (Immutable Collections):** Similar to lists, but immutable (cannot be changed after creation) using parentheses `()`.  
    * *Example:* `point = (3, 4)`  
    
  * **Dictionaries (Key-Value Pairs):** Data stored as look-up keys and values using curly braces `{}`.  
    * *Example:* `person = {"name": "Alice", "age": 25}`

---

## Day 3: Conditional Statements and Loops

* **Conditional Statements (`if`, `elif`, `else`)**  
  * **Analogy:** A security checkpoint or a fork in the road. Your program checks if a condition is met; if yes, it executes a specific path. If not, it checks alternative options (`elif`) or falls back to a default path (`else`).  
  * **Code Example:**  
    ```python
    x = 10
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")
    ```

* **For Loops**  
  * Used to iterate or loop over a sequence (such as items in a list or characters in a string) one by one.  
  * **Code Example:**  
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("I love " + fruit)
    ```

* **While Loops**  
  * Continues executing a block of code over and over again as long as a specified condition remains `True`. (Watch out for infinite loops!)  
  * **Code Example:**  
    ```python
    count = 0
    while count < 5:
        print("Count: " + str(count))
        count += 1
    ```