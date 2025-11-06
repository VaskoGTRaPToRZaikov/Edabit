def fizz_buzz(num):
    if num % 3 == 0:
        if num % 5 ==0:
            return "FizzBuzz"
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"

    return str(num)


