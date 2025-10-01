class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.age: int = 0
        self.sound: str = sound

    def noise(self) -> None:
        if self.age == 0:
            print("---")
        elif self.age == 4:
            print("RIP")
        else:
            print(self.sound)

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

    def grow(self, increment: int):
        if self.age == 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

def main():
    animal: Animal = Animal("", "")
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        print(f"${line}")
        args: list[str] = line.split()

        if not args:
            continue

        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "init":
            if len(args) < 3:
                print("fail: uso correto é init <especie> <som>")
                continue
            especie = args[1]
            som = args[2]
            animal = Animal(especie, som)
        elif cmd == "show":
            print(animal)
        elif cmd == "grow":
            if len(args) < 2:
                print("fail: forneça um valor para grow")
                continue
            try:
                increment = int(args[1])
                animal.grow(increment)
            except ValueError:
                print("fail: valor de grow deve ser um número inteiro")
        elif cmd == "noise":
            animal.noise()
        else:
            print("fail: comando não encontrado")

if __name__ == "__main__":
    main()
