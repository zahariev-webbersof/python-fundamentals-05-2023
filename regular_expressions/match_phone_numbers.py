import re

phone_numbers = input()
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

matches = re.findall(pattern, phone_numbers)

print(', '.join(matches))