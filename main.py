import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
      if (n%i) == 0 or n == 1:
        return False
    return True

# Tester plusieurs nombres différents

print(is_prime(5))   # True
print(is_prime(10))  # False
print(is_prime(13))  # True
print(is_prime(15))  # False
print(is_prime(29))  # True
print(is_prime(30))  # False

# Tester les valeurs limites

print(is_prime(1))   # False
print(is_prime(2))   # True
print(is_prime(3))   # True
print(is_prime(4))   # False
print(is_prime(2147483647))   # True, le plus grand nombre premier possible pour les entiers signés de 32 bits