def CompoundInterest(p, r, t):
    A = p*(pow((1+(r/100)), t))
    CI = A - p
    print("\nCompound interest is", CI)

P=float(input("Principle : "))
R=float(input("Rate : "))
T=int(input("Time : "))
CompoundInterest(P, R, T)
