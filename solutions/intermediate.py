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


def q11():
    # Q11. Counter counts frequencies
    from collections import Counter
    print("Q11:", Counter("aabb"))  # Counter({'a':2, 'b':2})


def q12():
    # Q12. filter keeps truthy predicate results
    print("Q12:", list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4])))  # [2, 4]


def q13():
    # Q13. sorted reverse
    print("Q13:", sorted([3, 1, 2], reverse=True))  # [3, 2, 1]


def q14():
    # Q14. dict merge operator
    a = {"x": 1}
    b = {"y": 2}
    print("Q14:", a | b)  # {'x': 1, 'y': 2}


def q15():
    # Q15. is (identity) vs == (equality)
    print("Q15:", "is checks object identity (same memory); == checks value "
          "equality.")


def q16():
    # Q16. re.search finds first match
    import re
    print("Q16:", re.search(r"\d+", "abc123").group())  # 123


def q17():
    # Q17. global for rebinding module-level names
    print("Q17:", "use 'global' only when you assign to a module-level "
          "variable inside a function.")


def q18():
    # Q18. shallow copy shares nested objects
    src = [[1, 2], [3, 4]]
    cp = src.copy()
    cp[0][0] = 99
    print("Q18:", src)  # [[99, 2], [3, 4]] (nested list mutated too)


def q19():
    # Q19. os.path.join builds a path
    import os
    print("Q19:", os.path.join("a", "b", "c"))  # a/b/c (or a\b\c on Windows)


def q20():
    # Q20. catching multiple exceptions
    print("Q20:", "except (ValueError, TypeError):  -> catches either type "
          "in one clause.")


if __name__ == "__main__":
    for fn in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
               q11, q12, q13, q14, q15, q16, q17, q18, q19, q20):
        fn()
