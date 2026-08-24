"""Solutions for intermediate Python practice questions.

Run directly to print all answers.
"""


def q1():
    # Q1. set intersection & union
    print("Q1:", {1, 2, 3} & {2, 3, 4}, {1, 2} | {3})  # {2,3} {1,2,3}


def q2():
    # Q2. conditional dict comprehension
    d = {x: x * x for x in range(10) if x % 2 == 0}
    print("Q2:", d)  # {0:0, 2:4, 4:16, 6:36, 8:64}


def q3():
    # Q3. str.join
    print("Q3:", "-".join(["a", "b", "c"]))  # a-b-c


def q4():
    # Q4. any / all
    print("Q4:", any([0, 0, 1]), all([1, 2, 3]))  # True True


def q5():
    # Q5. nested list indexing
    m = [[1, 2], [3, 4]]
    print("Q5:", m[1][0])  # 3


def q6():
    # Q6. else runs only when no exception
    print("Q6:", "the 'else' block (runs only if try finished without error)")


def q7():
    # Q7. inheritance check
    class A:
        pass
    class B(A):
        pass
    print("Q7:", issubclass(B, A))  # True


def q8():
    # Q8. defaultdict auto-defaults missing keys
    from collections import defaultdict
    d = defaultdict(int)
    d["x"] += 1
    print("Q8:", d["x"])  # 1


def q9():
    # Q9. starred unpacking
    first, *rest = [1, 2, 3, 4]
    print("Q9:", first, rest)  # 1 [2, 3, 4]


def q10():
    # Q10. map applies a function
    print("Q10:", list(map(str, [1, 2, 3])))  # ['1', '2', '3']


if __name__ == "__main__":
    for fn in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        fn()
