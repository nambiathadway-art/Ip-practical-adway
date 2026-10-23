"""Practical 2 - Input/Output operations and arithmetic expressions"""
import math
from menu import run


def q1():
    """Name and age: print vs f-string"""
    name = input("Enter name: ")
    age = input("Enter age: ")
    print("Hello", name, "you are", age, "years old")   # print adds spaces automatically
    print(f"Hello {name}, you are {age} years old")      # f-string: you control the spacing
    print("Both show the same text; f-string is cleaner and allows formatting like {x:.2f}.")


def q2():
    """Numeric input handling"""
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Without conversion, a + b =", a + b, "(joined as text!)")
    try:
        print(a - b)
    except TypeError as e:
        print("a - b ->", e)
    a, b = float(a), float(b)
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "cannot divide by zero")


def q3():
    """Sum, average and expression of three numbers"""
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print(f"Sum = {a + b + c}")
    print(f"Average = {(a + b + c) / 3:.2f}")
    print(f"(a + b) * c / 2 = {(a + b) * c / 2}")


def q4():
    """Operator precedence"""
    print("10 + 5 * 2     =", 10 + 5 * 2, " (* before +)")
    print("(10 + 5) * 2   =", (10 + 5) * 2, " (brackets first)")
    print("100 / 5 + 3 * 2 =", 100 / 5 + 3 * 2, " (/ and * before +, left to right; / gives float)")
    print("Order: () > ** > * / // % > + - ")


def q5():
    """Salary breakdown"""
    basic = float(input("Enter basic salary: "))
    hra = basic * 0.20
    da = basic * 0.10
    net = basic + hra + da
    print(f"{'Basic':<8}: {basic:>10.2f}")
    print(f"{'HRA 20%':<8}: {hra:>10.2f}")
    print(f"{'DA 10%':<8}: {da:>10.2f}")
    print("-" * 22)
    print(f"{'Net':<8}: {net:>10.2f}")


def q6():
    """Area and perimeter"""
    l = float(input("Rectangle length: "))
    w = float(input("Rectangle width: "))
    print(f"Rectangle area = {l * w:.2f}, perimeter = {2 * (l + w):.2f}")
    r = float(input("Circle radius: "))
    print(f"Circle area = {math.pi * r ** 2:.2f}, circumference = {2 * math.pi * r:.2f}")


def q7():
    """Unit conversion"""
    km = float(input("Kilometers: "))
    c = float(input("Celsius: "))
    inr = float(input("Rupees: "))
    rate = 83.0   # fixed rate: 1 USD = 83 INR
    print(f"{km} km = {km * 1000} m")
    print(f"{c} C = {c * 9 / 5 + 32:.1f} F")
    print(f"Rs {inr} = $ {inr / rate:.2f}  (1 USD = Rs {rate})")


def q8():
    """Multiple inputs in one line"""
    a, b, c = map(float, input("Enter three numbers separated by space: ").split())
    print(f"Sum = {a + b + c:.2f}")
    print(f"Product = {a * b * c:.2f}")


def q9():
    """Expression based grading"""
    m1 = float(input("Marks 1: "))
    m2 = float(input("Marks 2: "))
    m3 = float(input("Marks 3: "))
    total = m1 + m2 + m3
    percent = total / 300 * 100
    if percent >= 90:
        grade = "A"
    elif percent >= 75:
        grade = "B"
    elif percent >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"Total = {total}/300, Percentage = {percent:.2f}%, Grade = {grade}")


def q10():
    """Error analysis in expressions"""
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print("Error:", e)
    try:
        print("Age: " + 18)
    except TypeError as e:
        print("Error:", e)
    # Prevent / handle
    d = 0
    print("Safe division:", 10 / d if d != 0 else "denominator is zero")
    print("Age: " + str(18))


# ---------------- Practice questions ----------------
def pq1():
    """Electricity bill"""
    units = int(input("Units consumed: "))
    fixed = 150
    variable = 6 * (units - 100) if units > 100 else 0
    print(f"Fixed charge    : Rs {fixed}")
    print(f"Variable charge : Rs {variable}")
    print(f"Total payable   : Rs {fixed + variable}")


def pq2():
    """Average speed"""
    distance = float(input("Distance (km): "))
    time = float(input("Time (hours): "))
    print(f"Average speed = {distance / time} km/h")   # 180 km in 3 h -> 60.0 km/h


def pq3():
    """Discount + GST bill"""
    bill = 2500
    discount = bill * 10 / 100
    after = bill - discount
    gst = after * 18 / 100
    print(f"Discount = {discount}, GST = {gst}, Net bill = {after + gst}")   # 250, 405, 2655


def pq4():
    """Compare arithmetic expressions"""
    a, b = 25, 4
    print("25 + 4 =", a + b)
    print("25 - 4 =", a - b)
    print("25 * 4 =", a * b)
    print("25 / 4 =", a / b, " (float division)")
    print("25 // 4 =", a // b, " (floor division, drops the fraction)")
    print("25 % 4 =", a % b, " (remainder)")
    print("25 ** 2 =", a ** 2)


def pq5():
    """Trip fuel cost"""
    distance, mileage, price = 240, 15, 105
    litres = distance / mileage
    print(f"Fuel needed = {litres} L, cost = Rs {litres * price}")   # 16 L, Rs 1680


def pq6():
    """Topper"""
    marks = list(map(int, input("Enter marks of 5 students separated by space: ").split()))
    top = max(marks)
    print("Topper marks:", top, "| Student position:", marks.index(top) + 1)   # 95, student 5


def pq7():
    """Monthly EMI (simple interest)"""
    principal, rate, months = 500000, 12, 24
    interest = principal * rate / 100 * (months / 12)
    total = principal + interest
    print(f"Interest = {interest}, Total = {total}, EMI = Rs {total / months:.2f}")   # 25833.33


def pq8():
    """Operator precedence verification"""
    print(10 + 5 * 2)        # 20
    print((10 + 5) * 2)      # 30
    print(100 / 5 + 3 * 2)   # 26.0
    print(50 - 6 / 2)        # 47.0
    print(8 + 2 ** 3)        # 16


def pq9():
    """Tip and bill splitting"""
    bill, friends = 1800, 4
    tip = bill * 8 / 100
    final = bill + tip
    print(f"Tip = {tip}, Final bill = {final}, Each pays = {final / friends}")   # 144, 1944, 486


def pq10():
    """BMI"""
    weight, height = 72, 1.75
    bmi = weight / height ** 2
    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obese"
    print(f"BMI = {bmi:.2f} -> {cat}")   # 23.51 Normal


if __name__ == "__main__":
    run(globals(), "Practical 2 - Input/Output and Arithmetic")
