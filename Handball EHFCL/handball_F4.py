import random, copy, time
Kiel = [["Landin", 0],  ["Sagosen", 0], ["Duvnjak", 0], ["Ekberg", 0], ["Pekeler", 0], ["Wiencek", 0], ["Weinhold", 0]]
sumKiel = copy.deepcopy(Kiel)
Barcelona = [["Möller", 0],  ["Palmarsson", 0], ["Cindric", 0], ["Enterrios", 0], ["Mem", 0], ["Fabregas", 0], ["Janc", 0]]
sumBarcelona = copy.deepcopy(Barcelona)
PSG = [["Gérard", 0],  ["Prandi", 0], ["Remili", 0], ["Karabatic", 0], ["Hansen", 0], ["Nahi", 0], ["Kounkoud", 0]]
sumPSG = copy.deepcopy(PSG)
Veszprem = [["Corrales", 0],  ["Lékai", 0], ["Nenadic", 0], ["Yahia", 0], ["Nilsson", 0], ["Marguc", 0], ["Borozan", 0]]
sumVeszprem = copy.deepcopy(Veszprem)
Pick = [["Mikler", 0], ["Bánhidi", 0], ["Bodó", 0], ["Canellas", 0], ["Mackovsek", 0], ["Radivojevic", 0], ["Bombac", 0]]
sumPick = copy.deepcopy(Pick)
teams = {"Kiel": Kiel, "Barcelona": Barcelona, "PSG": PSG, "Veszprém": Veszprem, "Pick Szeged": Pick}
power = {"Kiel": 14, "Barcelona": 15, "PSG": 13, "Veszprém": 11, "Pick Szeged": 11}
sum = {"Kiel": sumKiel, "Barcelona": sumBarcelona, "PSG": sumPSG, "Veszprém": sumVeszprem, "Pick Szeged": sumPick}


def sortedScorers(team):
    sortScorers = sorted(dict(team).items(), key=lambda x: x[1], reverse=True)
    for i in sortScorers:
        if i[1] > 0:
            print(i[0], i[1])


def match(Ateam, Bteam):
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


print('Üdvözöljük a 2020/21-es FINAL4 nézőit!')
time.sleep(1)
match('PSG', 'Barcelona')
A1 = winner
A2 = looser
time.sleep(1)
match('Pick Szeged', 'Veszprém')
B1 = winner
B2 = looser
print(f"\nA döntő a {A1} és a {B1} között zajlik majd, míg a {A2} és a {B2} a 3. helyért mérkőzik!")
time.sleep(3)
match(A2, B2)
C3 = winner
C4 = looser
time.sleep(1)
match(A1, B1)
C1 = winner
C2 = looser
time.sleep(1)
print("\nA torna góllövői: \nBarcelona:")
sortedScorers(sumBarcelona)
print("\nPick Szeged: ")
sortedScorers(sumPick)
time.sleep(1)
print("\nPSG: ")
sortedScorers(sumPSG)
time.sleep(1)
print("\nVeszprém: ")
sortedScorers(sumVeszprem)
time.sleep(1)
print(f'\nAz idei FINAL4 végeredménye: \n1. helyezett: {C1}\n2. helyezett: {C2}\n3. helyezett: {C3}\n4. helyezett: {C4}')
print('F4Sim v1.3')
