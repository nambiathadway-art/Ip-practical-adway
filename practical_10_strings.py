"""Practical 10 - String operations: slicing, searching, methods"""
from menu import run

TEXT = "Python Programming"


def q1():
    """Indexing"""
    s = "Python"
    print("First:", s[0], "Last:", s[-1], "Middle:", s[len(s) // 2])


def q2():
    """Slicing"""
    s = "Programming"
    print(s[:5], "|", s[-4:], "|", s[2:7])
    print("[start:end] takes characters from start up to, but NOT including, end")


def q3():
    """Step slicing"""
    s = "Python"
    print("Alternate:", s[::2])
    print("Reverse:", s[::-1])


def q4():
    """Immutability"""
    s = "Python"
    try:
        s[0] = "J"
    except TypeError as e:
        print("Error:", e)
    s = "J" + s[1:]
    print("New string:", s)


def q5():
    """in / not in"""
    s = "Python is fun"
    word = input("Enter substring: ")
    print(f"'{word}' found" if word in s else f"'{word}' not found")
    print("'Java' not in s ->", "Java" not in s)


def q6():
    """find() vs index()"""
    s = "Python is fun"
    print("find('is') =", s.find("is"), " index('is') =", s.index("is"))
    print("find('xyz') =", s.find("xyz"))
    try:
        s.index("xyz")
    except ValueError as e:
        print("index('xyz') ->", e)


def q7():
    """count()"""
    s = "banana"
    print("Count of 'a':", s.count("a"))
    print("Count of 'an':", s.count("an"))


def q8():
    """Case conversion"""
    s = "hello python world"
    print(s.upper(), "|", s.lower(), "|", s.title())


def q9():
    """strip, replace, f-string"""
    s = "   hello world   "
    print(f"[{s.strip()}]")
    print(s.strip().replace("world", "Python"))
    name, n = "Asha", 3
    print(f"{name} has {n} messages")


def q10():
    """split and join"""
    sentence = "Python makes coding easy"
    words = sentence.split()
    print(words)
    print("-".join(words))


def q11():
    """Palindrome"""
    s = input("Enter a string: ").lower()
    print("Palindrome" if s == s[::-1] else "Not a palindrome")


def q12():
    """Text analyzer"""
    para = input("Enter a paragraph: ")
    words = para.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("Words:", len(words))
    print("Characters:", len(para))
    print("Most frequent word:", max(freq, key=freq.get) if freq else "-")


# ---------------- Practice questions ----------------
def pq1():
    """Chatbot cleaner"""
    s = " Python makes NLP powerful "
    print("_".join(s.strip().lower().split()))


def pq2():
    """ID masking"""
    sid = "STU2026CS1098"
    print(sid[:4], sid[-4:], sid[:4] + "****" + sid[-4:])


def pq3():
    """Drone log parser"""
    log = "ALT:250|SPD:45|BAT:78"
    data = dict(part.split(":") for part in log.split("|"))
    print("Altitude:", data["ALT"], "Speed:", data["SPD"], "Battery:", data["BAT"])


def pq4():
    """Password validator"""
    pw = "PySecure2026!"
    print("Uppercase:", any(c.isupper() for c in pw))
    print("Lowercase:", any(c.islower() for c in pw))
    print("Digit:", any(c.isdigit() for c in pw))
    print("Special:", any(not c.isalnum() for c in pw))
    print("Min length 8:", len(pw) >= 8)


def pq5():
    """Medical keywords"""
    report = "fever cough fever fatigue fever cold"
    words = report.split()
    print("fever count:", words.count("fever"))
    print("Unique symptoms:", sorted(set(words)))
    print("Most repeated:", max(set(words), key=words.count))


def pq6():
    """Output: step slice"""
    text = "PythonProgramming"
    print(text[2:10:2])                # toPo


def pq7():
    """Output: chained methods"""
    s = " Data Science "
    print(s.strip().upper().replace(" ", "_"))    # DATA_SCIENCE


def pq8():
    """Output: split + reversed join"""
    msg = "AI|ML|DL|NLP"
    parts = msg.split("|")
    print("-".join(parts[::-1]))         # NLP-DL-ML-AI


def pq9():
    """Fill blank: slice"""
    text = "PythonProgramming"
    print(text[6:])                      # Programming


def pq10():
    """Fill blank: replace"""
    sentence = "Python makes coding easy"
    print(sentence.replace(" ", "-"))


if __name__ == "__main__":
    run(globals(), "Practical 10 - Strings")
