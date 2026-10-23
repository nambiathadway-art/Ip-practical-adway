"""Tiny menu helper shared by all practical files.
Every question in a practical is a function named q1, q2 ... (main questions),
s1, s2 ... (extra section, Practical 7 only) or pq1, pq2 ... (practice questions).
"""
import re


def run(ns, title="Practical"):
    pat = re.compile(r"^(q|s|pq)(\d+)$")
    order = {"q": 0, "s": 1, "pq": 2}
    items = []
    for name, obj in ns.items():
        m = pat.match(name)
        if m and callable(obj):
            items.append((order[m.group(1)], int(m.group(2)), name, obj))
    items.sort()
    table = {name: obj for _, _, name, obj in items}

    while True:
        print(f"\n===== {title} =====")
        for _, _, name, obj in items:
            doc = (obj.__doc__ or "").strip().splitlines()
            print(f"{name:>5}  {doc[0] if doc else ''}")
        choice = input("\nEnter question (e.g. q3, pq2) or x to exit: ").strip().lower()
        if choice == "x":
            break
        if choice.isdigit():
            choice = "q" + choice
        if choice in table:
            print()
            table[choice]()
        else:
            print("Invalid choice")
