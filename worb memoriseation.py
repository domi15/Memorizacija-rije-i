import random
lista = ["balon", "škola", "crvenilo", "sladoled", "krov", "izvanzemaljac", "pahulja", "gitara", "leptir", "šumski požar", "knjiga", "kaktus", "cipelica", "oblak", "roda", "harmonika", "čarape", "plava boja", "flamingo", "jastuk", "skakavac", "četka za kosu", "ledena ploča", "sljeme", "žirafa", "planina", "kišobran", "konj", "luben"]
br = 0
li = []
while True:
    a = lista[random.randint(0,29)]
    print(a)
    s = input()
    if a in li and s == 'v':
        br += 1
    elif a not in li and s == 'n':
        br += 1
        li.append(a)
    else:
        break
print('Game Over, Score:', br)
