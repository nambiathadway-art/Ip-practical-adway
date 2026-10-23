"""Practical 9 - User-defined and built-in functions, recursion"""
import time
from menu import run


def q1():
    """Define and call a function"""
    def show():
        print("Hello from a function!")
    show()
    show()
    show()
    print("Write once, reuse many times")


def q2():
    """Function with parameters"""
    def add(a, b):
        print("Sum =", a + b)
    add(10, 20)
    add(3.5, 1.5)


def q3():
    """Function with return value"""
    def square(n):
        return n * n
    result = square(7)
    print("Square:", result, "| used again:", result + 1)


def q4():
    """Default and keyword arguments"""
    def power(base, exp=2):
        return base ** exp
    print(power(5))                    # default exp=2 -> 25
    print(power(5, 3))                 # positional -> 125
    print(power(exp=3, base=2))        # keyword, order does not matter -> 8
    print("Positional: order matters; keyword: names are used; default: used when argument is skipped")


def q5():
    """Built-in functions vs manual"""
    nums = [4, 9, 2, 7]
    text = "python"
    print(len(nums), sum(nums), max(nums), min(nums))
    print(len(text), max(text), min(text))
    total, big = 0, nums[0]
    for n in nums:
        total += n
        if n > big:
            big = n
    print("Manual sum:", total, "manual max:", big, "(built-ins are shorter and faster)")


def q6():
    """List processing functions"""
    def list_sum(lst):
        total = 0
        for x in lst:
            total += x
        return total

    def largest(lst):
        big = lst[0]
        for x in lst:
            if x > big:
                big = x
        return big

    for data in ([1, 2, 3], [10, 50, 30], [-5, -2, -9]):
        print(data, "sum =", list_sum(data), "largest =", largest(data))


def q7():
    """Factorial: recursion vs loop"""
    def fact_rec(n):
        if n == 0 or n == 1:           # base case
            return 1
        return n * fact_rec(n - 1)     # recursive case

    def fact_loop(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    print("Recursive 5! =", fact_rec(5), "| Loop 5! =", fact_loop(5))
    print("Trace: fact(3) -> 3*fact(2) -> 3*2*fact(1) -> 3*2*1 = 6")


def q8():
    """Recursive Fibonacci vs iterative"""
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    print("Series:", [fib(i) for i in range(10)])
    t = time.time(); fib(25); r = time.time() - t
    t = time.time(); fib_iter(25); i = time.time() - t
    print(f"fib(25) recursive {r:.4f}s vs iterative {i:.6f}s")
    print("Recursive repeats the same calls (about 2^n calls); iterative does n steps")


def q9():
    """Function calling function"""
    def get_input():
        return int(input("Enter a number: "))

    def process(n):
        return n * n

    def show(result):
        print("Square =", result)

    def main():
        n = get_input()
        show(process(n))
    main()


def q10():
    """Variable scope"""
    global counter
    counter = 10                       # global variable

    def no_global():
        counter = 99                   # creates a NEW local variable
        print("Inside (local):", counter)

    def with_global():
        global counter
        counter += 5
        print("Inside (global changed):", counter)

    no_global()
    print("Outside after no_global:", counter)    # still 10
    with_global()
    print("Outside after with_global:", counter)  # 15


def q11():
    """Menu driven program"""
    def add():
        a, b = int(input("a: ")), int(input("b: "))
        print("Sum =", a + b)

    def is_prime():
        n = int(input("Number: "))
        print("Prime" if n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1)) else "Not prime")

    def factorial():
        n = int(input("Number: "))
        f = 1
        for i in range(2, n + 1):
            f *= i
        print("Factorial =", f)

    print("1. Addition\n2. Prime check\n3. Factorial")
    ch = input("Choice: ").strip()
    {"1": add, "2": is_prime, "3": factorial}.get(ch, lambda: print("Invalid choice"))()


def q12():
    """Student result system"""
    def input_marks():
        return [float(input(f"Marks of subject {i}: ")) for i in range(1, 4)]

    def calculate(marks):
        total = sum(marks)
        return total, total / len(marks)

    def grade(percent):
        if percent >= 90:
            return "A"
        if percent >= 75:
            return "B"
        if percent >= 50:
            return "C"
        return "Fail"

    marks = input_marks()
    total, percent = calculate(marks)
    print(f"Total = {total}, Percentage = {percent:.2f}%, Grade = {grade(percent)}")


# ---------------- Practice questions ----------------
def pq1():
    """Drone battery drop"""
    def analyse(battery):
        drops = [battery[i] - battery[i + 1] for i in range(len(battery) - 1)]
        avg = sum(drops) / len(drops)
        for hour, d in enumerate(drops, 1):
            if d > 5:
                print(f"Warning: drop of {d}% in hour {hour}")
        return avg
    print("Average drop per hour:", analyse([92, 88, 84, 79, 73, 68]))   # 4.8


def pq2():
    """BMI service"""
    def calculate_bmi(weight, height):
        bmi = weight / height ** 2
        if bmi < 18.5:
            return bmi, "Underweight"
        if bmi < 25:
            return bmi, "Normal"
        if bmi < 30:
            return bmi, "Overweight"
        return bmi, "Obese"
    bmi, cat = calculate_bmi(72, 1.75)
    print(f"BMI = {bmi:.2f}, Category = {cat}")


def pq3():
    """Recursive digit sum"""
    def digit_sum(n):
        return 0 if n == 0 else n % 10 + digit_sum(n // 10)
    print(digit_sum(482931))           # 27


def pq4():
    """Bill amount"""
    def bill_amount(price, discount, gst):
        after = price - price * discount / 100
        return after + after * gst / 100
    print(bill_amount(2500, 10, 18))   # 2655.0


def pq5():
    """Text sanitizer"""
    def sanitize(text):
        clean = " ".join(text.split()).lower()
        return clean, len(clean.split())
    print(sanitize("Python Makes AI Easy"))   # ('python makes ai easy', 4)


def pq6():
    """Output: add"""
    def add(a, b):
        return a + b
    print(add(5, 3))                   # 8


def pq7():
    """Output: default argument"""
    def greet(name="Student"):
        print("Hello", name)
    greet()                            # Hello Student


def pq8():
    """Output: recursion"""
    def fact(n):
        if n == 1:
            return 1
        return n * fact(n - 1)
    print(fact(4))                     # 24


def pq9():
    """Syntax error: missing colon"""
    print("Error: missing colon after def add(a, b)")
    def add(a, b):
        return a + b
    print(add(2, 3))


def pq10():
    """Indentation error"""
    print("Error: the body of the function must be indented")
    def square(x):
        print(x * x)
    square(5)


if __name__ == "__main__":
    run(globals(), "Practical 9 - Functions and Recursion")
