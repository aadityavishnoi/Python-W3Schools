T = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("Tuple: ", T)
print("First Element: ", T[0])
print("Last Element: ", T[-1])
print("Slice: ", T[1:4])
print("Slice: ", T[4:1:-1])
print("Slice: ", T[1:7:2])
print(T[8:2:-2])

T1 = (10, 20, 30)
L = list(T1)
print(L)

T2 = (1, 2)
T3 = (3, 4)

T3 = T2 + T3
print(T3)

T4 = (1, 2, 4, 8, 9)
if 2 in T4:
    print("Yes")