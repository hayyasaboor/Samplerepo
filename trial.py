def odd_even(n):
    if n % 2 != 0 and n < 50:
        return "odd and less than 50"
    elif n % 2 == 0 and n > 100:
        return "even and greater than 100"
    else:
        return "other"
print(odd_even(456))