def solve_circuit(A, B, C):
    nand_ab = not (A and B)
    nor_bc = not (B or C)
    nand_bc = not (B and C)

    and_1 = nand_ab and nor_bc
    and_2 = nor_bc and nand_bc

    Q = and_1 or and_2
    
    return int(Q)

print("A | B | C | Q")
print("-------------")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            Q = solve_circuit(A, B, C)
            print(f"{A} | {B} | {C} | {Q}")