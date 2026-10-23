"""Practical 12 - Exception handling: try, except, else, finally, custom exceptions"""
from menu import run


def q1():
    """Basic try-except"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")


def q2():
    """Different error types"""
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("a / b =", a / b)
    except ValueError:
        print("Invalid input: please enter integers")
    except ZeroDivisionError:
        print("Division by zero is not allowed")


def q3():
    """else block"""
    try:
        a, b = int(input("a: ")), int(input("b: "))
        result = a / b
    except (ValueError, ZeroDivisionError):
        print("Error occurred")
    else:
        print("Division successful:", result)   # runs only when no exception


def q4():
    """finally block"""
    try:
        print("Opening file...")
        n = int(input("Enter a number: "))
        print("Processing", 10 / n)
    except Exception as e:
        print("Error:", e)
    finally:
        print("File closed")              # always runs


def q5():
    """Exception details"""
    for code in ("10 / 0", "int('abc')", "[1, 2][5]", "{'a': 1}['b']"):
        try:
            eval(code)
        except Exception as e:
            print(f"{code:15} -> {type(e).__name__}: {e}")


def q6():
    """Loop until valid input"""
    while True:
        try:
            n = int(input("Enter an integer: "))
            print("You entered", n)
            break
        except ValueError:
            print("Invalid, try again")


def q7():
    """User friendly messages"""
    try:
        a = float(input("Enter a number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter another number: "))
        if op not in "+-*/" or len(op) != 1:
            raise ValueError("operator")
        print("Result:", eval(f"{a}{op}{b}"))
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Oops! Please enter valid numbers and a valid operator.")


def q8():
    """raise keyword"""
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise Exception("Age must be 18 or above")
        print("Access granted")
    except Exception as e:
        print("Error:", e)


class InvalidMarksError(Exception):
    pass


def q9():
    """Custom exception"""
    try:
        marks = int(input("Enter marks: "))
        if marks > 100 or marks < 0:
            raise InvalidMarksError("Marks must be between 0 and 100")
        print("Valid marks:", marks)
    except InvalidMarksError as e:
        print("InvalidMarksError:", e)
    except ValueError:
        print("Enter a number")


def q10():
    """Bank withdrawal"""
    balance = 5000
    try:
        amount = float(input("Withdrawal amount: "))
        if amount > balance:
            raise ValueError("Insufficient balance")
        balance -= amount
        print("Withdrawal successful. Balance:", balance)
    except ValueError as e:
        print("Transaction failed:", e)


def q11():
    """Multiple except vs generic Exception"""
    print("Program A: multiple except blocks")
    try:
        int("abc")
    except ValueError:
        print("  Value error handled specifically")
    except ZeroDivisionError:
        print("  Zero division handled specifically")
    print("Program B: generic Exception")
    try:
        int("abc")
    except Exception as e:
        print("  Some error:", e)
    print("Specific blocks give precise messages; generic one catches everything but hides the cause")


def q12():
    """Nested try-except"""
    data = [10, 20, 30]
    try:
        n = int(input("Enter divisor: "))
        try:
            print("Result:", 100 / n)
            idx = int(input("Enter list index: "))
            print("Value:", data[idx])
        except ZeroDivisionError:
            print("Inner: division by zero")
        except IndexError:
            print("Inner: index out of range")
    except ValueError:
        print("Outer: invalid number")
    print("Flow: inner handler catches errors from the inner block first; anything it misses goes to the outer try.")


# ---------------- Practice questions ----------------
class LowBatteryError(Exception):
    pass


class DosageError(Exception):
    pass


class SuspiciousLoginError(Exception):
    pass


class LabelError(Exception):
    pass


def pq1():
    """Drone LowBatteryError"""
    try:
        battery = int(input("Battery %: "))
        if battery < 15:
            raise LowBatteryError("Battery below 15%, land immediately")
        print("Flight calculations safe")
    except LowBatteryError as e:
        print("Warning:", e)


def pq2():
    """Dosage validator"""
    try:
        age = int(input("Age: "))
        dose = float(input("Dosage (mg): "))
        if age < 1 or dose <= 0 or dose > 1000:
            raise DosageError("Invalid age or dosage")
        print("Dosage accepted")
    except DosageError as e:
        print("DosageError:", e)
    finally:
        print("Validation finished")


def pq3():
    """Login retry guard"""
    attempts = 0
    try:
        while True:
            if input("Password: ") == "secure123":
                print("Login successful")
                break
            attempts += 1
            if attempts == 3:
                raise SuspiciousLoginError("3 failed attempts")
    except SuspiciousLoginError as e:
        print("Alert:", e)
    finally:
        print("Login check complete")


def pq4():
    """Weather sensor handler"""
    try:
        with open("temps.txt") as f:
            values = [float(line) for line in f]
        if any(v < -100 for v in values):
            raise ValueError("sensor fault value below -100")
        print("Average:", sum(values) / len(values))
    except FileNotFoundError:
        print("Missing file")
    except ValueError as e:
        print("Invalid data:", e)
    except ZeroDivisionError:
        print("No readings to average")


def pq5():
    """Label validator"""
    labels = ["cat", "dog", "", "bird2", "cat", "cat"]
    seen = {}
    for lab in labels:
        try:
            if not lab.strip():
                raise LabelError("blank label")
            if any(c.isdigit() for c in lab):
                raise LabelError(f"digit in label {lab!r}")
            seen[lab] = seen.get(lab, 0) + 1
            if seen[lab] > 2:
                raise LabelError(f"duplicate label {lab!r} exceeds threshold")
        except LabelError as e:
            print("LabelError:", e)


def pq6():
    """Output"""
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Math Error")
    finally:
        print("Done")                  # Math Error / Done


def pq7():
    """Output"""
    try:
        num = int("25A")
    except ValueError:
        print("Invalid")
    else:
        print("Valid")
    finally:
        print("Closed")                # Invalid / Closed


def pq8():
    """Output"""
    try:
        data = [1, 2, 3]
        print(data[5])
    except IndexError:
        print("Out of Range")
    finally:
        print("Execution Complete")    # Out of Range / Execution Complete


def pq9():
    """Fill blanks"""
    try:
        num = 10 / 0
    except ZeroDivisionError:
        print("Division error")
    finally:
        print("Completed")


def pq10():
    """Fill blanks: user-defined exception"""
    class LowMarksError(Exception):
        pass
    marks = 25
    try:
        if marks < 35:
            raise LowMarksError("Fail")
    except LowMarksError as e:
        print(e)


if __name__ == "__main__":
    run(globals(), "Practical 12 - Exception Handling")
