import random, copy, time

Kiel = [["Landin", 0],  ["Sagosen", 0], ["Duvnjak", 0], ["Ekberg", 0], ["Pekeler", 0], ["Wiencek", 0], ["Weinhold", 0]]
sumKiel = copy.deepcopy(Kiel)
Barcelona = [["Möller", 0],  ["Palmarsson", 0], ["Cindric", 0], ["Gomez", 0], ["Mem", 0], ["Fabregas", 0], ["Janc", 0]]
sumBarcelona = copy.deepcopy(Barcelona)
PSG = [["Gérard", 0],  ["Prandi", 0], ["Remili", 0], ["Karabatic", 0], ["Hansen", 0], ["Nahi", 0], ["Kounkoud", 0]]
sumPSG = copy.deepcopy(PSG)
Veszprem = [["Corrales", 0],  ["Lékai", 0], ["Nenadic", 0], ["Yahia", 0], ["Nilsson", 0], ["Marguc", 0], ["Borozan", 0]]
sumVeszprem = copy.deepcopy(Veszprem)
Pick = [["Mikler", 0], ["Bánhidi", 0], ["Bodó", 0], ["Canellas", 0], ["Mackovsek",0], ["Radivojevic", 0], ["Bombac", 0]]
sumPick = copy.deepcopy(Pick)
Kielce = [["Wolff", 0], ["Dujshebaev", 0], ["Karacic", 0], ["Tournat", 0], ["Kulesh", 0], ["Gudjonsson", 0], ["Fernandez", 0]]
sumKielce = copy.deepcopy(Kielce)
Flensburg = [["Bergerud", 0], ["Sögard", 0], ["Gottfridsson", 0], ["Steinhauser", 0], ["Joendal", 0], ["Möller", 0], ["Wanne", 0]]
sumFlensburg = copy.deepcopy(Flensburg)
Aalborg = [["Gade", 0], ["Sandell", 0], ["Christensen", 0], ["Samuelsson", 0], ["Möllgaard", 0], ["Jensen", 0], ["Antonsen", 0]]
sumAalborg = copy.deepcopy(Aalborg)
teams = {"Flensburg": Flensburg, "Barcelona": Barcelona, "Kiel": Kiel, "Pick Szeged": Pick, "PSG": PSG, "Aalborg": Aalborg, "Kielce": Kielce, "Veszprém": Veszprem}
power = {"Kiel": 14, "Barcelona": 15, "PSG": 13, "Veszprém": 12, "Pick Szeged": 13, "Aalborg": 9, "Flensburg":11, "Kielce":12}
sum = {"Kiel": sumKiel, "Barcelona": sumBarcelona, "PSG": sumPSG, "Veszprém": sumVeszprem, "Pick Szeged": sumPick, "Aalborg": sumAalborg, "Flensburg": sumFlensburg, "Kielce": sumKielce}


def sortedScorers(team):
    sortScorers = sorted(dict(team).items(), key=lambda x: x[1], reverse=True)
    for i in sortScorers:
        if i[1] > 0:
            print(i[0], i[1])


