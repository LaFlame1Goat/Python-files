import random
import math
import time

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Mod_Inverse does not exist")

def generate_keys(bits):
    min_value = 2 ** (bits // 2)
    max_value = 2 ** (bits // 2 + 1) - 1
    
    start_time = time.time()
    
    p = generate_prime(min_value, max_value)
    q = generate_prime(min_value, max_value)

    while p == q:
        q = generate_prime(min_value, max_value)

    n = p * q
    phi_n = (p-1) * (q-1)

    e = random.randint(3, phi_n-1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    d = mod_inverse(e, phi_n)

    end_time = time.time()
    runtime = (end_time - start_time) * 1000 

    return (e, d, n, phi_n, p, q, runtime)

for bits in [8, 16]:
    e, d, n, phi_n, p, q, runtime = generate_keys(bits)
    print(f"\n{bits}-bit keys generated in {runtime:.6f} milliseconds.")
    print("Public Key:", e)
    print("Private Key:", d)
    print("n:", n)
    print("Phi of n:", phi_n)
    print("p:", p)
    print("q:", q)
