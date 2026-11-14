# Breakdown Notes: loops.py

---

## What is Inside `loops.py`?
This script introduces **`for` loops** and **lists (`[]`)**. Up until now, our scripts checked only a single port at a time. By combining loops with our conditional logic (`if/elif/else`), our script transforms into an automated scanner that can inspect multiple ports in a fraction of a second.

---

## Core Breakdown of Concepts

### 1. Lists (`[]`)
* **What it is:** An ordered collection of items stored inside square brackets.
* **Analogy:** Think of a shopping list or a clipboard holding a specific sequence of items. 
* **Example:** `common_ports = [21, 22, 80, 443, 3389]`

### 2. The `for` Loop
* **What it does:** Iterates or loops through a sequence (like a list) one item at a time, running a block of code for each item.
* **Analogy:** Think of a security guard walking down a row of numbered doors, stopping at each door to check its lock before moving to the next one.
* **Syntax Breakdown:** `for port in common_ports:` means "take each item from the list one by one, temporarily call it `port`, and run the indented block below using that value."

### 3. Nested Blocks & Indentation
* **What it is:** Putting an `if/elif/else` statement *inside* a `for` loop.
* **The Rule:** Indentation determines where code lives. 
  * Lines indented under the `for` loop repeat for every item in the list.
  * Lines indented *even further* (nested under the `if` statements) only run when that specific condition matches.
  * Any unindented line at the very bottom (like `print("Done.")`) runs **only once** after the entire loop has finished.

---

## Explanation & Rules

* **Sequential Execution:** The loop handles items strictly in the order they appear inside the list.
* **Indentation is Syntax:** In Python, spaces are not just for visual neatness—they define your code blocks. Misplacing an indent will either change how many times code runs or crash your program entirely.

---

## Common Security Pitfalls & Warnings

### 1. Modifying a List While Looping Over It
* **The Mistake:** Trying to add or remove items from a list while your `for` loop is actively running through it.
* **Why it breaks:** It confuses Python's internal counter, causing it to skip items or throw unexpected bugs.

### 2. Indentation Errors on Final Statements
* **The Mistake:** Accidentally indenting your closing statement (like `print("Done.")`) so that it sits under the loop block.
* **Why it breaks:** Instead of printing "Done." once at the very end of the scan, Python will print "Done." repeatedly after *every single port* it checks!

---

## Tool Connection
Real-world port scanners like **Nmap** use this exact loop structure at scale. When you run a command like `nmap -p 21,22,80,443,3389 <target>`, that comma-separated list is the professional equivalent of our `common_ports` list! 

*(Ethical Reminder: Only ever scan machines you own or have explicit written permission to test.)*

---

## 🎯 Your Turn: Practice Exercises
Test your understanding and build your coding muscles with these exercises:

1. **Predict First:** Without running the code yet, how many times will the “Checking port...” line print? Which ports will trigger the "Not in my list yet" message?
2. **Test It:** Run the script and check your predictions.
3. **Hands-On Challenge:** Add two new `elif` branches inside your loop to handle:
   * **Port 21:** `FTP: file transfer, unencrypted`
   * **Port 3389:** `RDP: Windows remote desktop`
   *(If it throws an error or doesn't work, bring your code back here and I'll give you a hint instead of just giving you the answer!)*


   ## Counters (loop_counter.py)

### What is a counter?
A counter is a variable that keeps score while a loop runs. It starts at a number (usually 0) and goes up by 1 each time something happens. Counting events is how security analysts measure things like failed logins or unknown ports.

### Core Breakdown

**1. `count = 0` (the starting score)**
* Creates the variable and sets the scoreboard to 0.
* It goes **above** the loop so it only happens once.

**2. `count += 1` (add a point)**
* Short for `count = count + 1`: take what's in the box, add 1, put it back.
* It goes **inside** the loop so it happens on every pass (or only when a condition is true, like inside an `else`).

**3. `print(count)` (read the scoreboard)**
* Goes **after** the loop, unindented, so it shows the final score once.

**Analogy:** Three friends walk past a scoreboard. You write 0 on it before the game, and each friend adds 1 point. At the end it says 3.

### The Bug: `count = 0` inside the loop
```python
for port in [80, 443, 22]:
    bad_count = 0      # wipes the board on EVERY pass
    bad_count += 1
print(bad_count)       # prints 1, not 3
```
* Each pass erases the previous points, so the board only ever "sees" the last friend.
* **No error message appears.** Python does exactly what you wrote, so the answer is silently wrong.

### Rule to Remember
Starting value **above** the loop. Update **inside** the loop. Report **after** the loop.

### Tool Connection
Splunk and Wazuh do this at scale: they loop through millions of log lines and count events, such as failed logins per IP, to catch brute-force attacks.