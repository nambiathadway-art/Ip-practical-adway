"""Practical 8 - Dictionaries: creation, indexing and methods"""
from menu import run


def q1():
    """Create dictionary"""
    student = {"Name": "Asha", "Age": 18, "Marks": 87}
    print(student, type(student))
    print("A dictionary maps unique KEYS to VALUES (key: value pairs)")


def q2():
    """Access values"""
    student = {"Name": "Asha", "Age": 18, "Marks": 87}
    print(student["Name"], student["Marks"])
    try:
        print(student["City"])
    except KeyError as e:
        print("KeyError for missing key:", e)


def q3():
    """get() method"""
    student = {"Name": "Asha", "Age": 18}
    print(student.get("Name"))
    print(student.get("City"))                  # None, no error
    print(student.get("City", "Not available"))  # default value
    print("student['City'] raises KeyError, get() does not")


def q4():
    """Add and update"""
    d = {"Name": "Asha", "Age": 18}
    d["City"] = "Mumbai"      # new key -> added
    d["Age"] = 19             # existing key -> updated
    print(d)


def q5():
    """pop() and del"""
    d = {"a": 1, "b": 2, "c": 3}
    print("pop('a') returned", d.pop("a"))
    del d["b"]
    print(d)
    print("pop with default:", d.pop("z", "not found"))
    try:
        del d["z"]
    except KeyError as e:
        print("del missing key -> KeyError", e)


def q6():
    """Iterate"""
    d = {"Name": "Asha", "Age": 18, "Marks": 87}
    print("Keys:")
    for k in d:
        print(k)
    print("Values:")
    for v in d.values():
        print(v)
    print("Key-value pairs:")
    for k, v in d.items():
        print(k, "->", v)


def q7():
    """keys(), values(), items()"""
    d = {"a": 1, "b": 2, "c": 3}
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))


def q8():
    """Character frequency"""
    text = input("Enter a string: ")
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print(freq)


def q9():
    """Nested dictionary"""
    students = {
        "S1": {"name": "Asha", "marks": 87, "city": "Mumbai"},
        "S2": {"name": "Ravi", "marks": 72, "city": "Pune"},
    }
    print(students["S1"]["name"])
    students["S2"]["marks"] = 80
    print(students)


def q10():
    """Merge with update()"""
    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 30}
    a.update(b)
    print(a)
    print("Common key 'y' was overwritten by the value from b")


def q11():
    """Sort dictionary"""
    d = {"banana": 3, "apple": 5, "cherry": 1}
    print("By key:", dict(sorted(d.items())))
    print("By value:", dict(sorted(d.items(), key=lambda item: item[1])))


def q12():
    """Inventory system"""
    inventory = {}
    inventory["Pen"] = 50              # add
    inventory["Book"] = 20
    inventory["Bag"] = 5
    inventory["Pen"] += 25             # update stock
    del inventory["Bag"]               # remove
    print("Final inventory:")
    for item, qty in inventory.items():
        print(f"  {item:<6} {qty}")


# ---------------- Practice questions ----------------
def pq1():
    """Attendance"""
    att = {"S101": "Present", "S102": "Absent", "S103": "Present", "S104": "Late"}
    att["S104"] = "Present"
    att["S105"] = "Present"
    print(att)
    print("Total present:", list(att.values()).count("Present"))


def pq2():
    """Hospital nested dictionary"""
    p = {"P001": {"name": "Asha", "temp": 98.6},
         "P002": {"name": "Ravi", "temp": 101.2},
         "P003": {"name": "Neha", "temp": 99.1}}
    hottest = max(p, key=lambda k: p[k]["temp"])
    print("Highest temperature:", hottest, p[hottest])
    p["P003"]["temp"] = 100.4
    print(p["P003"])


def pq3():
    """Drone sensors"""
    d = {"altitude": 250, "speed": 45, "battery": 78, "gps": "ACTIVE"}
    d["wind_speed"] = 12
    del d["gps"]
    for k, v in d.items():
        print(k, ":", v)


def pq4():
    """Retail inventory"""
    inv = {"Laptop": 12, "Mouse": 40, "Keyboard": 25, "Monitor": 10}
    inv["Laptop"] -= 2
    inv["Printer"] = 5
    inv = {k: v for k, v in inv.items() if v > 0}   # remove out-of-stock items
    print(inv)


def pq5():
    """Word frequency"""
    text = "python makes coding easy and python makes debugging easier"
    freq = {}
    for w in text.split():
        freq[w] = freq.get(w, 0) + 1
    print(freq)


def pq6():
    """Output: key access"""
    student = {"name": "Asha", "marks": 92}
    print(student["name"])           # Asha


def pq7():
    """Output: len after adding"""
    d = {"a": 1, "b": 2}
    d["c"] = 3
    print(len(d))                    # 3


def pq8():
    """Output: get() default"""
    data = {"x": 10, "y": 20}
    print(data.get("z", 0))          # 0


def pq9():
    """Key error: name vs 'name'"""
    print("Error: student[name] uses a VARIABLE name (NameError). Keys that are strings need quotes")
    student = {"name": "Ravi", "marks": 85}
    print(student["name"])


def pq10():
    """append() on dict"""
    print("Error: dictionaries have no append(); use update() or d[key] = value")
    d = {"a": 1, "b": 2}
    d.update({"c": 3})
    print(d)


if __name__ == "__main__":
    run(globals(), "Practical 8 - Dictionaries")
