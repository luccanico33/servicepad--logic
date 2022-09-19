"""Code a program (in python) that displays the numbers from 1 to 100 on the
screen, substituting the multiples of 3 for the word "fizz", the multiples of
5 for "buzz" and the multiples of both, that is, the multiples of 3 and 5,
by the word "fizz buzz".
Plus: Implement a test to the task performed
(Preferably with UnitTest or pytest).

Plus: Implementar una prueba a la tarea realizada
(Preferiblemente con UnitTest o pytest)."""


def number_check(number_count: int):
    if number_count % 3 == 0 and number_count % 5 == 0:
        return "fizz buzz"
    elif number_count % 3 == 0:
        return "fizz"
    elif number_count % 5 == 0:
        return "buzz"
    else:
        return number_count


if __name__ == "__main__":
    number_count = 1
    while number_count <= 100:
        print(number_check(number_count))
        number_count += 1

    """for i in range(100):
        if number_count % 3 == 0 and number_count % 5 == 0:
            print("fizz buzz")
        elif number_count % 3 == 0:
            print("fizz")
        elif number_count % 5 == 0:
            print("buzz")
        else:
            print(number_count)
        number_count += 1"""
