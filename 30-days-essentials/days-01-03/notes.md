# Beginner Python Notes: The Core Basics

---

## 1. What is a Function? (`print`)
* **Analogy:** Think of a function like a vending machine button. You press it, feed it something, and it performs a specific job.
* **How it works:** `print("Hello")` 
  * `print` is the function name.
  * Its only job is to display whatever is inside the parentheses onto your terminal screen.

---

## 2. What are Strings? (`" "`)
* **Analogy:** A string is just regular text wrapped in quotation marks, like gift wrapping paper.
* **How it works:** Quotation marks tell Python, *"Treat this content as plain text, not as a command, variable, or math calculation."*
* **Examples:**
  * `"Hello World"` $\rightarrow$ A **string** (text)
  * `123` $\rightarrow$ A **number** (integer)
  * `"123"` $\rightarrow$ A **string** (because the quotes wrap it!)

---

## 3. What is a Variable?
* **Analogy:** A variable is a labeled storage box in your room. You place an item inside the box, put a sticky label on the outside, and reference the label whenever you need to find that item again.
* **Code Example:**
  ```python
  agent_name = "Alice"   # Stores the text "Alice" inside a box labeled 'agent_name'
  print(agent_name)      # Python opens the box and displays "Alice"