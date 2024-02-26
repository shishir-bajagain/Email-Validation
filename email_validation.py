import re

response = input("Enter your email: ")

pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,3}$")

match = pattern.search(response)

if match:
    print("Correct Email!!")
else:
    print("Incorrect Email")
