import re

pattern = """
    ^
    (19|20)\d\d # start of string
    -
    (0[1-9]|1[012]) # Year
    -
    (0[1-9]|[12][0-9]|3[01]) # Day
    $
"""
text = '2022-07-12'
print(re.fullmatch(pattern, text, re.X))
