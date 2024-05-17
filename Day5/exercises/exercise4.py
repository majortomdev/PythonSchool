def count_primes(number):
    prime_numbers =[2]
    pinpoint=3

    if number == 0 or number ==1:
        return 0

    while pinpoint<=number:
        for n in range(3,pinpoint,2):
            if pinpoint %n == 0:
                pinpoint += 2
                break
        else:
            prime_numbers.append(pinpoint)
            pinpoint+=2
    print(f"There were {len(prime_numbers)} primes found")
    print(prime_numbers)
    return len(prime_numbers);


print(count_primes(50))