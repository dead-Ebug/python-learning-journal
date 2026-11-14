# ==================================================
# FILE: port_report.py
# PURPOSE: This file labels and identifies network ports 
#          and gives you more information about them.
# ==================================================

# This here is Part 1 
# Make a list of at least 8 ports, including 25, 53, 8080, & 8443.
# Lets go ahead and create it.

port_list = [25, 53, 8080, 8443, 21, 22, 443, 3389, 2]
# Here i made sure to include the ones listed 25, 53, 8080, & 8443. 
# I also included 4 extra ports since part 1 asked for 8 ports in total.
# I also included 1 more port as an unknown that will be port 2

# Count the Unknowns: Before your loop starts, create a counter variable 
# (unknown_count = 0). Inside the loop, add 1 to this counter every time
# an unknown port is encountered (unknown_count += 1).
unknown_count = 0

# Next step is to Loop through them. For each 
# port, print the service name if you know it 
# (look them up: SMTP, DNS, etc.), otherwise print "unknown".

for port in port_list:
    print(f"Checking port {port}...")

# This part here is the counter loop that needs to go inside the loop.

    # Remember this one
    # An if/elif/else INSIDE the loop: indent one level deeper.
    if port == 25:
        print("  SMTP: simple mail transfer, unencrypted")
    elif port == 53:
        print("  DNS: domain name system, unencrypted")
    elif port == 8080:
        print("  HTTP: web proxy, unencrypted")
    elif port == 8443:
        print("  HTTPS: secure web server, encrypted")
    elif port == 21:
        print("  FTP: file transfer protocol, unencrypted")
    elif port == 22:
        print("  SSH: secure shell, encrypted")
    elif port == 443:
        print("  HTTPS: secure web server, encrypted")
    elif port == 3389:
        print("  RDP: remote desktop, encrypted")
    
    # This part here is the counter loop that needs to go inside the loop.
    else: 
        print("  unknown")
        unknown_count += 1

print(f"unknown ports found: {unknown_count}")
print("Done.")
    
