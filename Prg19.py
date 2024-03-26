import random

colors = {"r": "red", "g": "green", "b": "blue","m": "magenta" }
secret = []
cnt_field = 3 

color_codes = []
for code in colors:
    color_codes.append(code)
    rnd = random.randint(0,len(colors)-1)
    code = color_codes[rnd]
    color = colors[code]
print(secret)