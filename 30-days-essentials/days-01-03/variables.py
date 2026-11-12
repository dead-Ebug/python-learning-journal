# ==================================================
# FILE: variables.py
# PURPOSE: Day 2 - variables and data types.
# ==================================================


# A variable is a labeled box that holds a value.
target_ip = "192.168.1.10"   # string (text), so it needs quotes
port = 443                   # integer (whole number), no quotes
timeout = 2.5                # float (decimal number)
is_open = True               # boolean: True or False (capital T/F!)

# type() tells you what kind of data a variable holds.
print(type(target_ip))
print(type(port))
print(type(timeout))
print(type(is_open))

# An f-string drops variables into text using {}.
print(f"Checking {target_ip} on port {port} (timeout {timeout}s)")