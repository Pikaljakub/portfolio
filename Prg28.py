num = 7

def je_prvocislo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(je_prvocislo(num))