from typing import List


def arithmetic_arranger(problems: List[str], show_answer: bool = False) -> str:
    arranged_problems = ""
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    operations = list(map(lambda element: element.split()[1], problems))
    if set(operations) != {"+", "-"} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []
    for problem in problems:
        elements = problem.split()
        numbers.extend([elements[0], elements[2]])

    if not all(map(lambda element: element.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda element: len(element) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    first_row = ""
    separators = ""
    values = list(map(lambda x: eval(x), problems))
    results = ""
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        first_row += numbers[i].rjust(space_width)
        separators += "-" * space_width
        results += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            first_row += " " * 4
            separators += " " * 4
            results += " " * 4

    last_row = ""
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        last_row += operations[i // 2]
        last_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            last_row += " " * 4

    if show_answer:
        arranged_problems = "\n".join((first_row, last_row, separators, results))
    else:
        arranged_problems = "\n".join((first_row, last_row, separators))
    return arranged_problems
