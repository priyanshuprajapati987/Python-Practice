# Advanced Python Practice

Try each **before** checking `solutions/advanced.py`.

---

### Q1. `staticmethod` vs `classmethod`
What is the first parameter of a `@classmethod`?

### Q2. `itertools.count`
What does `itertools.count(10)` produce? How do you stop it?

### Q3. Generator `send`
What does `.send(value)` do on a generator?

### Q4. Property decorator
How do you make a method act like a read-only attribute?

### Q5. `functools.lru_cache`
What does decorating a function with `@lru_cache` do?

### Q6. Context manager protocol
Which two methods must a class implement to be usable in `with`?

### Q7. `threading` vs `multiprocessing`
Which is better for CPU-bound work in Python and why?

### Q8. `dataclass`
What does `@dataclass` auto-generate for a class?

### Q9. Walrus operator
What does `if (n := len(x)) > 5:` do?

### Q10. `asyncio.gather`
What does `asyncio.gather(*coros)` return?

### Q11. `__init_subclass__`
What special method lets a parent class react when a subclass is created?

### Q12. Descriptor protocol
Which methods (`__get__`, `__set__`, `__delete__`) make an object a descriptor?

### Q13. `yield from`
What does `yield from iterable` do compared to `for x in iterable: yield x`?

### Q14. `inspect` module
Which module lets you introspect a function's parameters at runtime?

### Q15. `asyncio.Lock`
Why use `async with lock:` instead of a plain variable for concurrent access?

### Q16. `functools.partial`
What does `functools.partial(sorted, reverse=True)` create?

### Q17. `contextlib.suppress`
What does `with contextlib.suppress(FileNotFoundError):` do?

### Q18. `dataclasses.field`
How do you give a field a default factory (e.g. a new list per instance)?

### Q19. `abc.ABC` + `@abstractmethod`
How do you force subclasses to implement a method?

### Q20. `concurrent.futures`
Which executor runs callables in separate threads, and which in processes?

### Q21. `asyncio.run`
How do you execute a coroutine `main()` from synchronous code?

### Q22. `type()` as metaclass
What does `type("Point", (object,), {"x": 0})` create?

### Q23. `contextlib.contextmanager`
In a `@contextmanager` function, what does `yield` separate?

### Q24. `functools.reduce`
What does `from functools import reduce; reduce(lambda a, b: a + b, [1, 2, 3, 4])` return?

### Q25. `__getattr__` vs `__getattribute__`
What is the key difference between `__getattr__` and `__getattribute__`?

---
➡️ Check answers in `solutions/advanced.py`
