# ==================================================
# FILE: conditionals.py
# PURPOSE: Day 3 - decisions with if / elif / else.
# ==================================================

port = 443   # integer, no quotes

# == compares two values. A single = would STORE a value instead.
if port == 80:
    print("HTTP: web traffic, NOT encrypted")
elif port == 443:
    print("HTTPS: web traffic, encrypted")
elif port == 22:
    print("SSH: remote login")
else:
    print(f"Port {port}: not in my list yet")