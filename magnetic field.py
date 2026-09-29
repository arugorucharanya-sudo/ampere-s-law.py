import math

 Permeability of free space
mu_0 = 4 * math.pi * 10**-7

 Input values
I = float(input("Enter current (A): "))
r = float(input("Enter distance from conductor (m): "))

 Calculate magnetic field
B = (mu_0 * I) / (2 * math.pi * r)

 Calculate Ampere's circulation
circulation = B * 2 * math.pi * r

 Display results
print("\n--- Ampere's Law Calculation ---")
print("Current =", I, "A")
print("Distance =", r, "m")
print("Magnetic Flux Density =", B, "T")
print("Ampere's Law Result =", circulation, "T.m")
print("Expected value (mu0 * I) =", mu_0 * I, "T.m")
