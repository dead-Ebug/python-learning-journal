# ==================================================
# FILE: while_loop.py
# PURPOSE: Day 3 - a while loop with a limit.
# ==================================================

attempts = 1          # scoreboard starts at 0, ABOVE the loop
max_attempts = 3      # the limit

# Keep looping while this condition is True.
while attempts <= max_attempts:
    attempts += 1     # update INSIDE the loop, or it never ends
    print(f"Connection attempt {attempts} of {max_attempts}...")

print("Gave up: too many attempts.")   # level 0: runs after the loop ends