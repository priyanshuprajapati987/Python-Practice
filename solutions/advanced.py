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


def q11():
    # Q11. __init_subclass__ hook
    print("Q11:", "__init_subclass__ (classmethod) is called on the parent "
          "whenever a subclass is defined.")


def q12():
    # Q12. descriptor protocol
    print("Q12:", "Defining __get__ makes it a non-data descriptor; "
          "adding __set__ makes it a data descriptor. __delete__ is optional.")


def q13():
    # Q13. yield from delegates
    def gen():
        yield from [1, 2, 3]
    print("Q13:", list(gen()))  # [1, 2, 3] (same as yielding each item)


def q14():
    # Q14. inspect module
    import inspect
    print("Q14:", "the 'inspect' module (e.g. inspect.signature(func)) "
          "lets you read parameters at runtime.")


def q15():
    # Q15. asyncio.Lock for coroutine safety
    print("Q15:", "async with lock: serializes concurrent coroutines safely; "
          "a plain variable isn't atomic under the event loop.")


def q16():
    # Q16. functools.partial pre-fills arguments
    from functools import partial
    rev_sorted = partial(sorted, reverse=True)
    print("Q16:", rev_sorted([3, 1, 2]))  # [3, 2, 1]


def q17():
    # Q17. contextlib.suppress swallows listed exceptions
    import contextlib
    print("Q17:", "with contextlib.suppress(FileNotFoundError): silently "
          "ignores that exception if it occurs.")


def q18():
    # Q18. field(default_factory=...) builds a fresh value per instance
    from dataclasses import dataclass, field

    @dataclass
    class B:
        items: list = field(default_factory=list)
    print("Q18:", B().items, B().items is B().items)  # [] False


def q19():
    # Q19. abc forces subclass implementation
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            ...
    print("Q19:", "a subclass of Shape cannot be instantiated until it "
          "implements area().")


def q20():
    # Q20. concurrent.futures executors
    print("Q20:", "ThreadPoolExecutor runs in threads; "
          "ProcessPoolExecutor runs in separate processes (beats GIL).")


if __name__ == "__main__":
    for fn in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
               q11, q12, q13, q14, q15, q16, q17, q18, q19, q20):
        fn()
