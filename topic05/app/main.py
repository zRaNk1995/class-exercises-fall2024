def add_nums(a: int, b: int) -> int:
    return a + b


def prompt_user_for_number() -> int:
    return int(input("Please enter an integer: "))


def add_nums_from_user_input() -> None:

    num1 = prompt_user_for_number()
    num2 = prompt_user_for_number()
    print(f"The sum of {num1} + {num2} is:", add_nums(num1, num2))


if __name__ == "__main__":
    add_nums_from_user_input()
