class Calculator:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, value: int):
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def useBattery(self) -> bool:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return False
        self.battery -= 1
        return True

    def sum(self, a: float, b: float):
        if not self.useBattery():
            return
        self.display = a + b

    def div(self, a: float, b: float):
        if not self.useBattery():
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b

def main():
    calc = None
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            calc = Calculator(int(args[1]))
        elif args[0] == "charge":
            calc.charge(int(args[1]))
        elif args[0] == "sum":
            calc.sum(float(args[1]), float(args[2]))
        elif args[0] == "div":
            calc.div(float(args[1]), float(args[2]))
        elif args[0] == "show":
            print(calc)
        else:
            print("fail: comando invalido")