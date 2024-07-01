def trial_division_factorization(N):
    factors = []
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            factors.append(i)
            N //= i
    if N > 1:
        factors.append(N)
    return factors

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def compute_private_exponent(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e and phi are not coprime")
    d = x % phi
    return d

def factorize_and_compute_private_key(N, e):
    factors = trial_division_factorization(N)
    if len(factors) != 2:
        raise ValueError("N should have exactly two prime factors for RSA")
    p, q = factors
    phi = (p - 1) * (q - 1)
    d = compute_private_exponent(e, phi)
    return d

N = int(input("Enter the modulus N: "))
e = int(input("Enter the public exponent e: "))

try:
    d = factorize_and_compute_private_key(N, e)
    print("Private exponent d:", d)
except ValueError as ve:
    print("Error:", ve)
