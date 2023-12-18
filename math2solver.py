def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solver(n, p=None, q=None):
    start = 10 ** (n-1)
    end = 10 ** n
    if p is not None and q is not None:
        start = p
        end = q
    elif p is not None:
        end = p
    largest_palindrome = 0
    
    for i in range(start, end):
        for j in range(start, end):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome


if __name__ == "__main__":
    print(solver(3))
    