def matchF4(Ateam, Bteam):
    global Agoal
    global Bgoal
    global tempA
    global tempB
    Agoal = 0
    Bgoal = 0
    tempA = copy.deepcopy(teams[Ateam])
    tempB = copy.deepcopy(teams[Bteam])
    print(f"\nKezdődik a mérkőzés: {Ateam} - {Bteam}")
    def goal(rand1, rand2):
        global Agoal
        global Bgoal
        x = random.randint(rand1, rand2)
        i = 0
        while i < x:
            a = power[Ateam] + random.randint(1, 50)
            b = power[Bteam] + random.randint(1, 50)
            if a > b:
                Agoal += 1
                y = random.randint(1, 6)
                scorer = teams[Ateam][y][0]
                sum[Ateam][y][1] += 1
                tempA[y][1] += 1
                print(f'{Agoal} - {Bgoal} a gólszerző: {scorer}')
            if a < b:
                Bgoal += 1
                y = random.randint(1, 6)
                scorer = teams[Bteam][y][0]
                sum[Bteam][y][1] += 1
                tempB[y][1] += 1
                print(f'{Agoal} - {Bgoal} a gólszerző: {scorer}')
            if a == b:
                side = random.randint(0, 1)
                if side == 0:
                    print(f'{teams[Ateam][0][0]} véd!')
                if side == 1:
                    print(f'{teams[Bteam][0][0]} véd!')
            i += 1
            time.sleep(0.3)
    goal(18, 35)
    print(f"Félidőben: {Agoal} - {Bgoal}")
    goal(18, 35)
    if Agoal == Bgoal:
        print(f'{Agoal} - {Bgoal}, hosszabbítás következik!')
        goal(4, 13)
    global winner
    global looser
    if Agoal > Bgoal:
        winner = Ateam
        looser = Bteam
    if Agoal < Bgoal:
        winner = Bteam
        looser = Ateam
    print(f"A végeredmény: {Ateam} - {Bteam}: {Agoal} - {Bgoal}")
    print(f"\nA {Ateam} góllövői:")
    sortedScorers(tempA)
    print(f"\nA {Bteam} góllövői:")
    sortedScorers(tempB)
    print(f"\nGyőzött a {winner}!")


Xgoal1 = 0
Xgoal2 = 0
Ygoal1 = 0
Ygoal2 = 0


def match(Ateam, Bteam, homeAdvantage):
    global Agoal
    global Bgoal
    global tempA
    global tempB
    Agoal = 0
    Bgoal = 0
    tempA = copy.deepcopy(teams[Ateam])
    tempB = copy.deepcopy(teams[Bteam])
    print(f"\nKezdődik a mérkőzés: {Ateam} - {Bteam}")
    def goal(rand1, rand2):
        global Agoal
        global Bgoal
        x = random.randint(rand1, rand2)
        i = 0
        while i < x:
            a = power[Ateam] + random.randint(1, 50) + homeAdvantage
            b = power[Bteam] + random.randint(1, 50)
            if a > b:
                Agoal += 1
                y = random.randint(1, 6)
                scorer = teams[Ateam][y][0]
                sum[Ateam][y][1] += 1
                tempA[y][1] += 1
                print(f'{Agoal} - {Bgoal} a gólszerző: {scorer}')
            if a < b:
                Bgoal += 1
                y = random.randint(1, 6)
                scorer = teams[Bteam][y][0]
                sum[Bteam][y][1] += 1
                tempB[y][1] += 1
                print(f'{Agoal} - {Bgoal} a gólszerző: {scorer}')
            if a == b:
                side = random.randint(0, 1)
                if side == 0:
                    print(f'{teams[Ateam][0][0]} véd!')
                if side == 1:
                    print(f'{teams[Bteam][0][0]} véd!')
            i += 1
            time.sleep(0.3)
    goal(18, 35)
    print(f"Félidőben: {Agoal} - {Bgoal}")
    goal(18, 35)
    if Agoal > Bgoal:
        print(f"\nGyőzött a {Ateam}!")
    if Agoal < Bgoal:
        print(f"\nGyőzött a {Bteam}!")
    else:
        print("\nDöntetlen a mérkőzés!")
    Xgoal1 = Agoal
    Ygoal1 = Bgoal
    print(f"\nA {Ateam} góllövői:")
    sortedScorers(tempA)
    print(f"\nA {Bteam} góllövői:")
    sortedScorers(tempB)
    print(f"A végeredmény: {Ateam} - {Bteam}: {Agoal} - {Bgoal}")
    
    print(f"\nKövetkezzen a visszavágó: {Bteam} - {Ateam}")
    Temp = Bteam
    Bteam = Ateam
    Ateam = Temp
    Agoal = 0
    Bgoal = 0
    tempA = copy.deepcopy(teams[Ateam])
    tempB = copy.deepcopy(teams[Bteam])
    goal(18, 35)
    print(f"Félidőben: {Agoal} - {Bgoal}")
    goal(18, 35)
    Temp = Bteam
    Bteam = Ateam
    Ateam = Temp
    if Agoal > Bgoal:
        print(f"\nGyőzött a {Ateam}!")
    if Agoal < Bgoal:
        print(f"\nGyőzött a {Bteam}!")
    else:
        print("\nDöntetlen a mérkőzés!")
    print(f"\nA {Bteam} góllövői:")
    sortedScorers(tempA)
    print(f"\nA {Ateam} góllövői:")
    sortedScorers(tempB)
    print(f"A végeredmény: {Bteam} - {Ateam}: {Agoal} - {Bgoal}")
    if (Xgoal1 == Agoal) & (Ygoal1 == Bgoal):
        print(f'{Xgoal1 + Bgoal} - {Ygoal1 + Agoal}, hosszabbítás következik!')
        goal(4, 13)
    print(f'\nÖsszesítésben: {Ateam} - {Bteam}: {Xgoal1 + Bgoal} - {Ygoal1 + Agoal}')
    global winner
    if (Xgoal1 + Bgoal) > (Ygoal1 + Agoal):
        winner = Ateam
    if (Xgoal1 + Bgoal) < (Ygoal1 + Agoal):
        winner = Bteam
    if (Xgoal1 + Bgoal) == (Ygoal1 + Agoal):
        if Ygoal1 > Bgoal:
            winner = Bteam
        if Ygoal1 < Bgoal:
            winner = Ateam
    print(f"\nGyőzött a {winner}!")


