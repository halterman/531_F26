from math import log2


A = 5

for n in range(1, 100):
    print(f"{2**(A * log2(n)):20.1f}  {n**A:20.1f}")
    

