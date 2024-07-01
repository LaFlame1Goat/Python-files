import random
import math

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

    return (e, d, n, phi_n, p, q)

# Generate 8-bit keys
e_8, d_8, n_8, phi_n_8, p_8, q_8 = generate_keys(8)
print("8-bit Public Key:", e_8)
print("8-bit Private Key:", d_8)
print("n:", n_8)
print("Phi of n:", phi_n_8)
print("p:", p_8)
print("q:", q_8)

# Generate 16-bit keys
e_16, d_16, n_16, phi_n_16, p_16, q_16 = generate_keys(16)
print("\n16-bit Public Key:", e_16)
print("16-bit Private Key:", d_16)
print("n:", n_16)
print("Phi of n:", phi_n_16)
print("p:", p_16)
print("q:", q_16)
