cnt = 0
iter = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a < b and b < c and c < d and a + b + c +d == 13:
                    print(f"{a}{b}{c}{d}")
                    cnt += 1
                iter += 1
