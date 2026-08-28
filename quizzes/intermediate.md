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

### Q11. `collections.Counter`
What does `from collections import Counter; Counter("aabb")` give?

### Q12. `filter`
What is `list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4]))`?

### Q13. `sorted` reverse
What is `sorted([3, 1, 2], reverse=True)`?

### Q14. Merge dicts
For `a = {"x": 1}; b = {"y": 2}`, what is `a | b` (Python 3.9+)?

### Q15. `is` vs `==`
What is the difference between `is` and `==`?

### Q16. `re` match
What does `import re; re.search(r"\d+", "abc123").group()` return?

### Q17. `global` keyword
When do you need the `global` statement inside a function?

### Q18. Shallow vs deep copy
What is the risk of copying a nested list with `list.copy()`?

### Q19. `os.path.join`
What does `import os; os.path.join("a", "b", "c")` produce (on most systems)?

### Q20. Multiple except
How do you catch both `ValueError` and `TypeError` in one `except`?

---
➡️ Check answers in `solutions/intermediate.py`
