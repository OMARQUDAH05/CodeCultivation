class plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    def show(self)->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    p1 = plant("Rose", 25, 30)
    p2 = plant("Sunflower",80,45)
    p3 = plant("Cacuts",15,120)
    print("=== Garden Plant Registry ===")
    p1.show()
    p2.show()
    p3.show()


if __name__ == "__main__":
    main()
