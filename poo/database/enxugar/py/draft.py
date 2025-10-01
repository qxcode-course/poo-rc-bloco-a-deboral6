class Towel:
    def __init__(self, color: str, size: str): 
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
    
    def isMaxWetness(self) -> int:
        if self.size == "P": 
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
    
    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            print("toalha encharcada")
            self.wetness = self.isMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0

    def __str__(self) -> str: 
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():   
    towel = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "criar":
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color, size)
        elif args[0] == "seca":
            if towel is None:
                print("fail: nenhuma toalha criada")
            else:
                print("sim" if towel.isDry() else "nao")
        elif args[0] == "torcer":
            if towel is None:
                print("fail: nenhuma toalha criada")
            else:
                amount: int = int(args[1])
                towel.dry(amount)
        elif args[0] == "mostrar":
            if towel is None:
                print("fail: nenhuma toalha criada")
            else:
                print(towel)
        else:
            print("fail: comando não encontrado")

main()
