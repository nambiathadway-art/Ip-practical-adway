"""Practical 1 - Basics of Python: Variables, Constants and Data Types"""
from menu import run


def q1():
    """Variable creation and naming rules"""
    name, age, marks, city = "Asha", 18, 87.5, "Mumbai"
    print(name, age, marks, city)

    # Invalid names -> SyntaxError (exec lets us try them safely)
    for code in ["1name = 'Asha'", "class = 'FYBSc'", "my-name = 'Asha'"]:
        try:
            exec(code)
        except SyntaxError as e:
            print(f"{code:20} -> SyntaxError: {e.msg}")

    # Corrected versions
    name1 = "Asha"      # cannot START with a digit
    class_ = "FYBSc"    # 'class' is a reserved keyword
    my_name = "Asha"    # '-' is the minus operator, use '_'
    print(name1, class_, my_name)
    print("Rules: start with letter/_, only letters-digits-_, no keywords, case-sensitive")


def q2():
    """Dynamic typing"""
    x = 10
    print(x, type(x))
    x = "Ten"
    print(x, type(x))
    x = 10.5
    print(x, type(x))
    print("Python is dynamically typed: the TYPE belongs to the value, not the variable,")
    print("so one name can point to int, str, float later. Static languages (C, Java)")
    print("need the type declared once (int x;) and it cannot change.")


def q3():
    """Constants simulation"""
    PI = 3.14159
    GRAVITY = 9.8
    MAX_USERS = 100
    print(PI, GRAVITY, MAX_USERS)
    PI = 3  # Python does NOT stop this
    print("PI after change:", PI)

    # Convention: UPPERCASE name = "do not change". Stronger: a class that blocks changes
    class Constants:
        PI = 3.14159
        GRAVITY = 9.8
        MAX_USERS = 100

        def __setattr__(self, key, value):
            raise AttributeError("Constants cannot be changed")

    c = Constants()
    try:
        c.PI = 3
    except AttributeError as e:
        print("Blocked:", e)
    print("Python trusts the programmer ('we are all consenting adults'), so it has no const keyword.")


def q4():
    """Data type identification system"""
    i = int(input("Enter an integer: "))
    f = float(input("Enter a float: "))
    s = input("Enter a string: ")
    b = input("Enter a boolean (True/False): ").strip().lower() == "true"
    print(f"\n{'Value':<15}{'Type'}")
    print("-" * 30)
    for v in (i, f, s, b):
        print(f"{str(v):<15}{type(v).__name__}")


def q5():
    """Type conversion (casting)"""
    age_text = input("Enter age: ")
    marks_text = input("Enter marks: ")
    age = int(age_text)
    marks = float(marks_text)
    print("After casting: age + marks =", age + marks)
    print("Marks out of 100 =", marks / 100 * 100, "| age next year =", age + 1)
    try:
        print(age_text + 1)           # str + int
    except TypeError as e:
        print("Without conversion ->", e)
    print("Text + text only joins:", age_text + marks_text)


def q6():
    """Implicit vs explicit type conversion"""
    print("int + float:", 5 + 2.5, type(5 + 2.5).__name__, "(implicit: int promoted to float)")
    try:
        print(5 + "10")
    except TypeError as e:
        print("int + str ->", e)
    print("Fixed with int():", 5 + int("10"))
    print("Fixed with str():", str(5) + "10")
    print("Implicit rule: bool -> int -> float (smaller type is widened). str is never converted automatically.")


def q7():
    """Memory behaviour of variables (id)"""
    a = 10
    b = 10
    print("id(a) =", id(a), " id(b) =", id(b), " same object:", a is b)
    b = 20
    print("After b = 20 -> id(b) =", id(b), " a still", a)
    print("Immutable (int, str, tuple): value cannot change, a new object is made.")
    l1 = [1, 2, 3]
    l2 = l1
    l2.append(4)
    print("Mutable list: l1 =", l1, " l2 =", l2, " same object:", l1 is l2)


def q8():
    """Swapping variables"""
    a, b = 10, 20
    print("Before:", a, b)
    temp = a          # method 1: third variable
    a = b
    b = temp
    print("Third variable:", a, b)
    a, b = b, a       # method 2: tuple unpacking
    print("Tuple unpacking:", a, b)
    print("Tuple unpacking is shorter, needs no extra variable and is the Pythonic way.")


def _parse(text):
    for kind in (int, float):
        try:
            return kind(text)
        except ValueError:
            pass
    return text


def q9():
    """Data type based calculator"""
    x = _parse(input("Enter first value: "))
    y = _parse(input("Enter second value: "))
    print("Types:", type(x).__name__, type(y).__name__)
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        print("Addition:", x + y)
    elif isinstance(x, str) and isinstance(y, str):
        print("Concatenation:", x + y)
    else:
        print("Invalid: cannot combine a number with a string")


def q10():
    """Boolean logic and data types"""
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    is_adult = age > 18
    has_passed = marks > 50
    print(is_adult, has_passed, type(is_adult).__name__)
    if is_adult and has_passed:
        print("Adult and passed")
    elif has_passed:
        print("Passed but not an adult")
    else:
        print("Did not pass")


def q11():
    """Temperature converter"""
    c = float(input("Enter temperature in Celsius: "))
    f = c * 9 / 5 + 32
    print(f"{c:.1f} C = {f:.2f} F")


# ---------------- Practice questions ----------------
def pq1():
    """Invalid variable name"""
    print("Error: a variable name cannot start with a digit -> SyntaxError")
    name1 = "Python"       # corrected
    print(name1)


def pq2():
    """str + int error"""
    age = "18"
    print("Error: TypeError, cannot add str and int")
    print(int(age) + 5)    # 23


def pq3():
    """NameError"""
    marks = 95
    print("Error: NameError, total_marks was never defined (typo/undefined variable)")
    total_marks = marks    # fix: define it first (or print(marks))
    print(total_marks)


def pq4():
    """Boolean spelling"""
    print("Error: NameError - Python booleans are True/False (capital first letter)")
    is_pass = True
    print(is_pass)


def pq5():
    """int('12.5') error"""
    print("Error: ValueError - int() cannot parse a string containing a decimal point")
    num = int(float("12.5"))   # string -> float -> int
    print(num)                 # 12


def pq6():
    """Output: dynamic typing"""
    x = 10
    x = "Python"
    print(type(x))             # <class 'str'>


def pq7():
    """Output: int(a) + b"""
    a = "20"
    b = 5
    print(int(a) + b)          # 25


def pq8():
    """Output: swap"""
    a = 10
    b = 20
    a, b = b, a
    print(a, b)                # 20 10


def pq9():
    """Output: comparison"""
    age = 19
    print(age > 18)            # True


def pq10():
    """Output: Celsius to Fahrenheit"""
    c = 37
    f = (c * 9 / 5) + 32
    print(f)                   # 98.6


if __name__ == "__main__":
    run(globals(), "Practical 1 - Variables, Constants, Data Types")
