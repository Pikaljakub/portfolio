import random
w, h, mines = 5, 3, 16
field = [[0 for y in range(h)] for x in range(w)]
if mines > w*h:
    mines = 0
    print("Error: Too many mines.")
for i in range(mines):
    while True:
        rx = random.randint(0, w -1)
        ry = random.randint(0, h -1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break

    field[rx][ry] = "M"
   
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()