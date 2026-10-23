"""Practical 5 - Loop control statements: break, continue, pass"""
from menu import run


def q1():
    """break"""
    for i in range(1, 11):
        if i == 5:
            break                      # loop exits immediately
        print(i, end=" ")
    print("\nLoop ended when i became 5")


def q2():
    """continue"""
    for i in range(1, 11):
        if i % 3 == 0:
            continue                   # skip this iteration only
        print(i, end=" ")
    print()


def q3():
    """break vs continue"""
    print("With break:   ", end="")
    for i in range(1, 11):
        if i == 5:
            break
        print(i, end=" ")
    print("\nWith continue:", end=" ")
    for i in range(1, 11):
        if i == 5:
            continue
        print(i, end=" ")
    print("\nbreak stops the whole loop; continue skips only the current iteration.")


def q4():
    """Search in a list"""
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    key = int(input("Number to search: "))
    for i, n in enumerate(nums):
        if n == key:
            print(f"Found at position {i + 1} (index {i})")
            break
    else:
        print("Not found")


def q5():
    """First number divisible by n (1-100)"""
    n = int(input("Enter n: "))
    for i in range(1, 101):
        if i % n == 0:
            print("First divisible number:", i)
            break


def q6():
    """Print positive numbers only"""
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    for n in nums:
        if n < 0:
            continue
        print(n, end=" ")
    print()


def q7():
    """Sum of valid inputs"""
    total = 0
    while True:
        n = float(input("Enter a number (0 to stop): "))
        if n == 0:
            break
        if n < 0:
            continue
        total += n
    print("Sum of valid inputs =", total)


def q8():
    """Password retry system (3 attempts)"""
    correct = "python123"
    for attempt in range(1, 4):
        if input(f"Attempt {attempt}/3 - enter password: ") == correct:
            print("Login successful")
            break
        print("Wrong password")
    else:
        print("Account locked after 3 wrong attempts")


def q9():
    """pass statement"""
    for i in range(1, 6):
        if i == 3:
            pass                       # placeholder: block must not be empty
        else:
            print(i, end=" ")
    print("\npass does nothing; Python needs at least one statement inside a block, else SyntaxError.")


def q10():
    """Pattern with conditional skipping"""
    for i in range(1, 6):
        for j in range(1, i + 1):
            if j % 2 == 0:
                continue               # skip multiples of 2
            print(j, end=" ")
        print()


# ---------------- Practice questions ----------------
def pq1():
    """Drone scan stops on low battery"""
    batteries = [90, 82, 74, 60, 14, 50]
    for row, b in enumerate(batteries, 1):
        if b < 15:
            print(f"Low battery ({b}%) at row {row}. Scan stopped.")
            break
        print(f"Row {row} scanned, battery {b}%")


def pq2():
    """Skip duplicate RFID scans"""
    scans = ["A1", "B2", "A1", "C3", "B2", "D4"]
    seen = []
    for card in scans:
        if card in seen:
            continue
        seen.append(card)
        print("Attendance marked:", card)


def pq3():
    """Triage queue exits on critical case"""
    patients = [("Ravi", "normal"), ("Neha", "minor"), ("Asha", "critical"), ("Kiran", "normal")]
    for name, status in patients:
        if status == "critical":
            print(f"Critical case: {name}! Leaving queue for emergency.")
            break
        print("Treated:", name)


def pq4():
    """Ignore damaged barcodes (-1)"""
    for code in [1021, -1, 1033, -1, 1045]:
        if code == -1:
            continue
        print("Scanned:", code)


def pq5():
    """PIN vault: stop after 5 failed attempts"""
    pin = "482931"
    failed = 0
    while True:
        if input("Enter 6-digit PIN: ") == pin:
            print("Vault unlocked")
            break
        failed += 1
        if failed == 5:
            print("Too many wrong attempts. Vault locked.")
            break


def pq6():
    """Average temperature skipping faulty (negative) readings"""
    readings = [25, 27, -5, 30, -1, 28]
    total = count = 0
    for t in readings:
        if t < 0:
            continue
        total += t
        count += 1
    print("Average =", total / count)


def pq7():
    """pass as an empty placeholder"""
    plagiarism_check_enabled = False
    if plagiarism_check_enabled:
        pass                           # AI plagiarism check will be added later
    print("Exam portal running (plagiarism section reserved)")


def pq8():
    """Stop at first defective product"""
    products = ["ok"] * 36 + ["defective"] + ["ok"] * 63   # 100 products
    for number, status in enumerate(products, 1):
        if status == "defective":
            print("First defective item found at product", number)
            break


def pq9():
    """Skip weekends over 30 days"""
    for day in range(1, 31):
        weekday = (day - 1) % 7          # day 1 = Monday
        if weekday in (5, 6):            # Saturday, Sunday
            continue
        print("Analysing day", day)


def pq10():
    """Halt when a suspicious IP appears 3 times"""
    attempts = ["10.0.0.1", "10.0.0.5", "10.0.0.1", "10.0.0.9", "10.0.0.1", "10.0.0.5"]
    count = {}
    for ip in attempts:
        count[ip] = count.get(ip, 0) + 1
        if count[ip] == 3:
            print(f"ALERT: {ip} seen 3 times. Scanner halted.")
            break


if __name__ == "__main__":
    run(globals(), "Practical 5 - break, continue, pass")
