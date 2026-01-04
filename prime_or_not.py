def is_prime(n: int) -> bool:
    return (
        n > 1
        and (n == 2 or n == 3 or n % 2 and n % 3)
        and all(n % i and n % (i + 2) for i in range(5, int(n**0.5) + 1, 6))
    )
