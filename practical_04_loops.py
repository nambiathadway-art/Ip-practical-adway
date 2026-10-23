"""Practical 4 - Looping statements: for, while, nested loops"""
from menu import run


def q1():
    """for loop and range"""
    for i in range(1, 11):
        print(i, end=" ")
    print()
    for i in range(2, 11, 2):          # only even numbers
        print(i, end=" ")
    print()
    print("range(start, stop, step): starts at start, stops BEFORE stop, moves by step")


def q2():
    """while loop"""
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()
    print("for: used when the count is known; while: used when the condition decides")
    print("while needs manual initialisation and update (i += 1), for does it automatically")


def q3():
    """Sum and average"""
    n = int(input("How many numbers? "))
    total = 0
    for _ in range(n):
        total += float(input("Enter number: "))
    print("Sum =", total)
    print("Average =", total / n if n else 0)


def q4():
    """Factorial using for and while"""
    n = int(input("Enter a number: "))
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("Factorial (for):", f)
    f, i = 1, 1
    while i <= n:
        f *= i
        i += 1
    print("Factorial (while):", f)


def q5():
    """Multiplication table"""
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i:>2} = {n * i:>3}")


def q6():
    """Reverse number and palindrome"""
    n = int(input("Enter a number: "))
    original, rev = n, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print("Reverse:", rev)
    print("Palindrome" if rev == original else "Not a palindrome")


def q7():
    """Count digits, even and odd digits"""
    n = abs(int(input("Enter a number: ")))
    total = even = odd = 0
    for d in str(n):
        total += 1
        if int(d) % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Total digits:", total, "Even:", even, "Odd:", odd)


def q8():
    """Prime number checker"""
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not prime")
        return
    i = 2
    while i * i <= n:                  # optimisation: only check up to sqrt(n)
        if n % i == 0:
            print("Not prime (divisible by", i, ")")
            return
        i += 1
    print("Prime")


def q9():
    """Fibonacci series"""
    n = int(input("Number of terms: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b                # each term = sum of previous two
    print()


def q10():
    """Nested loop patterns"""
    print("(a) Star pattern")
    for i in range(1, 5):
        print("*" * i)
    print("(b) Reverse star pattern")
    for i in range(4, 0, -1):
        print("*" * i)
    print("(c) Number pattern")
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print("Reverse number pattern")
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# ---------------- Practice questions ----------------
def pq1():
    """range(1,10) misses 10"""
    print("Error: range stops BEFORE the stop value, so 10 is not printed")
    for i in range(1, 11):
        print(i, end=" ")
    print()


def pq2():
    """Output: range(1, 6)"""
    for i in range(1, 6):
        print(i)                       # 1 2 3 4 5 (each on a new line)


def pq3():
    """Nested loop indentation"""
    print("Error: print inside inner loop was not indented -> IndentationError")
    for i in range(3):
        for j in range(3):
            print("*")                 # indented under the inner loop


def pq4():
    """Fibonacci update error"""
    print("Error: after a = b, the line b = a + b uses the NEW a, giving b + b")
    a, b = 0, 1
    for _ in range(5):
        print(a, end=" ")
        a, b = b, a + b                # update both together
    print()


def pq5():
    """Infinite while loop"""
    print("Error: num is never increased, so num <= 5 is always True")
    num = 1
    while num <= 5:
        print(num)
        num += 1


def pq6():
    """Output: i * 2"""
    i = 1
    while i <= 5:
        print(i * 2)                   # 2 4 6 8 10
        i += 1


def pq7():
    """Output: factorial loop"""
    fact = 1
    for i in range(1, 5):
        fact *= i
    print(fact)                        # 24 (1*2*3*4, loop stops at 4)


def pq8():
    """Factorial logic error"""
    print("Error: fact starts at 0, so 0 * anything = 0. It must start at 1")
    n = 5
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)                        # 120


def pq9():
    """Output: Fibonacci"""
    a = 0
    b = 1
    for i in range(5):
        print(a, end=" ")
        a, b = b, a + b                # 0 1 1 2 3
    print()


def pq10():
    """Output: triangle"""
    for i in range(3):
        for j in range(i + 1):
            print("*", end="")
        print()                        # *  **  ***


if __name__ == "__main__":
    run(globals(), "Practical 4 - Loops")
