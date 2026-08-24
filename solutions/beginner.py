"""Solutions for beginner Python practice questions.

Run directly to print all answers.
"""


def q1():
    # Q1. Type conversion
    print("Q1:", int("42"), str(3.14))  # 42 3.14


def q2():
    # Q2. Power operator
    print("Q2:", 2 ** 5)  # 32


def q3():
    # Q3. String indexing & slice
    s = "code"
    print("Q3:", s[1], s[1:3])  # o od


def q4():
    # Q4. Substring membership
    s = "hello world"
    print("Q4:", "world" in s)  # True


def q5():
    # Q5. str.count
    print("Q5:", "banana".count("a"))  # 3


def q6():
    # Q6. while loop
    out = []
    i = 0
    while i < 3:
        out.append(str(i))
        i += 1
    print("Q6:", " ".join(out))  # 0 1 2


def q7():
    # Q7. list.pop removes & returns last
    a = [10, 20, 30]
    popped = a.pop()
    print("Q7 pop:", popped, "| list:", a)  # 30 | [10, 20]


def q8():
    # Q8. round to N decimals
    print("Q8:", round(3.14159, 2))  # 3.14


def q9():
    # Q9. comparison chaining
    print("Q9:", 1 < 2 < 3)  # True


def q10():
    # Q10. ternary expression
    x = 5
    print("Q10:", "yes" if x > 3 else "no")  # yes


if __name__ == "__main__":
    for fn in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        fn()
