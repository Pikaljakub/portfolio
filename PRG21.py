'''
Vzdálenost bodů A[1,2] a B[3,4] je 2.83 m.
'''
a = {'x': 1, 'y': 2}
b = {'x': 3, 'y': 4}

distance = (((a['x'] - b['x'])**2 + (a['y'] - b['y'])**2)**0.5)
print(f"Vzdálenost bodů A[{a['x']},a{a['y']}] a B[{b['x']},{b['y']}] je {distance:.2f} m.")
