"""Practical 11 - File handling: reading and writing text files
Files are created in the folder where you run the program."""
import os
from menu import run


def _make_sample():
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nFiles store data\nPython is powerful\n")


def q1():
    """Write to a file"""
    f = open("sample.txt", "w")
    f.write("Python is easy\n")
    f.write("Files store data\n")
    f.write("Python is powerful\n")
    f.close()                          # always close so data is saved
    print("sample.txt written")


def q2():
    """Read entire file"""
    _make_sample()
    f = open("sample.txt", "r")
    print(f.read())
    f.close()


def q3():
    """readline() vs for loop"""
    _make_sample()
    f = open("sample.txt")
    print("readline():", f.readline().strip())
    print("readline():", f.readline().strip())
    f.close()
    print("for loop:")
    f = open("sample.txt")
    for line in f:
        print(" ", line.strip())
    f.close()
    print("readline reads ONE line per call; the loop reads all lines one by one")


def q4():
    """with statement"""
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nFiles store data\n")
    with open("sample.txt") as f:
        print(f.read())
    print("with closes the file automatically, even if an error occurs, so close() is not needed")


def q5():
    """Append mode"""
    _make_sample()
    with open("sample.txt", "a") as f:
        f.write("New appended line\n")
    with open("sample.txt") as f:
        print(f.read())               # old content is still there


def q6():
    """Count lines, words, characters"""
    _make_sample()
    with open("sample.txt") as f:
        text = f.read()
    print("Lines:", len(text.splitlines()), "Words:", len(text.split()), "Characters:", len(text))


def q7():
    """Search word"""
    _make_sample()
    word = input("Enter word to search: ").lower()
    with open("sample.txt") as f:
        count = f.read().lower().split().count(word)
    print(f"'{word}' occurs {count} time(s)")


def q8():
    """Copy file"""
    _make_sample()
    with open("sample.txt") as src, open("copy.txt", "w") as dst:
        dst.write(src.read())
    with open("copy.txt") as f:
        print("copy.txt contains:\n" + f.read())


def q9():
    """Filter lines by keyword"""
    _make_sample()
    with open("sample.txt") as src, open("filtered.txt", "w") as dst:
        for line in src:
            if "Python" in line:
                dst.write(line)
    with open("filtered.txt") as f:
        print(f.read())


def q10():
    """Student record file"""
    with open("students.txt", "w") as f:
        f.write("101,Asha,87\n102,Ravi,72\n103,Neha,91\n")
    print(f"{'Roll':<6}{'Name':<8}{'Marks'}")
    with open("students.txt") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"{roll:<6}{name:<8}{marks}")


def q11():
    """File exceptions"""
    try:
        with open("missing_file.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("Sorry, the file does not exist. Please check the file name.")


def q12():
    """Update file content"""
    _make_sample()
    with open("sample.txt") as f:
        data = f.read()
    data = data.replace("Python", "Java")
    with open("sample.txt", "w") as f:
        f.write(data)
    with open("sample.txt") as f:
        print(f.read())


# ---------------- Practice questions ----------------
def pq1():
    """Drone flight log"""
    with open("flight_log.txt", "w") as f:
        f.write("ALT=250,SPD=45,BAT=78\n")
    with open("flight_log.txt", "a") as f:
        for alt, spd, bat in [(260, 50, 70), (270, 48, 45), (280, 52, 40), (290, 47, 66), (300, 55, 30)]:
            f.write(f"ALT={alt},SPD={spd},BAT={bat}\n")
    low = 0
    with open("flight_log.txt") as f:
        for line in f:
            print(line.strip())
            bat = int(line.strip().split("BAT=")[1])
            if bat < 50:
                low += 1
    print("Entries with battery below 50:", low)


def pq2():
    """Patient notes"""
    notes = ["Asha - stable", "Ravi - critical condition", "Neha - recovering", "Kiran - critical", "Mira - stable"]
    with open("patient_notes.txt", "w") as f:
        f.write("\n".join(notes) + "\n")
    with open("patient_notes.txt") as f:
        for line in f:
            if "critical" in line:
                print(line.strip())


def pq3():
    """Login audit"""
    with open("audit_log.txt", "w") as f:
        f.write("user=admin,status=FAILED\nuser=ravi,status=SUCCESS\n")
    with open("audit_log.txt", "a") as f:
        f.write("user=guest,status=FAILED\nuser=admin,status=FAILED\n")
    failed = 0
    with open("audit_log.txt") as src, open("threat_log.txt", "w") as threat:
        for line in src:
            if "FAILED" in line:
                failed += 1
                threat.write(line)
    print("Failed logins:", failed, "(copied to threat_log.txt)")


def pq4():
    """Prompt archive"""
    prompts = ["Explain AI", "", "Write a poem about rain", "", "Summarise this text", "What is ML",
               "Define recursion", "Translate hello", "Plan a trip", "Fix my code"]
    with open("prompt_bank.txt", "w") as f:
        f.write("\n".join(prompts) + "\n")
    with open("prompt_bank.txt") as f:
        lines = [l.strip() for l in f if l.strip()]
    with open("prompt_bank.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Prompts after removing blanks:", len(lines))
    print("Average words per prompt:", sum(len(l.split()) for l in lines) / len(lines))


def pq5():
    """Weather daily dump"""
    data = [(32, 70, 15), (35, 65, 10), (30, 80, 20), (36, 60, 12), (33, 72, 18), (29, 85, 22), (34, 68, 14)]
    with open("weather.txt", "w") as f:
        for t, h, w in data:
            f.write(f"TEMP={t},HUM={h},WIND={w}\n")
    best_day, best_temp = 0, -100
    with open("weather.txt") as f:
        for day, line in enumerate(f, 1):
            temp = int(line.split(",")[0].split("=")[1])
            if temp > best_temp:
                best_day, best_temp = day, temp
    print(f"Highest temperature: {best_temp} on day {best_day}")


def pq6():
    """Output (with the finally removed)"""
    print("As printed in the sheet, 'finally' without 'try' is a SyntaxError.")
    print("If 'finally' is removed, the output is:")
    with open("demo.txt", "w") as f:
        f.write("Python\nAI")
    with open("demo.txt", "r") as f:
        print(f.readline().strip())    # Python


def pq7():
    """Output: readlines length"""
    with open("demo.txt", "w") as f:
        f.write("A\nB\nC")
    with open("demo.txt", "r") as f:
        lines = f.readlines()
        print(len(lines))              # 3


def pq8():
    """Output: append"""
    with open("demo.txt", "w") as f:
        f.write("DATA")
    with open("demo.txt", "a") as f:
        f.write("SCIENCE")
    with open("demo.txt", "r") as f:
        print(f.read())                # DATASCIENCE


def pq9():
    """Fill blanks: write"""
    with open("report.txt", "w") as f:
        f.write("Python Lab\n")
        f.write("Practical 11")
    print("File written")


def pq10():
    """Fill blanks: read FAILED lines"""
    if not os.path.exists("audit_log.txt"):
        with open("audit_log.txt", "w") as f:
            f.write("user=admin,status=FAILED\nuser=ravi,status=SUCCESS\n")
    with open("audit_log.txt", "r") as f:
        for line in f:
            if "FAILED" in line:
                print(line.strip())
            else:
                pass


if __name__ == "__main__":
    run(globals(), "Practical 11 - File Handling")
