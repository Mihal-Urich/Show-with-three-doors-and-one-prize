import random

class Doors:
    def __init__(self) -> None:
        self.doors = [0, 0, 0]
        self.doors[random.randint(0, 2)] = 1
        self.player_number = -1

    def AskPlayerChoise(self, x) -> None:
        self.player_number = x

    def SayWrongDoor(self) -> int:
        for i in range(3):
            if (self.doors[i] != 1 and i != self.player_number):
                return i
            
    def SayGameResults(self) -> bool:
        return self.doors[x] == 1
    

class Player:
    def __init__(self) -> None:
        self.player_number = random.randint(0, 2)

    def SayNumber(self) -> int:
        return self.player_number

    def ChangeAnswer(self, wrong : int):
        for i in range(3):
            if (i != self.player_number and i != wrong):
                self.player_number = i
                break

iters = 1000000
cnt1 = 0
for i in range(iters):
    d = Doors()
    p = Player()
    d.AskPlayerChoise(p.SayNumber())
    wrong =  d.SayWrongDoor()
    p.ChangeAnswer(wrong)
    if (d.doors[p.player_number] == 1):
        cnt1 += 1
print(cnt1/iters * 100, "%")

cnt2 = 0
for i in range(iters):
    d = Doors()
    p = Player()
    if (d.doors[p.player_number] == 1):
        cnt2 += 1
print(cnt2/iters * 100, "%")
