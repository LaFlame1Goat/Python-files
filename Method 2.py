def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def find_private_key_brute_force(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"n: {n}")
    print(f"phi: {phi}")
    
    d = mod_inverse(e, phi)
    
    if d is not None:
        print(f"Private key d: {d}")
        return d
    else:
        print("No valid private key found.")
        return None

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public exponent e: "))

find_private_key_brute_force(p, q, e)
