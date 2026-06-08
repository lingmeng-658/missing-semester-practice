from math_utils import calculate_tax, Student
import math


def main():
    total = calculate_tax(100, 0.13)
    student = Student("lingmeng", 85)

    print(total)
    print(student.passed())
    print(math.sqrt(16))

if __name__ == "__main__":
    main()