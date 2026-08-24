"""Interactive Python practice quiz runner.

Run:  python quiz_runner.py
"""

QUIZ = [
    ("beginner", "What is 2 ** 5?", "32"),
    ("beginner", "For s='code', what is s[1]?", "o"),
    ("beginner", "'banana'.count('a') is?", "3"),
    ("beginner", "round(3.14159, 2) is?", "3.14"),
    ("intermediate", "{1,2,3} & {2,3,4} is?", "{2, 3}"),
    ("intermediate", "'-'.join(['a','b','c']) is?", "a-b-c"),
    ("intermediate", "any([0,0,1]) is?", "True"),
    ("intermediate", "map(str,[1,2,3]) -> list is?", "['1', '2', '3']"),
    ("advanced", "First param of a @classmethod is?", "cls"),
    ("advanced", "Which is better for CPU-bound: threading or multiprocessing?", "multiprocessing"),
]


def ask(question, expected):
    try:
        ans = input(f"\n❓ {question}\n> ").strip()
    except EOFError:
        ans = ""
    correct = ans.lower() == expected.lower()
    print(f"{'✅' if correct else '❌'}  expected: {expected}")
    return correct


def main():
    print("🐍 Python Practice Quiz\n(Type your answer and press Enter.)\n")
    score = 0
    for level, question, expected in QUIZ:
        print(f"[{level.upper()}]")
        if ask(question, expected):
            score += 1
    total = len(QUIZ)
    print(f"\n{'='*30}\n🏁 Score: {score}/{total}  ({score*100//total}%)")


if __name__ == "__main__":
    main()
