def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
            if number < 100:
                print(" ", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
            if number < 100:
                print(" ", end="")
        elif number % 3 == 0:
            print("Fizz", end="")
            if number < 100:
                print(" ", end="")
        else:
            print("{:d}".format(number), end="")
            if number < 100:
                print(" ", end="")