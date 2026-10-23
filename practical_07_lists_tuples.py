"""Practical 7 - Lists and Tuples (creation, indexing, methods) + 2D indexing/slicing"""
import numpy as np
from menu import run


def q1():
    """Creating lists and tuples"""
    nums = [10, 20, 30, 40, 50]
    names = ("Asha", "Ravi", "Neha")
    print(nums, type(nums))
    print(names, type(names))
    print("List uses [], tuple uses (); a list can change, a tuple cannot")


def q2():
    """Indexing"""
    lst = [10, 20, 30, 40, 50]
    tup = ("a", "b", "c", "d", "e")
    print("First:", lst[0], tup[0], "| Last:", lst[-1], tup[-1], "| Middle:", lst[len(lst) // 2], tup[len(tup) // 2])
    print("Negative index lst[-2] =", lst[-2], " tup[-2] =", tup[-2])


def q3():
    """Slicing"""
    lst = [1, 2, 3, 4, 5, 6]
    tup = (1, 2, 3, 4, 5, 6)
    print("First 3:", lst[:3], tup[:3])
    print("Last 2:", lst[-2:], tup[-2:])
    print("Alternate:", lst[::2], tup[::2])
    print("Slicing a list gives a list, slicing a tuple gives a tuple")


def q4():
    """Mutability vs immutability"""
    lst = [1, 2, 3]
    lst[0] = 100
    print("List after change:", lst)
    tup = (1, 2, 3)
    try:
        tup[0] = 100
    except TypeError as e:
        print("Tuple error:", e)
    print("Immutable = object cannot be changed after creation (safe, hashable, faster)")


def q5():
    """append() and insert()"""
    lst = [10, 20, 30]
    lst.append(40)
    lst.insert(1, 15)
    print(lst)


def q6():
    """remove() and pop()"""
    lst = [10, 20, 30, 40]
    lst.remove(20)
    print("After remove(20):", lst)
    print("pop() returned:", lst.pop(), "->", lst)
    try:
        lst.remove(99)
    except ValueError as e:
        print("remove(99) ->", e)
    try:
        [].pop()
    except IndexError as e:
        print("pop() on empty ->", e)


def q7():
    """sort() and reverse()"""
    lst = [5, 2, 9, 1, 7]
    lst.sort()
    print("Ascending:", lst)
    lst.sort(reverse=True)
    print("Descending:", lst)
    lst.reverse()
    print("Reversed:", lst)
    print("sort() orders by value; reverse() only flips the current order")


def q8():
    """Tuple count() and index()"""
    t = (1, 2, 2, 3, 2, 4)
    print("count(2) =", t.count(2))
    print("index(3) =", t.index(3))
    try:
        t.index(9)
    except ValueError as e:
        print("index(9) ->", e)
    print("Safe check:", 9 in t)


def q9():
    """Nested lists"""
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("m[1][2] =", m[1][2])
    m[0][0] = 100
    print(m)


def q10():
    """Convert list <-> tuple"""
    lst = [1, 2, 3]
    tup = tuple(lst)
    print(tup, type(tup))
    back = list(tup)
    back.append(4)
    print(back, type(back))
    print("Original tuple unchanged:", tup)


def q11():
    """Iteration"""
    lst = [10, 20, 30]
    tup = (1, 2, 3)
    total = 0
    for x in lst:
        print(x, end=" ")
        total += x
    print("-> sum", total)
    for x in tup:
        print(x, end=" ")
    print("\nSame for loop works for both")


def q12():
    """Shopping cart"""
    categories = ("Grocery", "Electronics", "Clothing")   # fixed -> tuple
    cart = []
    cart.append(("Rice", 60, categories[0]))
    cart.append(("Earphones", 500, categories[1]))
    cart.append(("T-shirt", 350, categories[2]))
    cart.remove(("T-shirt", 350, categories[2]))
    print("Cart summary:")
    for item, price, cat in cart:
        print(f"  {item:<10} Rs {price:>4}  ({cat})")
    print("Total = Rs", sum(p for _, p, _ in cart))


# ---- Extra section: 2D indexing / slicing ----
MAT = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def s1():
    """2D list indexing"""
    print("First:", MAT[0][0], "Last:", MAT[2][2], "Middle:", MAT[1][1])


def s2():
    """Row and column access"""
    print("2nd row:", MAT[1])
    print("3rd column:", [row[2] for row in MAT])
    print("Lists have no column slice, so we loop through the rows")


def s3():
    """Negative indexing in 2D"""
    print("Last row:", MAT[-1], "Last column:", [r[-1] for r in MAT], "Bottom-right:", MAT[-1][-1], "==", MAT[2][2])


def s4():
    """Slicing rows"""
    print("First two rows:", MAT[0:2])
    print("Last two rows:", MAT[-2:])


def s5():
    """Submatrix from a list"""
    sub = [row[0:2] for row in MAT[0:2]]
    print("Top-left 2x2:", sub)
    print("Limitation: a list cannot do MAT[0:2, 0:2]; we need a loop/comprehension")


ARR = np.array(MAT)


def s6():
    """NumPy basic indexing"""
    print("Element (1,2):", ARR[1, 2], "| Row 1:", ARR[1], "| Column 1:", ARR[:, 1])


def s7():
    """NumPy row/column slicing"""
    print("First two rows:\n", ARR[0:2, :])
    print("Last column:", ARR[:, -1])
    print("List version needed a loop; NumPy does it in one expression")


def s8():
    """NumPy submatrix"""
    print("Middle 2x2:\n", ARR[1:3, 1:3])
    print("Advantage: one slice for rows AND columns, faster, and no loops")


# ---------------- Practice questions ----------------
def pq1():
    """Library kiosk"""
    ids = [1045, 1098, 1120, 1087, 1155, 1178, 1201, 1199, 1180, 1166, 1134, 1102]
    ids.insert(0, 1215)
    ids.pop()               # oldest = last element
    print(ids)


def pq2():
    """Drone coordinates"""
    pts = [(10, 20, 150), (15, 25, 160), (20, 30, 170), (25, 35, 180), (30, 40, 190),
           (35, 45, 200), (40, 50, 210), (45, 55, 220), (50, 60, 230), (55, 65, 240)]
    print("x:", [p[0] for p in pts])
    print("y:", [p[1] for p in pts])
    print("altitude:", [p[2] for p in pts])


def pq3():
    """Doctor shifts"""
    shifts = [["Dr A", "Dr B", "Dr C"], ["Dr D", "Dr E", "Dr F"], ["Dr G", "Dr H", "Dr I"],
              ["Dr J", "Dr K", "Dr L"], ["Dr M", "Dr N", "Dr O"], ["Dr P", "Dr Q", "Dr R"],
              ["Dr S", "Dr T", "Dr U"]]
    shifts[4][2] = "Dr Z"   # day 5 -> index 4, night -> last shift (index 2)
    print(shifts[4])


def pq4():
    """Remove duplicates preserving order"""
    songs = ["Shape of You", "Believer", "Perfect", "Believer", "Faded", "Perfect", "Senorita",
             "Levitating", "Faded", "Perfect", "Blinding Lights", "Senorita", "Peaches", "Believer", "Perfect"]
    unique = []
    for s in songs:
        if s not in unique:
            unique.append(s)
    print(unique)


def pq5():
    """Tuple immutability"""
    points = [(0, 0), (10, 5), (20, 10), (30, 15), (40, 20)]
    try:
        points[2][0] = 25
    except TypeError as e:
        print("Error:", e)
    print("A tuple cannot be edited in place. Replace the whole tuple in the list instead:")
    points[2] = (25, 12)
    print(points)


def pq6():
    """Quiz scores"""
    scores = [78, 85, 91, 88, 76, 95, 89, 84]
    midterm, final = scores[:4], scores[4:]
    print("Midterm:", midterm, "Final:", final)
    print("Highest:", max(scores), "Average:", sum(scores) / len(scores))


def pq7():
    """Canteen combos"""
    combos = [["Veg Burger", 120], ["Pizza Slice", 90], ["Pasta Bowl", 150], ["Sandwich", 80]]
    combos.append(["Noodles", 110])
    combos.sort(key=lambda item: item[1])
    print(combos)


def pq8():
    """GPS route points"""
    route = [(18.5204, 73.8567), (18.5210, 73.8575), (18.5221, 73.8580), (18.5232, 73.8591),
             (18.5243, 73.8602), (18.5254, 73.8613), (18.5265, 73.8624), (18.5276, 73.8635),
             (18.5287, 73.8646), (18.5298, 73.8657)]
    print("Alternate:", route[::2])
    print("First 5:", route[:5])
    print("Reversed:", route[::-1])


def pq9():
    """Stock prices"""
    prices = [210, 215, 208, 220, 225, 230, 218, 240, 235, 245]
    top3 = sorted(prices, reverse=True)[:3]
    print("Top 3:", top3, "Positions (1-based):", [prices.index(p) + 1 for p in top3])
    print("Lowest:", min(prices), "at slot", prices.index(min(prices)) + 1)


def pq10():
    """Hostel rooms"""
    rooms = ("A101", "A102", "A103", "B201", "B202", "B203", "C301", "C302", "C303", "A101", "B201")
    print("Count of A101:", rooms.count("A101"))
    print("Index of C302:", rooms.index("C302"))
    print("Repeated rooms:", [r for r in sorted(set(rooms)) if rooms.count(r) > 1])


if __name__ == "__main__":
    run(globals(), "Practical 7 - Lists, Tuples, 2D Slicing")
