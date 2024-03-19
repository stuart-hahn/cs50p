import re

email = input("Enter email: ").strip()

if re.search(r"^(\w+\.)*\w+@(\w+\.)*\w+\.(com|org|co|edu|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
