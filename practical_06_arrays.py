"""Practical 6 - Arrays: 2D lists, NumPy arrays, indexing and slicing"""
import numpy as np
from menu import run

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# ---- 2D arrays using lists ----
def q1():
    """Create and access 2D list"""
    print("Matrix:", M)
    print("First row:", M[0])
    print("Element at (2,3):", M[1][2])


def q2():
    """Matrix traversal"""
    print("Row-wise:")
    for row in M:
        for x in row:
            print(x, end=" ")
        print()
    print("Column-wise:")
    for j in range(len(M[0])):
        for i in range(len(M)):
            print(M[i][j], end=" ")
        print()


def q3():
    """Sum of rows and columns"""
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    mat = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        print(f"Sum of row {i + 1} =", sum(mat[i]))
    for j in range(cols):
        print(f"Sum of column {j + 1} =", sum(mat[i][j] for i in range(rows)))


def q4():
    """Matrix addition"""
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = a[i][j] + b[i][j]
    for row in result:
        print(row)


def q5():
    """Transpose"""
    mat = [[1, 2, 3], [4, 5, 6]]
    t = [[0] * len(mat) for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            t[j][i] = mat[i][j]
    print("Original:", mat)
    print("Transposed:", t)


# ---- NumPy ----
def q6():
    """Array creation: array, zeros, ones"""
    a = np.array([[1, 2, 3], [4, 5, 6]])
    z = np.zeros((2, 3))
    o = np.ones((3, 2), dtype=int)
    for name, arr in (("array", a), ("zeros", z), ("ones", o)):
        print(name, "\n", arr, "\n shape:", arr.shape, " dtype:", arr.dtype)


def q7():
    """NumPy indexing and slicing"""
    arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    print("Element [1,2]:", arr[1, 2])
    print("Row 1:", arr[1])
    print("Column 2:", arr[:, 2])
    print("Slice arr[0:2, 1:3]:\n", arr[0:2, 1:3])


def q8():
    """Arithmetic on arrays vs lists"""
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Add:", a + b, " Subtract:", a - b, " Multiply:", a * b)
    l1, l2 = [1, 2, 3], [4, 5, 6]
    print("List + List joins:", l1 + l2)
    print("List element-wise needs a loop:", [x + y for x, y in zip(l1, l2)])


def q9():
    """Mean, median, standard deviation"""
    arr = np.array([12, 15, 11, 18, 20, 14])
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Std deviation:", round(float(np.std(arr)), 2))


def q10():
    """Reshape"""
    a = np.arange(1, 13)
    print("1D:", a)
    print("3x4:\n", a.reshape(3, 4))
    print("2x6:\n", a.reshape(2, 6))
    try:
        a.reshape(5, 3)
    except ValueError as e:
        print("Constraint: total elements must stay the same ->", e)


def q11():
    """Matrix multiplication and transpose"""
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("NumPy a @ b:\n", a @ b)
    manual = [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    print("Manual:", manual)
    print("Transpose of a:\n", a.T)


def q12():
    """Student marks dataset"""
    names = ["Asha", "Ravi", "Neha", "Kiran"]
    marks = np.array([[78, 85, 90], [65, 70, 72], [92, 88, 95], [55, 60, 58]])
    avg = marks.mean(axis=1)
    for n, a in zip(names, avg):
        print(f"{n}: average {a:.2f}")
    print("Highest mark:", marks.max(), "by", names[np.argmax(marks.max(axis=1))])
    print("Lowest mark:", marks.min(), "by", names[np.argmin(marks.min(axis=1))])
    print("Best student by average:", names[np.argmax(avg)])


# ---------------- Practice questions ----------------
def pq1():
    """Irrigation zones"""
    data = np.array([[45, 50, 48, 52, 47, 49, 51],
                     [55, 53, 54, 52, 56, 57, 55],
                     [38, 40, 42, 39, 41, 43, 44],
                     [60, 62, 61, 63, 64, 62, 65]])
    for i, row in enumerate(data, 1):
        print(f"Zone {i}: avg {row.mean():.2f}, highest day {row.argmax() + 1}, lowest day {row.argmin() + 1}")
    r, c = np.unravel_index(data.argmax(), data.shape)
    print(f"Overall highest moisture: Zone {r + 1}, Day {c + 1}")


def pq2():
    """ICU temperatures"""
    t = np.array([[98.6, 99.1, 100.2, 99.8, 98.9, 99.0],
                  [97.8, 98.0, 98.4, 98.6, 98.2, 98.1],
                  [101.2, 100.8, 101.5, 102.0, 101.7, 101.3],
                  [99.4, 99.5, 99.6, 99.3, 99.2, 99.1],
                  [98.7, 98.9, 99.0, 98.8, 98.6, 98.5]])
    print("Highest per patient:", t.max(axis=1))
    print("Average temperature:", round(float(t.mean()), 2))
    print("Critical patient index:", int(t.max(axis=1).argmax()), "(0-based) -> Patient", int(t.max(axis=1).argmax()) + 1)


def pq3():
    """Classroom occupancy"""
    g = np.array([[1, 1, 0, 1, 0, 1, 1, 0],
                  [1, 0, 1, 1, 1, 0, 1, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1],
                  [1, 1, 1, 1, 0, 0, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1]])
    print("Busiest room:", g.sum(axis=1).argmax() + 1, "with", g.sum(axis=1).max(), "slots")
    print("Total free slots:", int((g == 0).sum()))
    print(f"Occupancy: {g.mean() * 100:.1f}%")


def pq4():
    """Invert image brightness"""
    img = np.array([[120, 135, 140, 150, 160, 170],
                    [110, 125, 130, 145, 155, 165],
                    [100, 115, 120, 135, 145, 155],
                    [90, 105, 110, 125, 135, 145],
                    [80, 95, 100, 115, 125, 135],
                    [70, 85, 90, 105, 115, 125]])
    print(255 - img)


def pq5():
    """Warehouse stock"""
    s = np.array([[10, 12, 15, 18, 20, 16, 14, 13, 11, 9],
                  [8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
                  [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
                  [30, 28, 26, 24, 22, 20, 18, 16, 14, 12]])
    print("Row totals:", s.sum(axis=1))
    print("Column totals:", s.sum(axis=0))
    print("Busiest shelf:", s.sum(axis=1).argmax() + 1)
    r, c = np.unravel_index(s.argmax(), s.shape)
    print(f"Maximum stocked bin: shelf {r + 1}, bin {c + 1}, value {s.max()}")


def pq6():
    """Traffic counts reshape"""
    v = np.array([120, 135, 140, 150, 160, 155, 148, 170, 180, 175, 190, 200,
                  210, 205, 198, 220, 230, 225, 240, 250, 245, 238, 230, 220])
    m = v.reshape(3, 8)
    print(m)
    r, c = np.unravel_index(m.argmax(), m.shape)
    print(f"Peak slot: junction {r + 1}, slot {c + 1}, count {m.max()}")
    print("Least busy junction:", m.sum(axis=1).argmin() + 1)
    print("Average count:", round(float(m.mean()), 2))


def pq7():
    """Heart rate reshape"""
    h = np.array([72, 74, 73, 75, 76, 74, 73, 72, 78, 80, 82, 79, 77, 76, 75, 74, 73, 72, 71, 70,
                  69, 68, 67, 66, 72, 74, 76, 78, 80, 82, 84, 83, 81, 79, 77, 75, 74, 73, 72, 71,
                  70, 69, 68, 67, 66, 65, 72, 74, 76, 78, 80, 82, 84, 86, 88, 85, 83, 81, 79, 77])
    print(h.reshape(12, 5))


def pq8():
    """Weighted revenue using matrix multiplication"""
    sales = np.array([[100, 120, 130, 140, 150], [110, 125, 135, 145, 155], [90, 100, 110, 120, 130],
                      [80, 95, 105, 115, 125], [70, 85, 95, 105, 115], [60, 75, 85, 95, 105],
                      [50, 65, 75, 85, 95]])
    w = np.array([2, 3, 1, 4, 5])
    print("Weighted revenue per store:", sales @ w)


def pq9():
    """Rainfall: first 15 vs last 15 days"""
    rain = np.random.randint(20, 121, size=(8, 30))
    first, last = rain[:, :15], rain[:, 15:]
    print("Average first 15 days:", round(float(first.mean()), 2))
    print("Average last 15 days:", round(float(last.mean()), 2))
    print("Wetter half:", "first 15" if first.mean() > last.mean() else "last 15")


def pq10():
    """Drone terrain grid"""
    g = np.random.randint(100, 501, size=(10, 10))
    r, c = np.unravel_index(g.argmax(), g.shape)
    print(f"Highest ridge: {g.max()} m at ({r}, {c})")
    r, c = np.unravel_index(g.argmin(), g.shape)
    print(f"Lowest valley: {g.min()} m at ({r}, {c})")
    print("Average elevation:", round(float(g.mean()), 2))
    print("Central 4x4:\n", g[3:7, 3:7])


if __name__ == "__main__":
    run(globals(), "Practical 6 - Arrays, Indexing, Slicing")
