t = 10e-9
E = 12e-3
a = 2.5e-1
b = 2.6e-1
s = (a / 2) * (b / 2) * 3.14
print(s)
Ps = E / (t * s)
print("{:.1f} МВт/см2".format(Ps*1e-6))
