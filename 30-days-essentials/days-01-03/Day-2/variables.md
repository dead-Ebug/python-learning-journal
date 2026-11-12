# Breakdown Notes: variables.py

---

## What is Inside `variables.py`?
This script introduces **variables** (storage boxes) and **data types** (the kind of data you put inside those boxes). In cybersecurity, we use variables constantly to track things like target IP addresses, port numbers, response timeouts, and whether a service is active or dead.

---

## Core Breakdown of Concepts

### 1. Variables and the Assignment Operator (`=`)
* **What it is:** A variable is a labeled storage box in your computer's memory. 
* **The `=` Sign:** In Python, `=` means **"store this value inside this name."** It is *not* a math equals sign. It always flows from right to left (taking what's on the right and saving it into the box name on the left).
* **Analogy:** Imagine writing "target_ip" on a cardboard box with a marker and dropping `"192.168.1.10"` inside. Whenever you need that IP later, you just look at the label (`target_ip`).

### 2. Core Data Types in the Script
Python looks at what you write and automatically figures out what kind of data it is (called **dynamic typing**):
* **String (`str` - Text):** Words, letters, or numbers wrapped in quotation marks. 
  * *Example:* `target_ip = "192.168.1.10"`
* **Integer (`int` - Whole Number):** Whole numbers without a decimal point. No quotes allowed!
  * *Example:* `port = 443`
* **Float (`float` - Decimal Number):** Numbers containing a decimal point, used for precision or measurements.
  * *Example:* `timeout = 2.5` (seconds)
* **Boolean (`bool` - True/False):** A binary flag that can only be `True` or `False`. **Crucial rule:** Python is case-sensitive, so it must start with a capital letter (`True`, not `true`).
  * *Example:* `is_open = True`

### 3. The `type()` Function
* **What it does:** Tells you the data type of whatever variable you hand it. 
* **Analogy:** It's like an X-ray scanner at airport security. You pass it a box, and it tells you exactly what kind of object is inside.
* **Example:** `print(type(port))` will output `<class 'int'>` on your screen because `port` holds a whole number.

### 4. f-strings (Formatted Strings)
* **What they do:** Allow you to inject variables directly into the middle of a sentence using curly braces `{}`.
* **Analogy:** Think of an f-string like a fill-in-the-blank security report template where Python automatically replaces the blanks with your variable values.
* **Code Example:** 
  ```python
  print(f"Checking {target_ip} on port {port}")
  # Output becomes: Checking 192.168.1.10 on port 443