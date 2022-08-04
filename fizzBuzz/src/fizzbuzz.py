def fizzbuzz(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return "fizzbuzz"
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)