randomizate = input("Randomizáljunk-e?")
if randomizate == 'i':
    y = []
    x = random.sample(range(0, 8), 8)
    X = []
    j = 0
    while j < 8:
        y.append(int(x[j]))
        j += 1
    while j > 0:
        X.append(list(teams.keys())[y[j-1]])
        j -= 1
if randomizate != 'i':
    j = 0
    X = []
    while j < 8:
        X.append(list(teams.keys())[j])
        j += 1
print("Üdvözöljük a negyeddöntőben:")
time.sleep(0.3)
match(X[0], X[1], 3)
time.sleep(1)
Q1 = winner
time.sleep(1)
match(X[2], X[3], 3)
time.sleep(1)
Q2 = winner
match(X[4], X[5], 3)
time.sleep(1)
Q3 = winner
match(X[6], X[7], 3)
time.sleep(1)
Q4 = winner
time.sleep(1)

print('Üdvözöljük a 2020/21-es FINAL4 nézőit!')
time.sleep(3)
matchF4(Q1, Q2)
A1 = winner
A2 = looser
time.sleep(3)
matchF4(Q3, Q4)
A3 = winner
A4 = looser
print(f"\nA döntő a {A1} és a {A3} között zajlik majd, míg a {A2} és a {A4} a 3. helyért mérkőzik!")
time.sleep(3)
matchF4(A2, A4)
B3 = winner
B4 = looser
time.sleep(3)
matchF4(A1, A3)
B1 = winner
B2 = looser
time.sleep(1)
print(f"\nA torna góllövői: \n{B4}:")
sortedScorers(sum[B4])
time.sleep(1)
print(f"\n{B3}:")
sortedScorers(sum[B3])
time.sleep(1)
print(f"\n{B2}: ")
sortedScorers(sum[B2])
time.sleep(1)
print(f"\n{B1}: ")
sortedScorers(sum[B1])
print(f'\nAz idei FINAL4 végeredménye: \n1. helyezett: {B1}\n2. helyezett: {B2}\n3. helyezett: {B3}\n4. helyezett: {B4}')
print('F4Sim v1.5')
