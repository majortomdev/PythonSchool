def my_generator():
    x = 0

    while True:
        x += 1
        yield x


practice_generator = my_generator()

print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print()


def my_generator():
    num = 0
    while True:
        num += 7
        yield num


practice_generator = my_generator()

print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
