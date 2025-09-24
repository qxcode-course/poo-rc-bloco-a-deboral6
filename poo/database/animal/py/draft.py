class animal:
    def __init__(self, species: str, age:int, sound: str):
        self.species: str = species
        self.age: int = 0
        self.sound: str = sound

    def emitirSom(self) -> None:
        if self.age == 0:
            print("")
        if self.age == 4:
            print("RIP")
        else:
            print(self.sound)
    def __str__(self) -> str:
        return f"{self.species}: {self.age}: {self.sound}"
    
    def ageBy(self, increment:int):
        if self.age == 4:
            print(f"warning: {self.species} morreu.")
            return
        self.age += increment
        
def main():

        

 