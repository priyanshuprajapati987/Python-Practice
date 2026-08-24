# Intermediate Python Practice

Try each **before** checking `solutions/intermediate.py`.

---

### Q1. Set operations
What is `{1, 2, 3} & {2, 3, 4}` and `{1, 2} | {3}`?

### Q2. Dict comprehension with condition
Build a dict `{x: x*x for x in range(10) if x % 2 == 0}`. What does it contain?

### Q3. `join`
What is `"-".join(["a", "b", "c"])`?

### Q4. `any` / `all`
What is `any([0, 0, 1])` and `all([1, 2, 3])`?

### Q5. Nested lists
For `m = [[1, 2], [3, 4]]`, what is `m[1][0]`?

### Q6. Try/except else/finally
In `try/except/else/finally`, which block runs only when there is NO exception?

### Q7. Class inheritance
If `class B(A): pass`, what does `issubclass(B, A)` return?

### Q8. `defaultdict`
With `from collections import defaultdict`, what does `d = defaultdict(int); d["x"] += 1` leave in `d["x"]`?

### Q9. `*rest` unpacking
For `first, *rest = [1, 2, 3, 4]`, what is `first` and `rest`?

### Q10. `map`
What does `list(map(str, [1, 2, 3]))` produce?

---
➡️ Check answers in `solutions/intermediate.py`
