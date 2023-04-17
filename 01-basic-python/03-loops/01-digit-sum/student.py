# Write your code here
def last_digit(n):
    return n%10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    x = 0
    while n > 0:
        x += last_digit(n)
        n= remove_last_digit(n)
    return x