"""Solutions for advanced Python practice questions.

Run directly to print all answers.
"""


def q1():
    # Q1. classmethod first param is the class (cls)
    print("Q1:", "A @classmethod's first parameter is the class itself, "
          "conventionally named 'cls'.")


def q2():
    # Q2. itertools.count is an infinite iterator
    import itertools
    c = itertools.count(10)
    print("Q2:", next(c), next(c))  # 10 11 (stop by taking only what you need,
    #       or wrap with itertools.islice)


def q3():
    # Q3. generator.send pushes a value into the generator
    def gen():
        x = yield 0
        yield x
    g = gen()
    next(g)            # prime it
    print("Q3:", g.send(42))  # 42


def q4():
    # Q4. @property makes a method look like an attribute
    class C:
        @property
        def name(self):
            return "x"
    print("Q4:", C().name)  # x  (accessed without parentheses)


def q5():
    # Q5. lru_cache memoizes results
    from functools import lru_cache
    print("Q5:", "@lru_cache caches return values keyed by arguments, "
          "speeding up repeated calls.")


def q6():
    # Q6. context manager protocol
    print("Q6:", "A class needs __enter__(self) and __exit__(self, ...) "
          "to be used in 'with'.")


def q7():
    # Q7. multiprocessing for CPU-bound
    print("Q7:", "multiprocessing (separate processes) beats threading for "
          "CPU-bound work because it bypasses the GIL.")


def q8():
    # Q8. dataclass generates boilerplate
    print("Q8:", "@dataclass auto-generates __init__, __repr__, __eq__, "
          "and other dunder methods from the fields.")


def q9():
    # Q9. walrus operator assigns inside an expression
    x = [1, 2, 3, 4, 5, 6]
    if (n := len(x)) > 5:
        print("Q9:", f"length is {n}")  # length is 6


def q10():
    # Q10. asyncio.gather runs coroutines concurrently
    import asyncio
    async def a():
        return 1
    async def b():
        return 2
    print("Q10:", asyncio.run(asyncio.gather(a(), b())))  # [1, 2]


if __name__ == "__main__":
    for fn in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        fn()
