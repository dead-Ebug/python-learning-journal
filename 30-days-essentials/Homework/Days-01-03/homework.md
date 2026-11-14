# Weekly Homework #1: Port Report

---

## Overview
Complete this homework assignment on your own between sessions, using only the core Python concepts you’ve learned so far (variables, lists, loops, and conditionals). 

Create a new file named **`port_report.py`** inside your repository to write your code.

---

## Part 1: Required Tasks
1. **Create a Port List:** Make a list of at least **8 ports**, ensuring your list includes ports `25`, `53`, `8080`, and `8443`.
2. **Loop & Identify:** Loop through your list of ports. For each port, use conditionals to print its corresponding service name if you know it (look up ports like SMTP, DNS, HTTP proxies, etc.). If the port is not in your recognized list, print `"unknown"`.
3. **Count the Unknowns:** Before your loop starts, create a counter variable (`unknown_count = 0`). Inside the loop, add `1` to this counter every time an unknown port is encountered (`unknown_count += 1`).
4. **Final Report:** After the loop finishes running, print the total number of unknown ports found.

---

## Part 2: The Data Type Trap (Required)
1. **Add a String Port:** Add one more item to your port list formatted as a string, such as `"22"`.
2. **Predict & Test:** Predict what will happen when your loop runs into a string instead of an integer, run the script, and write a short entry in your **`notes.md`** file detailing what you saw and *why* it happened.

---

## Part 3: Bonus Challenge (Optional)
If you want an extra coding challenge:
* Expand your conditional logic using `<` and `>` comparisons to check port ranges. 
* Print `"well-known"` for any ports below `1024`, and print `"registered"` for any ports `1024` and above.