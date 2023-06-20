# Write your code here
import re

def correct_dates(string):
    def replace(match):
        m, d, y = match.groups()
        return f'{d}/{m}/{y}'
    return re.sub(r'(\d+)/(\d+)/(\d+)', replace, string)
