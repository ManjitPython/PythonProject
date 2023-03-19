# import re
#
# text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern in the text
import re

text = "Phone number: 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

result = re.search(pattern, text)
if result:
    print("Found:", result.group())
else:
    print("Not found")
# Output: Found: 123-456-7890
