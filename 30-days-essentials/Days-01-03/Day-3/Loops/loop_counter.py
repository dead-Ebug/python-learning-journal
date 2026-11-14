# ==================================================
# FILE: loop_counter.py
# PURPOSE: Day 3 - counters inside loops.
# ==================================================

# Version 1: scoreboard set to 0 ONCE, before the loop.
count = 0
for port in [80, 443, 22]:
    count += 1
print(f"Version 1: {count}")

# Version 2 (the bug): scoreboard wiped on EVERY pass.
for port in [80, 443, 22]:
    bad_count = 0
    bad_count += 1
print(f"Version 2: {bad_count}")