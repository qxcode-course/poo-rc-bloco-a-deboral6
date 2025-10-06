class Car:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self):
        return f"pass:{self.pass_}, gas:{self.gas}, km:{self.km}"

    def show(self):
        print(self)

    def enter(self):
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount):
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return

        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if distance <= self.gas:
            self.gas -= distance
            self.km += distance
        else:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
