# Regular Expression

import re 

text="I attended Disha Computer Institute for programming courses."

search_text="Disha Computer Institute"

pattern=re.compile(re.escape(search_text),re.IGNORECASE)

match=pattern.search(text)

if match:
    print(f"Found {match.group()}")
else:
    print("Not Found")
