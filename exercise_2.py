"""In mathematics, the Fibonacci sequence or serie is the following infinite
sequence of natural numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610 ...
where f (0) = 0, f (1) = 1 and f (n) = f (n-1) + f (n-2).
Code a program (in python) that solves for any number in the Fibonacci series.
Plus: Implement a test to the task performed
(Preferably with UnitTest or Pytest).

Plus: Implementar una prueba a la tarea realizada
(Preferiblemente con UnitTest o Pytest)."""

seq_fibo = {}


def counter_fibo(num: int):
    """function designed to calculate the value of the fibonacci sequence depending on the input value

    Args:
        num (int): input value to calculate the corresponding value of the fibonacci sequence

    Raises:
        Exception: cannot be calculated with values less than zero
    """
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return "unable to get a value"
    elif num in seq_fibo:
        return seq_fibo[num]

    res = counter_fibo(num - 1) + counter_fibo(num - 2)
    seq_fibo[num] = res
    return res


if __name__ == "__main__":

    value_in = int(input("enter a number to get the Fibonacci value: "))

    res = counter_fibo(value_in)
    print(f"{value_in} ==> {res}")
