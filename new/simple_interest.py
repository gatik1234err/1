def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = 1000
r = 5
t = 3

si = simple_interest(p, r, t)
print("Simple Interest is:", si)