def is_palindrome(n):
    return str(n) == str(n)[::-1]

def answer():
    max_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome

if __name__ == "__main__":
    result = answer()
    print("The largest palindrome made from the product of two 3 digit numbers is: ", result)