"""Practical 3 - Decision making: if, if-else, if-elif-else, nested if"""
from menu import run


def q1():
    """Basic if"""
    n = float(input("Enter a number: "))
    if n > 0:
        print("The number is positive")


def q2():
    """Even or odd"""
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")


def q3():
    """Grade using elif"""
    marks = float(input("Enter marks: "))
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")


def q4():
    """Nested if: voting eligibility"""
    age = int(input("Enter age: "))
    nationality = input("Enter nationality: ").strip()
    if age >= 18:
        if nationality.lower() == "indian":
            print("Eligible to vote")
        else:
            print("Not eligible: must be Indian")
    else:
        print("Not eligible: age below 18")


def q5():
    """Largest of three (handles equal values)"""
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a == b == c:
        print("All three numbers are equal")
    elif a >= b and a >= c:
        print("Largest is", a)
    elif b >= a and b >= c:
        print("Largest is", b)
    else:
        print("Largest is", c)


def q6():
    """Leap year"""
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def q7():
    """Simple calculator"""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator")


def q8():
    """Discount system"""
    amount = float(input("Enter purchase amount: "))
    if amount >= 2000:
        rate = 20
    elif amount >= 1000:
        rate = 10
    else:
        rate = 0
    discount = amount * rate / 100
    print(f"Discount {rate}% = {discount}, Final amount = {amount - discount}")


def q9():
    """Triangle type"""
    a = float(input("Side 1: "))
    b = float(input("Side 2: "))
    c = float(input("Side 3: "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("These sides cannot form a triangle")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


def q10():
    """Menu driven program"""
    print("1. Check even/odd\n2. Find largest\n3. Grade system")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        q2()
    elif choice == "2":
        q5()
    elif choice == "3":
        q3()
    else:
        print("Invalid choice")


# ---------------- Practice questions ----------------
def pq1():
    """Placement eligibility"""
    cgpa = float(input("CGPA: "))
    attendance = float(input("Attendance %: "))
    if cgpa >= 7.0 and attendance >= 75:
        print("Eligible for placement")
    else:
        print("Not eligible for placement")


def pq2():
    """Loan approval"""
    salary = float(input("Salary: "))
    score = int(input("Credit score: "))
    if salary >= 30000 and score > 700:
        print("Loan approved")
    else:
        print("Loan rejected")


def pq3():
    """Final bill with discount"""
    amount = float(input("Purchase amount: "))
    if amount > 5000:
        rate = 15
    elif amount > 2000:
        rate = 10
    else:
        rate = 0
    print(f"Final bill = Rs {amount - amount * rate / 100}")


def pq4():
    """Voting eligibility (nested if)"""
    q4()


def pq5():
    """Parking bill"""
    hours = int(input("Hours parked: "))
    if hours <= 0:
        charge = 0
    elif hours == 1:
        charge = 20
    else:
        charge = 20 + (hours - 1) * 10
    charge = min(charge, 100)
    print("Parking charge: Rs", charge)


def pq6():
    """Age category"""
    age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teen")
    elif age < 60:
        print("Adult")
    else:
        print("Senior Citizen")


def pq7():
    """Scholarship eligibility"""
    marks = float(input("Marks: "))
    income = float(input("Family income: "))
    if marks > 85 and income < 300000:
        print("Scholarship awarded")
    else:
        print("Not eligible for scholarship")


def pq8():
    """Recharge plan benefit"""
    amount = int(input("Recharge amount: "))
    if amount >= 299:
        print("2 GB/day")
    elif amount >= 199:
        print("1 GB/day")
    else:
        print("Only talktime benefits")


def pq9():
    """Blood pressure category"""
    sys_bp = int(input("Systolic reading: "))
    if sys_bp < 120:
        print("Normal")
    elif sys_bp < 130:
        print("Elevated")
    elif sys_bp < 140:
        print("High Stage 1")
    else:
        print("High Stage 2")


def pq10():
    """Employee bonus"""
    years = int(input("Years of service: "))
    salary = float(input("Salary: "))
    if years >= 10:
        rate = 20
    elif years >= 5:
        rate = 10
    else:
        rate = 0
    print(f"Bonus = {rate}% = Rs {salary * rate / 100}")


if __name__ == "__main__":
    run(globals(), "Practical 3 - Conditional Statements")
