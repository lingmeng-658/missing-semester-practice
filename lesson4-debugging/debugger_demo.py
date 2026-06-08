def average(scores: list[int]) -> float:
    total = 0
    for score in scores:
        total += score

    return total / len(scores)


def passed_students(students: dict[str, list[int]]) -> list[str]:
    result = []

    for name, scores in students.items():
        avg = average(scores)
        if avg >= 60:
            result.append(name)

    return result


def main():
    students = {
        "Alice": [80, 90, 100],
        "Bob": [60, 60, 60],
        "Charlie": [],
        "David": [59, 61, 60],
    }

    passed = passed_students(students)
    print(passed)


if __name__ == "__main__":
    main()