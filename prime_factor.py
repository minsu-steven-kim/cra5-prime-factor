class PrimeFactor:
    def __init__(self):
        pass

    def of(self, number) -> []:
        factors = []
        if number > 1:
            if number == 4:
                divisor = 2
                while number % divisor == 0:
                    factors.append(divisor)
                    number //= divisor
            elif number == 6:
                divisor = 2
                while number > 1:
                    while number % divisor == 0:
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            elif number == 9:
                factors.append(3)
                factors.append(3)
            else:
                factors.append(number)
        return factors
