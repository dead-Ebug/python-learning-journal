# ==================================================
# FILE: loops.py
# PURPOSE: Day 3 - a for loop that checks many ports.
# ==================================================

# A list holds several values in order, inside [ ].
common_ports = [21, 22, 80, 443, 3389]

# The loop runs the indented block once per item.
# Each time, "port" holds the next value from the list.
for port in common_ports:
    print(f"Checking port {port}...")

    # An if/elif/else INSIDE the loop: indent one level deeper.
    if port == 80:
        print("  HTTP: web traffic, NOT encrypted")
    elif port == 443:
        print("  HTTPS: web traffic, encrypted")
    elif port == 22:
        print("  SSH: remote login")
    else:
        print("  Not in my list yet")

print("Done.")   # No indent, so this runs once, after the loop ends