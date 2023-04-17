# Write your code here
import re

def is_valid_password(string):
    return all(re.search('[a-zA-Z0-9-+/.*@].\{12,}',string) and not any(re.search(r'(.)\1{2}',string)))