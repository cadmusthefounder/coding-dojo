def fizz_buzz(x):
    result = []
    for item in range(1, x+1):
        if item%3 == 0 and item%5 == 0:
            result.append("FizzBuzz")
        elif item%3 == 0:
            result.append("Fizz")
        elif item%5 ==0:
            result.append("Buzz")
        else:
            result.append(item)
            
    return result